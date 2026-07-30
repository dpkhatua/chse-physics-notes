const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');
const rough = require('roughjs');

const dom = new JSDOM('<!doctype html><html><body></body></html>');
global.window = dom.window;
global.document = dom.window.document;

const SVG_NS = 'http://www.w3.org/2000/svg';

var INK = '#23324a';
var BLUE = '#1e5fb4';
var ORANGE = '#e0762b';
var TEAL = '#0e8a7d';
var PURPLE = '#7b4fb0';
var PINK = '#d1467a';
var GREEN = '#2f9e44';

let currentSize = { w: 480, h: 260 };
let lastSvgEl = null;

// Auto-appending proxy: every RoughSVG drawing call's returned node gets appended to svgEl automatically,
// so the diagram function bodies (unchanged from sketch.js) don't need to know they're targeting SVG now.
function makeAutoAppendRC(svgEl, roughSvg) {
  return new Proxy(roughSvg, {
    get(target, prop) {
      const orig = target[prop];
      if (typeof orig === 'function') {
        return function (...args) {
          const node = orig.apply(target, args);
          if (node && typeof node.nodeType !== 'undefined') {
            svgEl.appendChild(node);
          }
          return node;
        };
      }
      return orig;
    },
  });
}

function setup(canvasId) {
  const svgEl = document.createElementNS(SVG_NS, 'svg');
  svgEl.setAttribute('viewBox', `0 0 ${currentSize.w} ${currentSize.h}`);
  svgEl.setAttribute('width', String(currentSize.w));
  svgEl.setAttribute('height', String(currentSize.h));
  svgEl.setAttribute('xmlns', SVG_NS);
  svgEl.setAttribute('class', 'hand-diagram');
  const roughSvg = rough.svg(svgEl);
  const rc = makeAutoAppendRC(svgEl, roughSvg);
  lastSvgEl = svgEl;
  return { canvas: null, rc: rc, ctx: svgEl, w: currentSize.w, h: currentSize.h };
}

// label(ctx, x, y, text, opts): ctx here is actually the svgEl (repurposed) — append a <text> node.
function label(ctx, x, y, text, opts) {
  opts = opts || {};
  const t = document.createElementNS(SVG_NS, 'text');
  t.setAttribute('x', x);
  t.setAttribute('y', y);
  t.setAttribute('font-family', "'Kalam', 'Comic Sans MS', cursive");
  t.setAttribute('font-size', (opts.size || 18));
  t.setAttribute('fill', opts.color || INK);
  const align = opts.align || 'left';
  t.setAttribute('text-anchor', align === 'center' ? 'middle' : (align === 'right' ? 'end' : 'start'));
  t.textContent = text;
  ctx.appendChild(t);
}

function arrow(rc, x1, y1, x2, y2, color, opts) {
  opts = Object.assign({ stroke: color || INK, strokeWidth: 2.2, roughness: 1.6 }, opts || {});
  rc.line(x1, y1, x2, y2, opts);
  var angle = Math.atan2(y2 - y1, x2 - x1);
  var headLen = 12;
  var a1 = angle + Math.PI - 0.4, a2 = angle + Math.PI + 0.4;
  rc.line(x2, y2, x2 + headLen * Math.cos(a1), y2 + headLen * Math.sin(a1), opts);
  rc.line(x2, y2, x2 + headLen * Math.cos(a2), y2 + headLen * Math.sin(a2), opts);
}

function axes(rc, ctx, x0, y0, w, h, xlab, ylab) {
  arrow(rc, x0, y0, x0 + w, y0, INK);
  arrow(rc, x0, y0, x0, y0 - h, INK);
  if (xlab) label(ctx, x0 + w - 10, y0 + 24, xlab);
  if (ylab) label(ctx, x0 - 10, y0 - h - 8, ylab);
}

function sineWave(rc, x0, y0, width, amp, cycles, color) {
  var pts = [];
  var n = 120;
  for (var i = 0; i <= n; i++) {
    var x = x0 + (width * i) / n;
    var t = (i / n) * cycles * Math.PI * 2;
    var y = y0 - amp * Math.sin(t);
    pts.push([x, y]);
  }
  rc.curve(pts, { stroke: color || BLUE, strokeWidth: 2.4, roughness: 1.2 });
  return pts;
}

  var DIAGRAMS = {};

  /* ---------- Kinematics / Mechanics ---------- */

  DIAGRAMS.vectorTriangle = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var ox = 60, oy = s.h - 50;
    arrow(rc, ox, oy, ox + 180, oy - 40, BLUE);
    label(ctx, ox + 60, oy - 30, 'A', { color: BLUE, size: 20 });
    arrow(rc, ox + 180, oy - 40, ox + 300, oy - 130, ORANGE);
    label(ctx, ox + 230, oy - 110, 'B', { color: ORANGE, size: 20 });
    arrow(rc, ox, oy, ox + 300, oy - 130, GREEN);
    label(ctx, ox + 150, oy + 15, 'R = A + B', { color: GREEN, size: 20 });
  };

  DIAGRAMS.displacementTimeGraph = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 55, y0 = s.h - 40;
    axes(rc, ctx, x0, y0, s.w - 90, s.h - 80, 't', 'x');
    var pts = [[x0, y0], [x0 + 60, y0 - 40], [x0 + 140, y0 - 60], [x0 + 220, y0 - 130]];
    rc.curve(pts, { stroke: PURPLE, strokeWidth: 2.6, roughness: 1.3 });
    label(ctx, x0 + 40, y0 - 90, 'uniformly accelerated', { size: 15, color: PURPLE });
  };

  DIAGRAMS.projectileMotion = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 40, y0 = s.h - 40;
    rc.line(x0, y0, s.w - 20, y0, { stroke: INK, strokeWidth: 2, roughness: 1.4 });
    var pts = [];
    for (var i = 0; i <= 40; i++) {
      var t = i / 40;
      var x = x0 + t * (s.w - 90);
      var y = y0 - (4 * (s.h - 90)) * t * (1 - t);
      pts.push([x, y]);
    }
    rc.curve(pts, { stroke: ORANGE, strokeWidth: 2.6, roughness: 1.3 });
    arrow(rc, x0, y0, x0 + 60, y0 - 70, BLUE);
    label(ctx, x0 + 20, y0 - 75, 'u', { color: BLUE, size: 20 });
    label(ctx, x0 + 5, y0 + 20, 'θ', { color: INK, size: 16 });
    label(ctx, s.w / 2 - 30, 30, 'Parabolic path', { size: 16, color: ORANGE });
  };

  DIAGRAMS.forceDisplacementGraph = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 55, y0 = s.h - 40;
    axes(rc, ctx, x0, y0, s.w - 90, s.h - 80, 'x', 'F');
    var pts = [[x0, y0 - 20], [x0 + 60, y0 - 70], [x0 + 140, y0 - 55], [x0 + 210, y0 - 100]];
    rc.curve(pts, { stroke: BLUE, strokeWidth: 2.4, roughness: 1.3 });
    var poly = [[x0, y0]].concat(pts).concat([[x0 + 210, y0]]);
    rc.polygon(poly, { fill: '#fff29b', fillStyle: 'hachure', stroke: 'none' });
    label(ctx, x0 + 60, y0 - 20, 'W = area under curve', { size: 14, color: ORANGE });
  };

  DIAGRAMS.emSpectrumBar = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var bands = ['Radio', 'Micro', 'IR', 'Visible', 'UV', 'X-ray', 'Gamma'];
    var colors = [BLUE, TEAL, GREEN, ORANGE, PINK, PURPLE, INK];
    var bw = (s.w - 40) / bands.length;
    for (var i = 0; i < bands.length; i++) {
      rc.rectangle(20 + i * bw, s.h / 2 - 25, bw - 4, 50, { fill: colors[i], fillStyle: 'hachure', stroke: INK, roughness: 1.3 });
      label(ctx, 22 + i * bw, s.h / 2 + 45, bands[i], { size: 11 });
    }
    arrow(rc, 20, s.h / 2 - 45, s.w - 20, s.h / 2 - 45, INK);
    label(ctx, 20, s.h / 2 - 55, 'increasing frequency →', { size: 12 });
  };

  DIAGRAMS.inclinedPlaneForces = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var bx = 40, by = s.h - 30, tx = s.w - 40, ty = 40;
    rc.line(bx, by, tx, ty, { stroke: INK, strokeWidth: 2.4, roughness: 1.3 });
    rc.line(bx, by, tx, by, { stroke: INK, strokeWidth: 2.4, roughness: 1.3 });
    var midx = (bx + tx) / 2 - 20, midy = by - ((by - ty) * (midx - bx)) / (tx - bx) - 20;
    rc.rectangle(midx - 20, midy - 20, 40, 40, { fill: '#ffe98a', fillStyle: 'hachure', stroke: INK, roughness: 1.5 });
    arrow(rc, midx, midy, midx, midy + 70, PURPLE);
    label(ctx, midx + 6, midy + 60, 'mg', { color: PURPLE, size: 18 });
    arrow(rc, midx, midy, midx - 45, midy - 25, TEAL);
    label(ctx, midx - 80, midy - 20, 'N', { color: TEAL, size: 18 });
    label(ctx, bx + 15, by - 10, 'θ', { size: 16 });
  };

  DIAGRAMS.circularMotion = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, cy = s.h / 2, r = Math.min(s.w, s.h) / 2 - 30;
    rc.circle(cx, cy, r * 2, { stroke: INK, strokeWidth: 2, roughness: 1.4 });
    var ang = -Math.PI / 5;
    var px = cx + r * Math.cos(ang), py = cy + r * Math.sin(ang);
    rc.circle(px, py, 14, { fill: ORANGE, fillStyle: 'solid', stroke: INK });
    arrow(rc, px, py, cx, cy, PINK);
    label(ctx, (px + cx) / 2 - 10, (py + cy) / 2 - 8, 'Fc', { color: PINK, size: 18 });
    arrow(rc, px, py, px - 45 * Math.sin(ang), py + 45 * Math.cos(ang) * -1, BLUE);
    label(ctx, px - 30, py - 40, 'v', { color: BLUE, size: 18 });
  };

  DIAGRAMS.centreOfMass = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    rc.line(40, y, s.w - 40, y, { stroke: INK, strokeWidth: 4, roughness: 1.6 });
    rc.circle(120, y, 20, { fill: BLUE, fillStyle: 'solid' });
    label(ctx, 105, y - 30, 'm1', { color: BLUE });
    rc.circle(s.w - 120, y, 30, { fill: ORANGE, fillStyle: 'solid' });
    label(ctx, s.w - 145, y - 40, 'm2', { color: ORANGE });
    var comx = 120 + (s.w - 240) * (2 / 3);
    rc.line(comx, y - 50, comx, y + 50, { stroke: GREEN, strokeWidth: 2, roughness: 1.2, strokeLineDash: [6, 4] });
    label(ctx, comx - 15, y - 55, 'CM', { color: GREEN, size: 18 });
  };

  DIAGRAMS.torqueDiagram = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, cy = s.h / 2;
    rc.line(cx, cy, cx + 120, cy - 20, { stroke: INK, strokeWidth: 4, roughness: 1.5 });
    rc.circle(cx, cy, 10, { fill: INK, fillStyle: 'solid' });
    arrow(rc, cx + 120, cy - 20, cx + 120, cy - 100, PINK);
    label(ctx, cx + 130, cy - 90, 'F', { color: PINK, size: 20 });
    label(ctx, cx + 40, cy + 10, 'r', { size: 18 });
    label(ctx, cx - 30, cy + 40, 'τ = r × F', { color: PURPLE, size: 20 });
  };

  DIAGRAMS.gravitationOrbit = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, cy = s.h / 2;
    rc.circle(cx, cy, 34, { fill: ORANGE, fillStyle: 'solid' });
    label(ctx, cx - 10, cy + 5, 'M', { color: '#fff', size: 16, align: 'center' });
    rc.ellipse(cx, cy, s.w - 60, s.h - 60, { stroke: BLUE, strokeWidth: 2, roughness: 1.4 });
    var ex = cx + (s.w - 60) / 2, ey = cy;
    rc.circle(ex, ey, 14, { fill: TEAL, fillStyle: 'solid' });
    arrow(rc, ex, ey, ex - 5, ey - 40, PINK);
    label(ctx, ex + 8, ey - 25, 'v', { color: PINK, size: 16 });
  };

  /* ---------- Bulk matter / thermo ---------- */

  DIAGRAMS.stressStrainGraph = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 55, y0 = s.h - 40;
    axes(rc, ctx, x0, y0, s.w - 90, s.h - 80, 'strain', 'stress');
    var pts = [[x0, y0], [x0 + 90, y0 - 90], [x0 + 130, y0 - 115], [x0 + 170, y0 - 118], [x0 + 210, y0 - 60]];
    rc.curve(pts, { stroke: PINK, strokeWidth: 2.6, roughness: 1.3 });
    label(ctx, x0 + 85, y0 - 100, 'elastic limit', { size: 13, color: PINK });
  };

  DIAGRAMS.pascalLaw = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(30, s.h / 2, s.w - 60, s.h / 2 - 20, { stroke: INK, roughness: 1.4 });
    rc.rectangle(60, s.h / 2 - 60, 30, 60, { stroke: BLUE, fill: '#bfe6ff', fillStyle: 'hachure' });
    arrow(rc, 75, s.h / 2 - 65, 75, s.h / 2 - 90, BLUE);
    label(ctx, 45, s.h / 2 - 95, 'small F', { color: BLUE, size: 14 });
    rc.rectangle(s.w - 130, s.h / 2 - 100, 90, 100, { stroke: ORANGE, fill: '#ffd8a8', fillStyle: 'hachure' });
    arrow(rc, s.w - 90, s.h / 2 - 105, s.w - 90, s.h / 2 - 140, ORANGE);
    label(ctx, s.w - 150, s.h / 2 - 145, 'large F (out)', { color: ORANGE, size: 14 });
  };

  DIAGRAMS.bernoulliFlow = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    rc.line(20, y - 50, s.w * 0.4, y - 20, { stroke: INK, roughness: 1.3 });
    rc.line(20, y + 50, s.w * 0.4, y + 20, { stroke: INK, roughness: 1.3 });
    rc.line(s.w * 0.4, y - 20, s.w * 0.7, y - 45, { stroke: INK, roughness: 1.3 });
    rc.line(s.w * 0.4, y + 20, s.w * 0.7, y + 45, { stroke: INK, roughness: 1.3 });
    rc.line(s.w * 0.7, y - 45, s.w - 20, y - 45, { stroke: INK, roughness: 1.3 });
    rc.line(s.w * 0.7, y + 45, s.w - 20, y + 45, { stroke: INK, roughness: 1.3 });
    arrow(rc, 40, y, 90, y, TEAL);
    arrow(rc, s.w * 0.45, y, s.w * 0.45 + 55, y, PINK);
    label(ctx, 30, y - 60, 'wide, slow (v1)', { size: 13, color: TEAL });
    label(ctx, s.w * 0.42, y - 60, 'narrow, fast (v2)', { size: 13, color: PINK });
  };

  DIAGRAMS.thermalExpansion = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    rc.rectangle(40, y - 15, 120, 30, { stroke: BLUE, fill: '#bfe6ff', fillStyle: 'hachure', roughness: 1.4 });
    rc.rectangle(40, y + 40, 180, 30, { stroke: ORANGE, fill: '#ffd8a8', fillStyle: 'hachure', roughness: 1.4 });
    arrow(rc, 165, y, 200, y, BLUE);
    arrow(rc, 225, y + 55, 245, y + 55, ORANGE);
    label(ctx, 45, y - 25, 'cold, length L', { size: 13, color: BLUE });
    label(ctx, 45, y + 90, 'heated → length L + ΔL', { size: 13, color: ORANGE });
  };

  DIAGRAMS.heatEngineCycle = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 55, y0 = s.h - 40;
    axes(rc, ctx, x0, y0, s.w - 90, s.h - 80, 'V', 'P');
    var pts = [[x0 + 20, y0 - 30], [x0 + 160, y0 - 40], [x0 + 190, y0 - 140], [x0 + 60, y0 - 150], [x0 + 20, y0 - 30]];
    rc.curve(pts, { stroke: PURPLE, strokeWidth: 2.4, roughness: 1.3 });
    label(ctx, x0 + 70, y0 - 90, 'cyclic process', { size: 14, color: PURPLE });
  };

  DIAGRAMS.kineticTheoryBox = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(30, 20, s.w - 60, s.h - 40, { stroke: INK, roughness: 1.4 });
    var colors = [BLUE, ORANGE, TEAL, PINK, PURPLE, GREEN];
    for (var i = 0; i < colors.length; i++) {
      var x = 60 + Math.random() * (s.w - 120);
      var y = 50 + Math.random() * (s.h - 100);
      rc.circle(x, y, 10, { fill: colors[i], fillStyle: 'solid' });
      var dx = (Math.random() - 0.5) * 50, dy = (Math.random() - 0.5) * 50;
      rc.line(x, y, x + dx, y + dy, { stroke: colors[i], strokeWidth: 1.5, roughness: 1.2 });
    }
    label(ctx, s.w / 2 - 60, s.h - 10, 'molecules in random motion', { size: 13 });
  };

  /* ---------- Oscillations & Waves ---------- */

  DIAGRAMS.springMass = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 40, y = s.h / 2;
    var coils = 8, spacing = (s.w - 160) / coils;
    var pts = [[x0, y]];
    for (var i = 1; i <= coils; i++) {
      pts.push([x0 + i * spacing, y + (i % 2 === 0 ? 18 : -18)]);
    }
    rc.curve(pts, { stroke: INK, strokeWidth: 2, roughness: 1.5 });
    rc.rectangle(s.w - 120, y - 30, 60, 60, { fill: '#ffe98a', fillStyle: 'hachure', stroke: INK });
    label(ctx, s.w - 105, y + 6, 'm', { size: 20 });
    arrow(rc, s.w - 60, y, s.w - 20, y, PINK);
    label(ctx, s.w - 55, y - 10, 'x', { color: PINK });
  };

  DIAGRAMS.simplePendulum = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var px = s.w / 2 - 60, py = 25;
    rc.line(px, py, px, py + 10, { stroke: INK, roughness: 1.2 });
    rc.line(px - 30, py, px + 30, py, { stroke: INK, strokeWidth: 3, roughness: 1.4 });
    var bx = px + 70, by = s.h - 40;
    rc.line(px, py, bx, by, { stroke: INK, strokeWidth: 1.8, roughness: 1.4 });
    rc.circle(bx, by, 20, { fill: ORANGE, fillStyle: 'solid' });
    var arcPts = [];
    for (var a = -0.05; a <= 0.6; a += 0.05) {
      arcPts.push([px + 150 * Math.sin(a), py + 150 * Math.cos(a)]);
    }
    rc.curve(arcPts, { stroke: TEAL, strokeWidth: 1.4, roughness: 1.2, strokeLineDash: [4, 4] });
    label(ctx, px + 10, py + 40, 'θ', { size: 16 });
    label(ctx, bx + 25, by, 'bob (m)', { size: 14 });
  };

  DIAGRAMS.transverseWave = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    sineWave(s.rc, 30, s.h / 2, s.w - 60, s.h / 2 - 30, 2.5, BLUE);
    label(ctx, s.w / 2 - 30, s.h - 10, 'transverse wave (y vs x)', { size: 14, color: BLUE });
  };

  DIAGRAMS.longitudinalWave = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    for (var x = 30; x < s.w - 20; x += 6) {
      var density = 3 + 3 * (1 + Math.sin((x / (s.w - 60)) * Math.PI * 4));
      rc.line(x, y - 40, x, y + 40, { stroke: INK, strokeWidth: density / 4, roughness: 1 });
    }
    label(ctx, 30, 24, 'compressions & rarefactions', { size: 14 });
  };

  DIAGRAMS.standingWave = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    rc.line(20, y, s.w - 20, y, { stroke: INK, strokeWidth: 2, roughness: 1.2 });
    var pts1 = [], pts2 = [];
    for (var i = 0; i <= 60; i++) {
      var x = 20 + (i / 60) * (s.w - 40);
      var t = (i / 60) * Math.PI * 2;
      pts1.push([x, y - 40 * Math.sin(t)]);
      pts2.push([x, y + 40 * Math.sin(t)]);
    }
    rc.curve(pts1, { stroke: PINK, strokeWidth: 2, roughness: 1.2 });
    rc.curve(pts2, { stroke: PINK, strokeWidth: 2, roughness: 1.2, strokeLineDash: [5,4] });
    label(ctx, s.w / 2 - 20, y - 55, 'node/antinode pattern', { size: 13, color: PINK });
  };

  /* ---------- Electrostatics / Current ---------- */

  DIAGRAMS.pointChargeField = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, cy = s.h / 2;
    rc.circle(cx, cy, 22, { fill: PINK, fillStyle: 'solid' });
    label(ctx, cx - 6, cy + 6, '+', { color: '#fff', size: 18, align: 'center' });
    for (var a = 0; a < Math.PI * 2; a += Math.PI / 4) {
      arrow(rc, cx, cy, cx + 110 * Math.cos(a), cy + 110 * Math.sin(a), BLUE);
    }
  };

  DIAGRAMS.dipoleField = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cy = s.h / 2;
    rc.circle(s.w / 2 - 60, cy, 20, { fill: PINK, fillStyle: 'solid' });
    label(ctx, s.w / 2 - 66, cy + 5, '+', { color: '#fff', align: 'center' });
    rc.circle(s.w / 2 + 60, cy, 20, { fill: BLUE, fillStyle: 'solid' });
    label(ctx, s.w / 2 + 54, cy + 5, '−', { color: '#fff', align: 'center' });
    for (var i = -2; i <= 2; i++) {
      var pts = [];
      for (var t = 0; t <= 1; t += 0.05) {
        var x = (s.w / 2 - 60) + t * 120;
        var y = cy + i * 22 * Math.sin(t * Math.PI);
        pts.push([x, y]);
      }
      rc.curve(pts, { stroke: TEAL, strokeWidth: 1.4, roughness: 1.1 });
    }
  };

  DIAGRAMS.gaussSurface = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, cy = s.h / 2, r = Math.min(s.w, s.h) / 2 - 25;
    rc.circle(cx, cy, 14, { fill: ORANGE, fillStyle: 'solid' });
    rc.circle(cx, cy, r * 2, { stroke: TEAL, roughness: 1.4, strokeLineDash: [6, 5] });
    for (var a = 0; a < Math.PI * 2; a += Math.PI / 6) {
      arrow(rc, cx + (r-30) * Math.cos(a), cy + (r-30) * Math.sin(a), cx + (r+15)*Math.cos(a), cy+(r+15)*Math.sin(a), BLUE);
    }
    label(ctx, cx - 40, cy - r - 10, 'Gaussian surface', { size: 13, color: TEAL });
  };

  DIAGRAMS.parallelPlateCapacitor = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y1 = s.h / 2 - 50, y2 = s.h / 2 + 50;
    rc.line(60, y1, s.w - 60, y1, { stroke: PINK, strokeWidth: 4, roughness: 1.4 });
    rc.line(60, y2, s.w - 60, y2, { stroke: BLUE, strokeWidth: 4, roughness: 1.4 });
    for (var x = 90; x < s.w - 70; x += 30) {
      arrow(rc, x, y1 + 8, x, y2 - 8, INK);
    }
    label(ctx, 60, y1 - 12, '+ + + + + +', { color: PINK, size: 16 });
    label(ctx, 60, y2 + 26, '− − − − − −', { color: BLUE, size: 16 });
  };

  DIAGRAMS.simpleCircuit = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(50, 40, s.w - 100, s.h - 80, { stroke: INK, strokeWidth: 2, roughness: 1.4 });
    rc.line(s.w/2 - 25, 40, s.w/2 + 25, 40, { stroke: INK, strokeWidth: 5, roughness: 1.3 });
    label(ctx, s.w/2 - 10, 32, '+', { size: 14 });
    rc.rectangle(s.w/2 - 30, s.h - 80, 60, 15, { stroke: ORANGE, fill: '#ffd8a8', fillStyle: 'hachure', roughness: 1.3 });
    label(ctx, s.w/2 - 12, s.h - 30, 'R', { color: ORANGE, size: 18 });
    label(ctx, s.w/2 - 15, 22, 'cell', { size: 14 });
  };

  /* ---------- Magnetism / EMI / AC ---------- */

  DIAGRAMS.wireFieldLines = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2;
    rc.circle(cx, s.h / 2, 8, { fill: INK, fillStyle: 'solid' });
    label(ctx, cx - 4, s.h / 2 + 5, '•', { size: 22 });
    label(ctx, cx + 15, s.h / 2 - 40, 'I (out of page)', { size: 13 });
    for (var r = 30; r <= Math.min(s.w, s.h) / 2 - 20; r += 30) {
      rc.circle(cx, s.h / 2, r * 2, { stroke: BLUE, roughness: 1.5 });
    }
  };

  DIAGRAMS.solenoidField = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    for (var x = 50; x < s.w - 40; x += 26) {
      rc.ellipse(x, y, 20, 60, { stroke: INK, strokeWidth: 2, roughness: 1.3 });
    }
    for (var i = -1; i <= 1; i++) {
      arrow(rc, 30, y + i * 30, s.w - 20, y + i * 30, BLUE);
    }
    label(ctx, s.w / 2 - 40, y - 70, 'uniform field inside', { size: 13, color: BLUE });
  };

  DIAGRAMS.currentLoopTorque = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(s.w/2 - 60, s.h/2 - 50, 120, 100, { stroke: ORANGE, strokeWidth: 2.4, roughness: 1.4 });
    for (var y = s.h/2 - 60; y <= s.h/2 + 60; y += 15) {
      arrow(rc, 20, y, s.w - 20, y, BLUE, { strokeWidth: 1.4 });
    }
    label(ctx, s.w/2 - 15, s.h/2 + 5, 'I', { color: ORANGE, size: 18 });
    label(ctx, 25, s.h/2 - 70, 'B', { color: BLUE, size: 16 });
  };

  DIAGRAMS.emiMagnetCoil = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    for (var x = s.w/2; x < s.w - 30; x += 26) {
      rc.ellipse(x, y, 20, 60, { stroke: INK, strokeWidth: 2, roughness: 1.3 });
    }
    rc.rectangle(60, y - 15, 70, 30, { fill: PINK, fillStyle: 'hachure', stroke: INK, roughness: 1.4 });
    label(ctx, 80, y + 6, 'N   S', { size: 16 });
    arrow(rc, 140, y, 190, y, TEAL);
    label(ctx, 145, y - 15, 'moving', { size: 12, color: TEAL });
  };

  DIAGRAMS.acWaveform = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    sineWave(s.rc, 30, s.h / 2, (s.w - 60), s.h/2 - 30, 2, BLUE);
    var pts = [];
    for (var i = 0; i <= 120; i++) {
      var x = 30 + ((s.w - 60) * i) / 120;
      var t = (i / 120) * 2 * Math.PI * 2 + 0.8;
      pts.push([x, s.h/2 - (s.h/2 - 40) * Math.sin(t)]);
    }
    rc.curve(pts, { stroke: ORANGE, strokeWidth: 2, roughness: 1.2 });
    label(ctx, 35, 24, 'V (blue)  and  I (orange) — phase difference', { size: 13 });
  };

  DIAGRAMS.transformerCore = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(s.w/2 - 20, 30, 40, s.h - 60, { stroke: INK, strokeWidth: 3, roughness: 1.4 });
    for (var y = 40; y < s.h - 40; y += 22) {
      rc.ellipse(s.w/2 - 20, y, 20, 40, { stroke: BLUE, roughness: 1.2 });
    }
    for (var y2 = 40; y2 < s.h - 40; y2 += 22) {
      rc.ellipse(s.w/2 + 20, y2, 20, 40, { stroke: ORANGE, roughness: 1.2 });
    }
    label(ctx, s.w/2 - 70, 24, 'primary', { size: 13, color: BLUE });
    label(ctx, s.w/2 + 30, 24, 'secondary', { size: 13, color: ORANGE });
  };

  /* ---------- Optics ---------- */

  DIAGRAMS.convexLensRay = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, y = s.h / 2;
    rc.line(cx, 20, cx, s.h - 20, { stroke: TEAL, strokeWidth: 6, roughness: 1.3 });
    rc.line(20, y, s.w - 20, y, { stroke: INK, roughness: 1.2, strokeLineDash: [5,4] });
    var ox = 60, oy = y - 40;
    rc.line(ox, y, ox, oy, { stroke: PINK, strokeWidth: 2.4, roughness: 1.3 });
    arrow(rc, ox, oy + 10, ox, oy, PINK);
    var fx = cx + 90;
    arrow(rc, ox, oy, cx, y - 20, BLUE);
    arrow(rc, cx, y - 20, fx, y, BLUE);
    arrow(rc, ox, oy, cx, y, ORANGE);
    arrow(rc, cx, y, fx, y - ((y-oy)/(cx-ox))*(fx-cx)*-1, ORANGE);
    label(ctx, ox - 15, oy - 10, 'O', { size: 14 });
    label(ctx, fx + 5, y + 4, 'I', { size: 14 });
    label(ctx, cx - 10, 15, 'convex lens', { size: 13, color: TEAL });
  };

  DIAGRAMS.concaveMirrorRay = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var mx = s.w - 60, y = s.h / 2;
    var pts = [];
    for (var t = -1; t <= 1; t += 0.1) { pts.push([mx - 40 * (1 - t*t), y + t * (s.h/2 - 20)]); }
    rc.curve(pts, { stroke: INK, strokeWidth: 3, roughness: 1.3 });
    rc.line(20, y, mx, y, { stroke: INK, roughness: 1.1, strokeLineDash: [5,4] });
    var ox = 50, oy = y - 50;
    arrow(rc, ox, y, ox, oy, PINK);
    label(ctx, ox - 12, oy - 8, 'O', { size: 14 });
    arrow(rc, ox, oy, mx - 30, y - 10, BLUE);
    arrow(rc, mx - 30, y - 10, ox + 120, y + 40, BLUE);
    label(ctx, mx - 90, 20, 'concave mirror', { size: 13 });
  };

  DIAGRAMS.totalInternalReflection = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    rc.line(20, y, s.w - 20, y, { stroke: INK, strokeWidth: 2, roughness: 1.3 });
    arrow(rc, 40, y - 70, s.w/2 - 20, y, BLUE);
    arrow(rc, s.w/2 - 20, y, s.w - 40, y - 70, ORANGE);
    label(ctx, 30, y - 80, 'denser medium', { size: 12 });
    label(ctx, 30, y + 20, 'rarer medium', { size: 12 });
    label(ctx, s.w/2 - 15, y + 20, 'θc', { size: 14 });
  };

  DIAGRAMS.youngDoubleSlit = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    rc.line(60, 20, 60, s.h - 20, { stroke: INK, strokeWidth: 3, roughness: 1.3 });
    rc.line(60, y - 40, 60, y - 30, { stroke: '#fff', strokeWidth: 6 });
    rc.line(60, y + 30, 60, y + 40, { stroke: '#fff', strokeWidth: 6 });
    for (var i = -3; i <= 3; i++) {
      var pts = [];
      for (var t = 0; t <= 1; t += 0.05) {
        pts.push([60 + t * (s.w - 120), y + i * 15 + 20 * Math.sin(t * Math.PI * 3)]);
      }
      rc.curve(pts, { stroke: i % 2 === 0 ? BLUE : ORANGE, strokeWidth: 1.2, roughness: 1 });
    }
    rc.line(s.w - 40, 20, s.w - 40, s.h - 20, { stroke: TEAL, strokeWidth: 3, roughness: 1.3 });
    label(ctx, s.w - 90, 15, 'bright/dark fringes', { size: 12, color: TEAL });
  };

  /* ---------- Modern physics ---------- */

  DIAGRAMS.photoelectricEffect = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(s.w/2 - 20, 20, 40, s.h - 40, { fill: '#adb5bd', fillStyle: 'hachure', stroke: INK, roughness: 1.4 });
    for (var y = 40; y < s.h - 30; y += 30) {
      arrow(rc, 30, y, s.w/2 - 25, y, ORANGE);
    }
    label(ctx, 20, 24, 'light (photons)', { size: 13, color: ORANGE });
    arrow(rc, s.w/2 + 20, s.h/2, s.w - 30, s.h/2 - 50, BLUE);
    rc.circle(s.w - 35, s.h/2 - 55, 8, { fill: BLUE, fillStyle: 'solid' });
    label(ctx, s.w - 90, s.h/2 - 65, 'e⁻ ejected', { size: 12, color: BLUE });
  };

  DIAGRAMS.bohrModel = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var cx = s.w / 2, cy = s.h / 2;
    rc.circle(cx, cy, 16, { fill: ORANGE, fillStyle: 'solid' });
    label(ctx, cx - 12, cy + 30, 'nucleus (+)', { size: 12 });
    [40, 70, 100].forEach(function (r, i) {
      rc.circle(cx, cy, r * 2, { stroke: [BLUE, TEAL, PURPLE][i], roughness: 1.3 });
    });
    var a = -0.6;
    rc.circle(cx + 70 * Math.cos(a), cy + 70 * Math.sin(a), 7, { fill: PINK, fillStyle: 'solid' });
    label(ctx, cx - 40, cy - 110, 'n = 1, 2, 3 …', { size: 13 });
  };

  DIAGRAMS.nuclearFission = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h/2;
    rc.circle(90, y, 20, { fill: ORANGE, fillStyle: 'cross-hatch', stroke: INK });
    arrow(rc, 20, y, 65, y, BLUE);
    label(ctx, 15, y - 15, 'n', { size: 14 });
    label(ctx, 60, y - 30, 'U-235', { size: 12 });
    rc.circle(s.w - 130, y - 30, 26, { fill: TEAL, fillStyle: 'hachure', stroke: INK });
    rc.circle(s.w - 100, y + 30, 22, { fill: PINK, fillStyle: 'hachure', stroke: INK });
    arrow(rc, 115, y, s.w - 150, y - 30, GREEN);
    arrow(rc, 115, y, s.w - 120, y + 30, GREEN);
    label(ctx, s.w - 90, y - 55, '+ energy', { size: 13, color: GREEN });
  };

  DIAGRAMS.bindingEnergyCurve = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var x0 = 55, y0 = s.h - 40;
    axes(rc, ctx, x0, y0, s.w - 90, s.h - 80, 'mass number A', 'BE/A');
    var pts = [];
    for (var i = 0; i <= 40; i++) {
      var x = x0 + (i / 40) * (s.w - 100);
      var t = i / 40;
      var y = y0 - (s.h - 100) * (Math.sin(t * Math.PI * 0.9) * 0.85 + 0.05);
      pts.push([x, y]);
    }
    rc.curve(pts, { stroke: PURPLE, strokeWidth: 2.4, roughness: 1.2 });
    label(ctx, x0 + (s.w - 100) * 0.35, y0 - (s.h - 100) * 0.95, 'Fe-56 (peak)', { size: 12, color: PURPLE });
  };

  DIAGRAMS.pnJunction = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    rc.rectangle(40, s.h/2 - 50, (s.w - 80)/2, 100, { fill: '#bfe6ff', fillStyle: 'hachure', stroke: INK, roughness: 1.3 });
    rc.rectangle(40 + (s.w-80)/2, s.h/2 - 50, (s.w - 80)/2, 100, { fill: '#ffd8a8', fillStyle: 'hachure', stroke: INK, roughness: 1.3 });
    label(ctx, 60, s.h/2 - 60, 'p-type', { size: 14, color: BLUE });
    label(ctx, s.w/2 + 30, s.h/2 - 60, 'n-type', { size: 14, color: ORANGE });
    rc.line(s.w/2, s.h/2 - 50, s.w/2, s.h/2 + 50, { stroke: INK, strokeWidth: 2, roughness: 1.2, strokeLineDash: [4,4] });
    label(ctx, s.w/2 - 55, s.h/2 + 70, 'depletion region', { size: 12 });
  };

  DIAGRAMS.semiconductorBands = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var labels = ['Conductor', 'Semiconductor', 'Insulator'];
    var colors = [TEAL, ORANGE, PINK];
    for (var i = 0; i < 3; i++) {
      var x = 40 + i * (s.w - 80) / 3;
      var width = (s.w - 100) / 3;
      rc.rectangle(x, 20, width, 40, { fill: '#d0ebff', fillStyle: 'hachure', stroke: INK });
      var gap = [4, 30, 70][i];
      rc.rectangle(x, 70 + gap, width, 40, { fill: colors[i], fillStyle: 'hachure', stroke: INK });
      label(ctx, x, s.h - 10, labels[i], { size: 12, color: colors[i] });
    }
  };



  /* ---------- Class XII Textbook Ch.1 Electrostatics diagrams ---------- */

  DIAGRAMS.chargingByInduction = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    // charged rod (left)
    rc.rectangle(30, y - 60, 100, 24, { fill: PINK, fillStyle: 'hachure', stroke: INK, roughness: 1.4 });
    label(ctx, 45, y - 66, '+ + + + + +', { size: 13, color: PINK });
    label(ctx, 45, y - 100, 'charged rod', { size: 13, color: PINK });
    // neutral conductor (two touching spheres) on the right
    rc.circle(s.w - 160, y + 10, 70, { stroke: INK, strokeWidth: 2, roughness: 1.4 });
    rc.circle(s.w - 90, y + 10, 70, { stroke: INK, strokeWidth: 2, roughness: 1.4 });
    label(ctx, s.w - 195, y - 10, '- - -', { size: 16, color: BLUE });
    label(ctx, s.w - 115, y - 10, '+ + +', { size: 16, color: PINK });
    label(ctx, s.w - 170, y + 55, 'induced charges', { size: 12 });
    arrow(rc, 140, y - 45, s.w - 220, y - 10, INK, { strokeWidth: 1.4, roughness: 1.8 });
  };

  DIAGRAMS.coulombsLawForce = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var y = s.h / 2;
    var x1 = 100, x2 = s.w - 100;
    rc.circle(x1, y, 50, { fill: PINK, fillStyle: 'solid', stroke: INK });
    rc.circle(x2, y, 60, { fill: BLUE, fillStyle: 'solid', stroke: INK });
    label(ctx, x1 - 12, y + 6, 'Q1', { color: '#fff', size: 16, align: 'center' });
    label(ctx, x2 - 12, y + 6, 'Q2', { color: '#fff', size: 16, align: 'center' });
    arrow(rc, x1 + 60, y - 40, x1 + 130, y - 40, ORANGE);
    arrow(rc, x2 - 70, y - 40, x2 - 140, y - 40, ORANGE);
    label(ctx, s.w/2 - 10, y - 50, 'F', { color: ORANGE, size: 18, align: 'center' });
    label(ctx, s.w/2 - 8, y + 55, 'F', { color: ORANGE, size: 18, align: 'center' });
    arrow(rc, x1, y + 70, x2, y + 70, INK, { strokeWidth: 1.2 });
    label(ctx, s.w/2 - 6, y + 90, 'r', { size: 16 });
  };

  DIAGRAMS.chargeSuperposition = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var ax = s.w/2, ay = 40, bx = 60, by = s.h - 40, cx = s.w - 60, cy = s.h - 40;
    rc.line(ax, ay, bx, by, { stroke: INK, strokeWidth: 2, roughness: 1.3 });
    rc.line(ax, ay, cx, cy, { stroke: INK, strokeWidth: 2, roughness: 1.3 });
    rc.line(bx, by, cx, cy, { stroke: INK, strokeWidth: 2, roughness: 1.3 });
    rc.circle(ax, ay, 16, { fill: PINK, fillStyle: 'solid' });
    rc.circle(bx, by, 16, { fill: TEAL, fillStyle: 'solid' });
    rc.circle(cx, cy, 16, { fill: ORANGE, fillStyle: 'solid' });
    label(ctx, ax - 6, ay - 16, 'q', { size: 16, color: PINK });
    label(ctx, bx - 20, by + 22, 'q', { size: 16, color: TEAL });
    label(ctx, cx + 8, cy + 22, 'q', { size: 16, color: ORANGE });
    arrow(rc, ax, ay, ax - 25, ay + 60, PURPLE);
    arrow(rc, ax, ay, ax + 25, ay + 60, PURPLE);
    arrow(rc, ax, ay, ax, ay + 75, GREEN);
    label(ctx, ax + 8, ay + 90, 'F (resultant)', { size: 12, color: GREEN });
  };

  DIAGRAMS.chargeDensityTypes = function (id) {
    var s = setup(id); if (!s) return;
    var rc = s.rc, ctx = s.ctx;
    var third = s.w / 3;
    // linear
    rc.line(20, s.h/2, third - 30, s.h/2, { stroke: BLUE, strokeWidth: 4, roughness: 1.4 });
    label(ctx, 20, s.h/2 + 30, 'linear: λ = q/ℓ', { size: 12, color: BLUE });
    // surface
    rc.rectangle(third + 20, s.h/2 - 35, third - 55, 70, { fill: '#ffd8a8', fillStyle: 'hachure', stroke: ORANGE, roughness: 1.3 });
    label(ctx, third + 20, s.h/2 + 50, 'surface: σ = q/S', { size: 12, color: ORANGE });
    // volume
    rc.circle(2*third + 60, s.h/2, 70, { fill: '#c8f2c0', fillStyle: 'hachure', stroke: GREEN, roughness: 1.3 });
    label(ctx, 2*third + 20, s.h/2 + 55, 'volume: ρ = q/V', { size: 12, color: GREEN });
  };

function renderToSVG(name, w, h) {
  if (!DIAGRAMS[name]) throw new Error('Unknown diagram: ' + name);
  currentSize = { w: w, h: h };
  lastSvgEl = null;
  DIAGRAMS[name]('dummy');
  if (!lastSvgEl) throw new Error('Diagram did not render: ' + name);
  const serializer = new dom.window.XMLSerializer();
  return serializer.serializeToString(lastSvgEl);
}

// CLI: node render.js requests.json output.json
// requests.json = [{ "name": "vectorTriangle", "w": 480, "h": 240, "key": "vectorTriangle_480x240" }, ...]
const requestsPath = process.argv[2];
const outputPath = process.argv[3];
const requests = JSON.parse(fs.readFileSync(requestsPath, 'utf8'));
const output = {};
const errors = [];
for (const req of requests) {
  try {
    output[req.key] = renderToSVG(req.name, req.w, req.h);
  } catch (e) {
    errors.push(req.key + ': ' + e.message);
  }
}
fs.writeFileSync(outputPath, JSON.stringify(output));
if (errors.length) {
  console.error('ERRORS:\n' + errors.join('\n'));
  process.exit(1);
}
console.log('Rendered', Object.keys(output).length, 'diagrams OK');
