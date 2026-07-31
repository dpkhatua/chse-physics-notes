from helpers import p, lst, olist, formula, diagram, sticky, mnemonic, section, chapter, derivation, solved, mistake, tip, pyq

CLASS_LABEL = "Class XI"
CLASS_TITLE = "Class XI Physics — CHSE Odisha (+2 1st Year)"
CLASS_INTRO = ("Mechanics-heavy year: motion, force, energy, gravitation, properties of matter, "
               "heat and waves. Get your basics rock-solid here — Class XII builds on every bit of it. "
               "Every chapter below has derivations, solved numericals and an Exam Corner to push you past 90%.")

UNITS = []

def add_unit(roman, name, chapters):
    UNITS.append({"roman": roman, "name": name, "chapters": chapters})

# ----------------------------------------------------------------------
add_unit("I", "Physical World and Measurement", [
chapter("ch02", 2, "Units and Measurements",
  "Before you measure the universe, learn to measure a pencil.",
  ["SI units", "errors", "dimensions"],
  sections=[
    section("Physical Quantities & SI Units", [
      p("A <b>physical quantity</b> is anything that can be measured — length, mass, time, temperature, current... "
        "Every measurement = <b>a number + a unit</b>. Say '10' without a unit and nobody knows if you mean 10 seconds or 10 kilometres!"),
      p("The world agreed on one common system: the <b>SI system (Système International)</b> with 7 base units:"),
      lst([
        "<b>metre (m)</b> — length", "<b>kilogram (kg)</b> — mass", "<b>second (s)</b> — time",
        "<b>ampere (A)</b> — electric current", "<b>kelvin (K)</b> — temperature",
        "<b>mole (mol)</b> — amount of substance", "<b>candela (cd)</b> — luminous intensity",
      ]),
      p("Every other unit (speed, force, energy...) is a <b>derived unit</b> — built by multiplying/dividing base units. "
        "E.g. speed = m/s, force = kg·m/s² (this combination even gets its own name: <mark class='hl-yellow'>newton</mark>)."),
      mistake("Writing an answer without units loses marks even if the number is correct — CHSE evaluators are strict about this in numerical answers."),
    ]),
    section("Significant Figures & Errors", [
      p("No measurement is perfectly exact — every instrument has a limit. <b>Significant figures</b> tell you how precisely a "
        "number is known."),
      olist([
        "All non-zero digits are significant. (247 → 3 sig. figs.)",
        "Zeros between non-zero digits are significant. (2007 → 4 sig. figs.)",
        "Leading zeros are never significant. (0.0025 → 2 sig. figs.)",
        "Trailing zeros after a decimal point ARE significant. (2.500 → 4 sig. figs.)",
      ]),
      p("<b>Errors</b> in measurement are of two broad kinds: <b>systematic errors</b> (same mistake every time — bad "
        "calibration, zero error) which can be corrected, and <b>random errors</b> (irregular, unpredictable) which we reduce "
        "by taking the mean of many readings."),
      formula("Combining errors", [
        "Addition/Subtraction → absolute errors <b>add</b>: Δ(A ± B) = ΔA + ΔB",
        "Multiplication/Division → relative errors <b>add</b>: Δ(AB)/AB = ΔA/A + ΔB/B",
      ]),
      solved(
        "The radius of a sphere is measured as (2.1 ± 0.02) cm. Find the percentage error in its volume.",
        [
          "Volume V = (4/3)πr³, so relative error in V = 3 × (relative error in r).",
          "Relative error in r = Δr/r = 0.02/2.1 = 0.00952",
          "Percentage error in V = 3 × 0.00952 × 100 = 2.86%",
        ],
        "≈ 2.86%",
      ),
    ]),
    section("Dimensions & Dimensional Analysis", [
      p("The <b>dimension</b> of a quantity shows which base quantities it's built from, written in square brackets. "
        "Force = mass × acceleration → [M L T⁻²]."),
      formula("Dimensional formulae to remember", [
        "Velocity → [M⁰L¹T⁻¹]", "Acceleration → [M⁰L¹T⁻²]", "Force → [M¹L¹T⁻²]",
        "Work / Energy → [M¹L²T⁻²]", "Power → [M¹L²T⁻³]", "Pressure → [M¹L⁻¹T⁻²]",
      ]),
      p("<b>Uses of dimensional analysis:</b> (1) check if an equation is correct — dimensions on both sides must match "
        "(principle of homogeneity); (2) convert units from one system to another; (3) derive a relation between quantities."),
      solved(
        "Check by dimensional analysis whether s = ut + ½at² is correct.",
        [
          "[s] = [L]",
          "[ut] = [LT⁻¹][T] = [L]",
          "[at²] = [LT⁻²][T²] = [L]",
          "All three terms have dimension [L] — equation is dimensionally consistent.",
        ],
        "Dimensionally correct (LHS = RHS = [M⁰L¹T⁰])",
      ),
      sticky("Limitation", "Dimensional analysis can't find dimensionless constants (like 1/2 in ½mv²), and it fails for "
             "equations with trigonometric, exponential or logarithmic terms.", "pink"),
      tip("In the exam, always write the dimensional formula in the boxed [M L T] form — examiners award marks specifically for correct notation."),
    ]),
  ],
  recap=[
    "Measurement = number + unit; SI has 7 base units.",
    "Significant figures show precision; trailing zeros after a decimal point count.",
    "Systematic errors can be corrected; random errors are reduced by averaging.",
    "Dimensional analysis checks equations and derives relations — but misses numeric constants.",
  ],
  exam_corner=[
    pyq(1, "Name the SI unit of luminous intensity."),
    pyq(1, "How many significant figures are there in 0.00580?"),
    pyq(2, "Distinguish between systematic and random errors, with one example each."),
    pyq(2, "Write the dimensional formula of (a) power (b) pressure."),
    pyq(3, "The percentage errors in measurement of mass and speed are 2% and 3% respectively. Find the maximum percentage error in kinetic energy (KE = ½mv²)."),
    pyq(5, "What is dimensional analysis? State its three main uses and one limitation, with an example for each use."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("II", "Kinematics", [
chapter("ch03", 3, "Motion in a Straight Line",
  "The simplest motion there is — but where every graph trick begins.",
  ["1D motion", "graphs", "kinematics equations"],
  sections=[
    section("Describing Motion", [
      p("<b>Distance</b> is the total path length covered (always positive, scalar). <b>Displacement</b> is the shortest "
        "straight-line change in position, with direction (vector). A student walking 5 m east then 5 m west covers a "
        "<b>distance</b> of 10 m but a <b>displacement</b> of zero!"),
      p("<b>Average speed</b> = total distance / total time. <b>Average velocity</b> = displacement / time. "
        "<b>Instantaneous velocity</b> is the velocity at one instant: v = dx/dt (the slope of the position-time graph at that point)."),
      mistake("Students often use 'speed' and 'velocity' interchangeably in derivations — CHSE examiners specifically check whether you used the vector (velocity) correctly in problems involving direction/sign."),
    ]),
    section("Graphs of Motion", [
      diagram("displacementTimeGraph", "Position–time graph for uniformly accelerated motion — slope keeps increasing.", 480, 260),
      p("On a <b>position–time graph</b>, the slope gives velocity. A straight line = uniform velocity; a curving line = "
        "changing velocity (acceleration). On a <b>velocity–time graph</b>, the slope gives acceleration, and the "
        "<mark class='hl-yellow'>area under the curve gives displacement</mark>."),
    ]),
    section("Equations of Uniformly Accelerated Motion", [
      derivation("v = u + at (from a v-t graph)",
        "A body has initial velocity u at t = 0, and moves with constant acceleration a. Let its velocity be v at time t.",
        [
          "By definition, acceleration a = (change in velocity)/(time taken) = (v − u)/t",
          "Rearranging: v − u = at",
        ],
        "v = u + at"),
      derivation("s = ut + ½at² (from a v-t graph)",
        "Same v-t graph: a straight line starting at u, rising to v after time t.",
        [
          "Displacement = area under the v-t graph = area of rectangle (u × t) + area of triangle (½ × t × (v−u))",
          "Since (v−u) = at (from the first equation), triangle's area = ½ × t × at = ½at²",
          "Total displacement s = ut + ½at²",
        ],
        "s = ut + ½at²"),
      formula("The three kinematics equations (constant a)", [
        "v = u + at",
        "s = ut + ½at²",
        "v² = u² + 2as",
      ]),
      solved(
        "A car accelerates uniformly from 18 km/h to 36 km/h in 5 s. Find (a) the acceleration (b) distance covered.",
        [
          "Convert: u = 18 km/h = 5 m/s, v = 36 km/h = 10 m/s, t = 5 s",
          "(a) a = (v−u)/t = (10−5)/5 = 1 m/s²",
          "(b) s = ut + ½at² = (5×5) + ½(1)(5²) = 25 + 12.5 = 37.5 m",
        ],
        "a = 1 m/s², s = 37.5 m",
      ),
      mnemonic("'Uvast' — <b>u</b>, <b>v</b>, <b>a</b>, <b>s</b>, <b>t</b> — the five characters in every kinematics problem. "
               "Write down what's given, what's asked, then pick the equation missing the unwanted letter."),
    ]),
  ],
  recap=[
    "Distance ≠ displacement; speed ≠ velocity — one has direction, the other doesn't.",
    "Slope of x-t graph = velocity; slope of v-t graph = acceleration; area under v-t graph = displacement.",
    "v = u+at, s = ut+½at², v² = u²+2as — valid only for constant acceleration.",
  ],
  exam_corner=[
    pyq(1, "Can a body have zero velocity and non-zero acceleration at the same instant? Give an example."),
    pyq(1, "What does the slope of a position-time graph represent?"),
    pyq(2, "Derive v = u + at using a velocity-time graph."),
    pyq(2, "A ball is thrown vertically upward with speed 20 m/s. Find the time taken to reach the highest point (g = 10 m/s²)."),
    pyq(3, "Derive s = ut + ½at² using a velocity-time graph, with a clear labelled graph."),
    pyq(5, "Derive all three equations of motion (v=u+at, s=ut+½at², v²=u²+2as) using calculus/graphical method, and solve: a train starting from rest accelerates at 2 m/s² for 10 s, then moves at constant velocity for 20 s. Find total distance covered."),
  ]),

chapter("ch04", 4, "Motion in a Plane",
  "Motion gets a second dimension — enter vectors, projectiles and circles.",
  ["vectors", "projectile motion", "circular motion"],
  sections=[
    section("Scalars, Vectors & Vector Addition", [
      p("A <b>scalar</b> has only magnitude (mass, speed, temperature). A <b>vector</b> has magnitude AND direction "
        "(displacement, velocity, force). Vectors are added using the <b>triangle law</b> or <b>parallelogram law</b> — "
        "you can't just add magnitudes unless they're in the same direction!"),
      diagram("vectorTriangle", "Triangle law: place vector B at the tip of A, the resultant R runs from A's tail to B's tip.", 480, 240),
      formula("Resolving a vector into components", [
        "Ax = A cos θ   (x-component)",
        "Ay = A sin θ   (y-component)",
        "A = √(Ax² + Ay²) ,  θ = tan⁻¹(Ay/Ax)",
      ]),
      solved(
        "Two forces of 6 N and 8 N act at right angles to each other. Find the magnitude and direction of the resultant.",
        [
          "Since they're perpendicular, R = √(6² + 8²) = √(36+64) = √100 = 10 N",
          "Direction: tanθ = 8/6 = 1.33 → θ = tan⁻¹(1.33) ≈ 53° from the 6 N force",
        ],
        "R = 10 N, at 53° from the 6 N force",
      ),
    ]),
    section("Projectile Motion", [
      p("Throw something at an angle and it follows a <b>parabolic path</b> — this is projectile motion. The trick: "
        "split it into two <i>independent</i> motions — horizontal (constant velocity, no acceleration) and vertical "
        "(uniform acceleration = −g)."),
      diagram("projectileMotion", "Horizontal velocity stays constant; gravity curves the path into a parabola.", 480, 240),
      derivation("Range of a projectile", "A body is projected with speed u at angle θ to the horizontal.",
        [
          "Time of flight T = 2u sinθ / g (time for vertical displacement to return to zero)",
          "Horizontal range R = horizontal velocity × time of flight = (u cosθ)(2u sinθ/g)",
          "R = (2u² sinθ cosθ)/g = u² sin2θ / g   (using 2sinθcosθ = sin2θ)",
        ],
        "R = u² sin2θ / g — maximum when θ = 45° (sin2θ = 1)"),
      formula("Key projectile results (launch angle θ, speed u)", [
        "Time of flight: T = 2u sinθ / g",
        "Maximum height: H = u² sin²θ / 2g",
        "Range: R = u² sin2θ / g",
        "Range is maximum when θ = 45°",
      ]),
      solved(
        "A ball is projected at 30° with the horizontal at 20 m/s. Find the range and maximum height (g = 10 m/s²).",
        [
          "R = u²sin2θ/g = (20²)(sin60°)/10 = (400)(0.866)/10 = 34.6 m",
          "H = u²sin²θ/2g = (400)(0.25)/20 = 5 m",
        ],
        "R ≈ 34.6 m, H = 5 m",
      ),
      mistake("Forgetting that horizontal velocity (u cosθ) stays CONSTANT throughout the flight — many students wrongly apply g to the horizontal component too."),
    ]),
    section("Uniform Circular Motion", [
      p("Moving in a circle at <b>constant speed</b> still means accelerating — because direction keeps changing! "
        "This acceleration points toward the centre: <b>centripetal acceleration</b>."),
      derivation("Centripetal acceleration", "A particle moves in a circle of radius r with constant speed v.",
        [
          "In a small time Δt, velocity direction changes by a small angle Δθ, where Δθ = Δs/r = vΔt/r.",
          "The change in velocity vector Δv has magnitude vΔθ (for small angles), directed toward the centre.",
          "Acceleration a = Δv/Δt = v(Δθ)/Δt = v × (v/r) = v²/r",
        ],
        "a = v²/r, directed toward the centre"),
      formula("Circular motion", [
        "Centripetal acceleration: a = v²/r = ω²r",
        "ω (angular velocity) = v/r = 2π/T",
      ]),
      sticky("Common confusion", "Centripetal force is NOT a new/separate force — it's just the name for whichever real "
             "force (tension, gravity, friction, normal force) happens to point toward the centre.", "blue"),
    ]),
  ],
  recap=[
    "Vectors add tip-to-tail (triangle law); resolve into perpendicular components to solve problems easily.",
    "Projectile motion = constant-velocity horizontal + uniformly accelerated vertical motion, independently.",
    "Range is max at 45°; time of flight depends only on the vertical component of velocity.",
    "Uniform circular motion has constant speed but changing velocity → centripetal acceleration v²/r toward the centre.",
  ],
  exam_corner=[
    pyq(1, "What is the angle between velocity and acceleration at the topmost point of a projectile's path?"),
    pyq(1, "Define angular velocity and give its SI unit."),
    pyq(2, "State the parallelogram law of vector addition and write the formula for the magnitude of the resultant."),
    pyq(2, "A stone tied to a string of length 1 m is whirled in a circle at 2 revolutions per second. Find its centripetal acceleration."),
    pyq(3, "Derive the expression for maximum height and time of flight of a projectile projected at angle θ with speed u."),
    pyq(5, "Derive the expression for the range of a projectile and show that the range is maximum at 45°. A cricket ball is hit at 25 m/s at 37° above horizontal — find its range, time of flight and maximum height (g=10 m/s², sin37°=0.6, cos37°=0.8)."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("III", "Laws of Motion", [
chapter("ch05", 5, "Laws of Motion",
  "Newton's three rules that quietly run the entire universe.",
  ["Newton's laws", "friction", "circular dynamics"],
  sections=[
    section("Newton's Three Laws", [
      olist([
        "<b>First law (Inertia):</b> A body stays at rest or in uniform motion unless acted on by a net external force. "
        "Force is not needed to keep something moving — only to change its motion.",
        "<b>Second law:</b> F = ma (rate of change of momentum ∝ applied force, in the direction of the force).",
        "<b>Third law:</b> For every action there is an equal and opposite reaction — forces always come in pairs acting "
        "on <i>different</i> bodies.",
      ]),
      formula("Newton's second law (general form)", ["F = dp/dt", "For constant mass: F = ma"]),
      p("<b>Impulse</b> = change in momentum = F × Δt (useful when force acts for a very short time, e.g. a bat hitting a ball)."),
      p("<b>Conservation of linear momentum:</b> if no external force acts on a system, total momentum stays constant — "
        "this is why rockets, recoiling guns and collisions can all be analysed without knowing the internal forces."),
      solved(
        "A bat exerts an average force of 200 N on a ball for 0.01 s. Find the impulse and the change in momentum.",
        [
          "Impulse = F × Δt = 200 × 0.01 = 2 N·s",
          "By the impulse-momentum theorem, change in momentum = impulse",
        ],
        "Impulse = change in momentum = 2 kg·m/s",
      ),
      mistake("Newton's third law pairs act on DIFFERENT bodies and can never cancel each other in an FBD of a single body — a very common conceptual error in CHSE answers."),
    ]),
    section("Friction", [
      p("Friction opposes relative sliding between two surfaces. <b>Static friction</b> acts before motion starts and adjusts "
        "itself up to a maximum (limiting friction); <b>kinetic friction</b> acts once sliding begins and is roughly constant."),
      formula("Friction", ["f ≤ μsN (static)", "f = μkN (kinetic)", "μk < μs — always easier to keep something moving than to start it"]),
      solved(
        "A block of mass 5 kg rests on a horizontal surface (μs = 0.4). Find the minimum horizontal force needed to just move it (g = 10 m/s²).",
        [
          "Normal reaction N = mg = 5 × 10 = 50 N",
          "Limiting friction fs(max) = μsN = 0.4 × 50 = 20 N",
          "To just start moving, applied force must equal limiting friction",
        ],
        "20 N",
      ),
    ]),
    section("Circular Dynamics — Banking of Roads", [
      diagram("inclinedPlaneForces", "Forces on a block on an inclined surface: weight mg splits into components along and perpendicular to the incline.", 480, 260),
      p("On a <b>banked road</b>, the horizontal component of the normal reaction supplies part (or all) of the required "
        "centripetal force, letting vehicles turn safely even without relying only on friction."),
      derivation("Maximum safe speed on a banked road (with friction)", "A vehicle of mass m moves on a road banked at angle θ, radius r, coefficient of friction μ.",
        [
          "Resolve N and friction f along horizontal (centripetal) and vertical directions.",
          "Vertical equilibrium: N cosθ = mg + f sinθ",
          "Horizontal (centripetal): N sinθ + f cosθ = mv²/r",
          "Using f = μN and solving the two equations simultaneously for v²",
        ],
        "v²max = rg(tanθ + μ)/(1 − μ tanθ)"),
      formula("Maximum safe speed on a banked curve (angle θ, friction μ)", ["v²max = rg(tanθ + μ)/(1 − μ tanθ)"]),
    ]),
  ],
  recap=[
    "1st law → inertia; 2nd law → F=ma; 3rd law → action-reaction pairs on different bodies.",
    "Linear momentum is conserved when no external force acts — key for collisions.",
    "Static friction adjusts up to μsN; kinetic friction is roughly constant at μkN.",
    "Banking of roads uses the normal reaction's horizontal component to help provide centripetal force.",
  ],
  exam_corner=[
    pyq(1, "State Newton's first law of motion. What is another name for this law?"),
    pyq(1, "Why is it easier to keep a block sliding than to start it sliding?"),
    pyq(2, "State the law of conservation of linear momentum and give one everyday example."),
    pyq(2, "A 2 kg body moving at 3 m/s collides with a wall and bounces back at 2 m/s. Find the change in momentum."),
    pyq(3, "Derive the expression for the maximum speed of a vehicle on a banked road (ignoring friction)."),
    pyq(5, "State and explain Newton's three laws of motion with one example each. A block of mass 10 kg is pulled by a horizontal force of 40 N on a surface with μk = 0.2. Find its acceleration (g = 10 m/s²)."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("IV", "Work, Energy and Power", [
chapter("ch06", 6, "Work, Energy and Power",
  "Nothing gets done in physics without work — literally.",
  ["work-energy theorem", "conservation of energy", "collisions"],
  sections=[
    section("Work and the Work–Energy Theorem", [
      p("Work is done only when a force causes displacement in its own direction: <b>W = F·s·cosθ</b>. Carrying a heavy "
        "bag while walking horizontally? Physics says the vertical force (your muscles) does <b>zero</b> work on the bag "
        "since displacement is horizontal!"),
      diagram("forceDisplacementGraph", "For a variable force, work done = area under the Force–displacement graph.", 480, 240),
      derivation("Work–energy theorem", "A constant force F acts on a mass m, accelerating it from u to v over displacement s.",
        [
          "From v² = u² + 2as: a = (v²−u²)/2s",
          "Work done W = F·s = (ma)·s = m × (v²−u²)/2s × s = ½m(v²−u²)",
          "W = ½mv² − ½mu² = final KE − initial KE",
        ],
        "Wnet = ΔKE (work-energy theorem)"),
      formula("Work–Energy theorem", ["Wnet = ΔKE = ½mv² − ½mu²", "Kinetic Energy: KE = ½mv²"]),
      solved(
        "A 2 kg block moving at 3 m/s is acted on by a force that brings it to rest over 1.5 m. Find the average force (assume it opposes motion).",
        [
          "Initial KE = ½(2)(3²) = 9 J, Final KE = 0",
          "By work-energy theorem, work done by force = ΔKE = 0 − 9 = −9 J",
          "W = −F×s (force opposes motion) → −9 = −F×1.5 → F = 6 N",
        ],
        "F = 6 N",
      ),
    ]),
    section("Potential Energy & Conservative Forces", [
      p("A force is <b>conservative</b> if the work it does depends only on start and end points, not the path taken "
        "(gravity, spring force). For such forces we can define a <b>potential energy</b>. Friction is <b>non-conservative</b> "
        "— it wastes energy as heat and depends on the path."),
      formula("Common potential energies", ["Gravitational PE: U = mgh", "Spring PE: U = ½kx²"]),
      mnemonic("Total mechanical energy (KE + PE) is conserved <i>only</i> when non-conservative forces (friction, air "
               "resistance) do no work."),
    ]),
    section("Collisions", [
      p("In <b>elastic collisions</b>, both momentum and kinetic energy are conserved (like ideal billiard balls). In "
        "<b>inelastic collisions</b>, momentum is conserved but kinetic energy is not — some energy converts to heat/sound/"
        "deformation. A <b>perfectly inelastic collision</b> is the extreme case: the bodies stick together afterward."),
      formula("Power", ["Power = Work done / time = W/t", "Instantaneous power: P = F·v"]),
      solved(
        "A ball of mass 1 kg moving at 4 m/s collides head-on with a stationary ball of mass 3 kg and they stick together. Find their common velocity.",
        [
          "By conservation of momentum: m1u1 + m2u2 = (m1+m2)v",
          "(1)(4) + (3)(0) = (1+3)v",
          "4 = 4v → v = 1 m/s",
        ],
        "v = 1 m/s (in the direction of the first ball's initial motion)",
      ),
      mistake("In inelastic collisions, students often wrongly try to conserve kinetic energy too — only momentum is conserved unless the collision is explicitly stated as elastic."),
    ]),
  ],
  recap=[
    "W = F s cosθ; only the force-component along displacement does work.",
    "Work–energy theorem: net work done = change in kinetic energy.",
    "Conservative forces (gravity, spring) → definable PE; friction is non-conservative.",
    "Elastic collisions conserve both momentum & KE; inelastic collisions conserve only momentum.",
  ],
  exam_corner=[
    pyq(1, "When is the work done by a force zero even though displacement is non-zero?"),
    pyq(1, "Define power and give its SI unit."),
    pyq(2, "Distinguish between elastic and inelastic collisions."),
    pyq(2, "A pump lifts 200 kg of water through a height of 6 m in 10 s. Find the power of the pump (g=10 m/s²)."),
    pyq(3, "Derive the work-energy theorem for a constant force."),
    pyq(5, "State the law of conservation of energy. Derive expressions for the velocities of two bodies after a 1-D elastic collision. A 4 kg mass moving at 5 m/s collides elastically with a stationary 4 kg mass — find their velocities after collision."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("V", "Motion of System of Particles and Rigid Body", [
chapter("ch07", 7, "System of Particles and Rotational Motion",
  "When an object isn't a single dot anymore — meet the centre of mass and torque.",
  ["centre of mass", "torque", "moment of inertia"],
  sections=[
    section("Centre of Mass", [
      diagram("centreOfMass", "Centre of mass of a two-body system lies closer to the heavier mass.", 480, 200),
      p("The <b>centre of mass (CM)</b> is the point where the entire mass of a system can be imagined concentrated for "
        "analysing translational motion. For an isolated system, the CM moves as if all external forces act at that single point."),
      formula("Centre of mass of a two-particle system", ["xcm = (m1x1 + m2x2) / (m1 + m2)"]),
      solved(
        "Two masses 2 kg and 4 kg are placed at x = 0 and x = 6 m. Find the position of their centre of mass.",
        [
          "xcm = (m1x1 + m2x2)/(m1+m2) = (2×0 + 4×6)/(2+4) = 24/6 = 4 m",
        ],
        "xcm = 4 m from the 2 kg mass",
      ),
    ]),
    section("Torque & Angular Momentum", [
      diagram("torqueDiagram", "Torque τ = r × F — turning effect depends on both the force and its distance from the pivot.", 460, 240),
      formula("Rotational quantities", [
        "Torque: τ = r × F  (τ = rF sinθ)",
        "Angular momentum: L = r × p = Iω",
        "Newton's 2nd law for rotation: τ = dL/dt",
      ]),
      p("Just like linear momentum, <b>angular momentum is conserved</b> when no external torque acts — this is why a "
        "spinning ice-skater speeds up when she pulls her arms in (reducing I increases ω to keep L constant)."),
      solved(
        "A force of 10 N is applied perpendicular to a spanner at a distance of 0.2 m from the bolt. Find the torque.",
        ["τ = rF sinθ, here θ = 90° so sinθ = 1", "τ = 0.2 × 10 × 1 = 2 N·m"],
        "τ = 2 N·m",
      ),
    ]),
    section("Moment of Inertia", [
      p("<b>Moment of inertia (I)</b> is the rotational equivalent of mass — it measures resistance to change in rotational "
        "motion, and depends on how mass is distributed relative to the axis."),
      formula("Moment of inertia & radius of gyration", ["I = Σmr² = MK²", "K = radius of gyration"]),
      sticky("Compare: Linear vs Rotational", "Mass ↔ Moment of Inertia (I) &middot; Velocity ↔ Angular velocity (ω) &middot; "
             "Force ↔ Torque (τ) &middot; Momentum ↔ Angular momentum (L)", "blue"),
      mistake("Moment of inertia is NOT a fixed property of a body like mass — it changes with the choice of axis. Always state the axis when quoting I."),
    ]),
  ],
  recap=[
    "Centre of mass moves as if all mass and all external force act there.",
    "Torque τ = r × F is the rotational analogue of force; τ = Iα.",
    "Angular momentum L = Iω is conserved when net external torque is zero.",
    "Moment of inertia depends on mass distribution, not just total mass.",
  ],
  exam_corner=[
    pyq(1, "Define radius of gyration."),
    pyq(1, "State the principle of conservation of angular momentum."),
    pyq(2, "Two point masses 1 kg and 3 kg are 4 m apart. Find the centre of mass from the 1 kg mass."),
    pyq(2, "Why does a figure skater spin faster when she pulls her arms inward?"),
    pyq(3, "Define torque and angular momentum, and derive the relation τ = dL/dt."),
    pyq(5, "Define moment of inertia and radius of gyration. Derive the centre of mass formula for a two-particle system, and find the CM of masses 3 kg, 5 kg placed at (0,0) and (4,0) m."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("VI", "Gravitation", [
chapter("ch08", 8, "Gravitation",
  "The force that keeps your feet on the ground and planets in orbit — same law, one equation.",
  ["Kepler's laws", "universal gravitation", "satellites"],
  sections=[
    section("Kepler's Laws of Planetary Motion", [
      olist([
        "<b>Law of orbits:</b> every planet moves in an elliptical orbit with the Sun at one focus.",
        "<b>Law of areas:</b> the line joining planet to Sun sweeps equal areas in equal times (planet moves faster near the Sun).",
        "<b>Law of periods:</b> T² ∝ r³ (square of time period ∝ cube of the semi-major axis).",
      ]),
    ]),
    section("Universal Law of Gravitation", [
      diagram("gravitationOrbit", "A satellite in circular orbit — gravity itself supplies the centripetal force.", 460, 260),
      formula("Newton's law of gravitation", ["F = G m1m2 / r²", "G = 6.674 × 10⁻¹¹ N m² kg⁻²"]),
      p("This single equation explains why apples fall AND why the Moon stays in orbit — Newton's big insight was "
        "that it's the <i>same</i> force at every scale."),
    ]),
    section("g, Potential Energy, Escape Speed", [
      formula("Variation of g", [
        "With altitude h: g' = g(1 − 2h/R)  (h ≪ R)",
        "With depth d: g' = g(1 − d/R)",
      ]),
      derivation("Escape speed", "Minimum speed ve needed for a body of mass m to just escape Earth's gravitational field from the surface (radius R, mass M), i.e. total energy = 0.",
        [
          "Total energy at surface = KE + PE = ½mve² + (−GMm/R)",
          "For the body to just escape (reach infinity with zero velocity), total energy = 0",
          "½mve² − GMm/R = 0  →  ve² = 2GM/R",
        ],
        "ve = √(2GM/R)"),
      formula("Energy & speeds", [
        "Gravitational PE: U = −GMm/r",
        "Escape speed: ve = √(2GM/R)",
        "Orbital speed (near surface): vo = √(GM/R) = ve/√2",
      ]),
      solved(
        "Find the escape speed from Earth's surface. (G=6.67×10⁻¹¹, M=6×10²⁴ kg, R=6.4×10⁶ m)",
        [
          "ve = √(2GM/R) = √(2 × 6.67×10⁻¹¹ × 6×10²⁴ / 6.4×10⁶)",
          "= √(8.0×10¹⁴/6.4×10⁶) = √(1.25×10⁸)",
        ],
        "ve ≈ 11.2 km/s",
      ),
      mnemonic("g decreases whether you go <b>up</b> (altitude) or <b>down</b> (depth) from Earth's surface — it's "
               "maximum only right at the surface."),
    ]),
  ],
  recap=[
    "Kepler: elliptical orbits, equal areas in equal times, T² ∝ r³.",
    "F = Gm1m2/r² — same law explains falling apples and orbiting moons.",
    "g decreases with both altitude and depth from Earth's surface.",
    "Escape speed ve = √(2GM/R); orbital speed vo = ve/√2.",
  ],
  exam_corner=[
    pyq(1, "State Kepler's law of periods."),
    pyq(1, "What is the value of escape speed from Earth's surface?"),
    pyq(2, "State the universal law of gravitation and write its formula, defining each term."),
    pyq(2, "How does the acceleration due to gravity vary with depth below Earth's surface?"),
    pyq(3, "Derive the expression for escape speed of a body from Earth's surface."),
    pyq(5, "State Kepler's three laws of planetary motion. Derive the relation between orbital velocity and escape velocity for a satellite near Earth's surface."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("VII", "Properties of Bulk Matter", [
chapter("ch09", 9, "Mechanical Properties of Solids",
  "Push, pull or twist a solid — it always tries to spring back (until it can't).",
  ["elasticity", "stress-strain", "Young's modulus"],
  sections=[
    section("Stress, Strain & Hooke's Law", [
      p("<b>Stress</b> = restoring force per unit area (how hard you're pushing/pulling per unit cross-section). "
        "<b>Strain</b> = fractional change in dimension (deformation caused). "
        "<b>Hooke's law:</b> for small deformations, stress ∝ strain."),
      formula("Types of modulus of elasticity", [
        "Young's modulus: Y = (F/A)/(ΔL/L)  — for length change",
        "Bulk modulus: K = −ΔP/(ΔV/V)  — for volume change",
        "Shear (rigidity) modulus: G = shear stress/shear strain",
      ]),
      solved(
        "A wire of length 2 m and cross-sectional area 1 mm² is stretched by 0.5 mm under a load. If Y = 2×10¹¹ Pa, find the applied force.",
        [
          "Y = (F/A)/(ΔL/L) → F = Y·A·ΔL/L",
          "A = 1×10⁻⁶ m², ΔL = 0.5×10⁻³ m, L = 2 m",
          "F = 2×10¹¹ × 1×10⁻⁶ × 0.5×10⁻³ / 2 = 50 N",
        ],
        "F = 50 N",
      ),
    ]),
    section("Stress–Strain Graph", [
      diagram("stressStrainGraph", "Beyond the elastic limit, the material doesn't return to its original shape.", 460, 240),
      p("Up to the <b>elastic limit</b>, the material returns to its original shape when the load is removed (Hooke's "
        "law region is linear). Beyond it, permanent deformation sets in, and eventually the material reaches its "
        "breaking point."),
      p("<b>Poisson's ratio</b> = (lateral strain)/(longitudinal strain) — how much a wire thins when stretched."),
      formula("Elastic potential energy stored in a stretched wire", ["U = ½ × stress × strain × volume = ½ × F × ΔL"]),
      tip("For 'derive elastic PE' questions, sketch the F–extension graph and use area = ½FΔx — examiners look specifically for this graphical justification."),
    ]),
  ],
  recap=[
    "Stress = force/area, strain = fractional deformation; Hooke's law: stress ∝ strain (elastic limit).",
    "Y for length change, K for volume change, G for shape (shear) change.",
    "Beyond the elastic limit, deformation becomes permanent.",
  ],
  exam_corner=[
    pyq(1, "Define Young's modulus of elasticity."),
    pyq(1, "What is Poisson's ratio?"),
    pyq(2, "Distinguish between elastic limit and breaking point using a stress-strain graph."),
    pyq(2, "A metal wire of length 1 m and area 2 mm² stretches by 1 mm under a 100 N load. Find Young's modulus."),
    pyq(3, "Derive the expression for elastic potential energy stored per unit volume in a stretched wire."),
    pyq(5, "Explain stress, strain and Hooke's law. Sketch and explain a typical stress-strain curve for a ductile metal, labelling the elastic limit, yield point and breaking point."),
  ]),

chapter("ch10", 10, "Mechanical Properties of Fluids",
  "Liquids that push equally in all directions, and pipes where speed and pressure trade places.",
  ["Pascal's law", "viscosity", "Bernoulli's theorem", "surface tension"],
  sections=[
    section("Pressure & Pascal's Law", [
      diagram("pascalLaw", "Pascal's law: a small force on a narrow piston creates a large force on a wide piston — hydraulic lift.", 480, 240),
      formula("Fluid pressure", ["P = F/A", "Pressure due to fluid column: P = hρg"]),
      p("<b>Pascal's law:</b> pressure applied at any point of an enclosed, incompressible fluid is transmitted "
        "<i>equally</i> in all directions — the basis of hydraulic lifts and hydraulic brakes."),
      solved(
        "In a hydraulic lift, the small piston has area 5 cm² and the large piston has area 100 cm². Find the force needed on the small piston to lift a 2000 N load.",
        [
          "Pascal's law: F1/A1 = F2/A2",
          "F1 = F2 × A1/A2 = 2000 × 5/100",
        ],
        "F1 = 100 N",
      ),
    ]),
    section("Viscosity & Bernoulli's Theorem", [
      p("<b>Viscosity</b> is a fluid's internal friction — resistance to relative flow between its layers. A ball falling "
        "through a viscous fluid reaches <b>terminal velocity</b> when viscous drag + buoyancy balance gravity (Stokes' law)."),
      diagram("bernoulliFlow", "Where a pipe narrows, fluid speeds up and pressure drops — Bernoulli's principle.", 480, 220),
      derivation("Bernoulli's theorem (energy conservation for flowing fluid)", "Consider an incompressible, non-viscous fluid flowing steadily through a pipe of varying cross-section.",
        [
          "Applying the work-energy theorem to a fluid element: work done by pressure forces = change in (KE + PE) of the fluid element.",
          "W = (P1 − P2)ΔV, and ΔKE = ½Δm(v2² − v1²), ΔPE = Δmg(h2 − h1)",
          "Equating and dividing by ΔV (using Δm = ρΔV): P1 + ½ρv1² + ρgh1 = P2 + ½ρv2² + ρgh2",
        ],
        "P + ½ρv² + ρgh = constant along a streamline"),
      formula("Bernoulli's theorem (along a streamline, no viscosity)", ["P + ½ρv² + ρgh = constant"]),
      mistake("Bernoulli's theorem applies only to non-viscous, incompressible, steady (streamline) flow — stating this assumption explicitly earns marks in CHSE answers."),
    ]),
    section("Surface Tension", [
      p("<b>Surface tension</b> makes a liquid surface behave like a stretched elastic membrane, minimising its area — "
        "that's why drops are spherical and insects can walk on water. It causes capillary rise in thin tubes, depending "
        "on the <b>angle of contact</b> between liquid and solid."),
      sticky("Real-life link", "Detergents reduce water's surface tension so it can spread and clean into fabric fibres "
             "instead of forming beads.", "yellow"),
    ]),
  ],
  recap=[
    "Pascal's law → pressure transmitted equally in enclosed fluid → hydraulic machines.",
    "Viscosity opposes relative flow; terminal velocity balances gravity, buoyancy and drag.",
    "Bernoulli: P + ½ρv² + ρgh = constant → speeds up where it narrows, pressure drops.",
    "Surface tension minimises surface area → spherical drops, capillary rise.",
  ],
  exam_corner=[
    pyq(1, "State Pascal's law."),
    pyq(1, "Define terminal velocity."),
    pyq(2, "State Bernoulli's theorem and write the equation with all terms defined."),
    pyq(2, "Why do insects float on water without sinking?"),
    pyq(3, "Derive Bernoulli's equation for a fluid flowing through a pipe of varying cross-section (statement of assumptions + derivation)."),
    pyq(5, "State Pascal's law and describe the working of a hydraulic lift with a labelled diagram. In a hydraulic press, pistons have areas 10 cm² and 200 cm² — find the force needed on the smaller piston to lift 4000 N."),
  ]),

chapter("ch11", 11, "Thermal Properties of Matter",
  "Heat isn't temperature — and knowing the difference solves half these problems.",
  ["thermal expansion", "specific heat", "heat transfer"],
  sections=[
    section("Temperature & Thermal Expansion", [
      diagram("thermalExpansion", "Heating a solid makes it expand — atoms vibrate more and push each other apart.", 480, 220),
      p("<b>Heat</b> is energy transferred due to a temperature difference; <b>temperature</b> is how hot/cold something "
        "is (average kinetic energy of molecules). Most substances <b>expand</b> when heated — solids in length/area/"
        "volume, liquids and gases in volume."),
      formula("Thermal expansion", ["Linear: L = L0(1 + αΔT)", "Area: A = A0(1 + βΔT), β ≈ 2α", "Volume: V = V0(1 + γΔT), γ ≈ 3α"]),
      sticky("Anomalous behaviour of water", "Water contracts (not expands) between 0°C and 4°C, reaching maximum "
             "density at 4°C — this is why ice floats and lakes don't freeze solid from the bottom up!", "blue"),
      solved(
        "A steel rod of length 2 m at 20°C is heated to 70°C. Find its new length. (α = 1.2×10⁻⁵ /°C)",
        [
          "ΔT = 70 − 20 = 50°C",
          "ΔL = L0αΔT = 2 × 1.2×10⁻⁵ × 50 = 1.2×10⁻³ m",
          "New length = 2 + 0.0012 = 2.0012 m",
        ],
        "2.0012 m",
      ),
    ]),
    section("Specific Heat Capacity & Calorimetry", [
      formula("Heat, specific heat & latent heat", [
        "Q = mcΔT   (c = specific heat capacity)",
        "Q = mL   (L = latent heat, during change of state — temperature doesn't change!)",
      ]),
      p("<b>CP</b> (specific heat at constant pressure) is greater than <b>CV</b> (at constant volume) for gases, because "
        "at constant pressure some heat also goes into doing work as the gas expands."),
      solved(
        "Find the heat required to convert 2 kg of ice at 0°C completely to water at 0°C. (Latent heat of fusion of ice = 3.36×10⁵ J/kg)",
        ["Q = mL = 2 × 3.36×10⁵"],
        "Q = 6.72×10⁵ J",
      ),
    ]),
    section("Heat Transfer", [
      olist([
        "<b>Conduction:</b> heat flows through a medium without the medium itself moving (touching a hot spoon).",
        "<b>Convection:</b> heat carried by actual movement of fluid particles (boiling water currents).",
        "<b>Radiation:</b> heat transferred via electromagnetic waves, needs no medium (sunlight reaching Earth).",
      ]),
      formula("Stefan's law & Wien's law", [
        "Stefan's law: E = σT⁴ (energy radiated per unit area per unit time)",
        "Wien's displacement law: λm T = constant",
      ]),
    ]),
  ],
  recap=[
    "Heat = energy in transit; temperature = degree of hotness — don't confuse the two.",
    "Water's anomalous expansion (0–4°C) is why ice floats.",
    "Q = mcΔT for temperature change; Q = mL for change of state at constant temperature.",
    "Conduction (medium, no bulk motion), convection (bulk fluid motion), radiation (no medium needed).",
  ],
  exam_corner=[
    pyq(1, "Define coefficient of linear expansion."),
    pyq(1, "State Wien's displacement law."),
    pyq(2, "Why does water show anomalous expansion between 0°C and 4°C? What is its significance for aquatic life?"),
    pyq(2, "Distinguish between conduction, convection and radiation with one example each."),
    pyq(3, "Explain why CP is greater than CV for a gas."),
    pyq(5, "Define specific heat capacity and latent heat. Calculate the heat required to convert 500 g of ice at −10°C to steam at 100°C. (cice=2100 J/kg°C, Lfusion=3.36×10⁵ J/kg, cwater=4200 J/kg°C, Lvap=2.26×10⁶ J/kg)"),
  ]),
])

# ----------------------------------------------------------------------
add_unit("VIII", "Thermodynamics", [
chapter("ch12", 12, "Thermodynamics",
  "The universe's strictest accountant: energy in, energy out, nothing lost.",
  ["laws of thermodynamics", "thermodynamic processes"],
  sections=[
    section("Zeroth & First Law", [
      p("<b>Zeroth law:</b> if A is in thermal equilibrium with B, and B with C, then A is in equilibrium with C — this "
        "is what makes a thermometer meaningful."),
      formula("First law of thermodynamics", ["ΔQ = ΔU + ΔW", "(Heat supplied = change in internal energy + work done by the system)"]),
      solved(
        "150 J of heat is supplied to a gas which does 60 J of work while expanding. Find the change in its internal energy.",
        ["ΔQ = ΔU + ΔW", "150 = ΔU + 60", "ΔU = 90 J"],
        "ΔU = 90 J (increase)",
      ),
    ]),
    section("Thermodynamic Processes", [
      diagram("heatEngineCycle", "A cyclic process on a P–V diagram — the enclosed area equals net work done per cycle.", 460, 240),
      lst([
        "<b>Isothermal:</b> temperature constant (PV = constant); happens slowly, in good thermal contact with surroundings.",
        "<b>Adiabatic:</b> no heat exchange with surroundings (ΔQ = 0); happens fast, or with perfect insulation.",
        "<b>Isochoric:</b> volume constant, so no work is done (ΔW = 0).",
        "<b>Cyclic:</b> system returns to its initial state, so ΔU = 0 over the full cycle.",
      ]),
      formula("Work done in special processes", [
        "Isothermal: W = nRT ln(V2/V1)",
        "Adiabatic: PVᵞ = constant  (γ = Cp/Cv)",
        "Cyclic process: Wnet = area enclosed by the P-V loop",
      ]),
    ]),
    section("Second Law of Thermodynamics", [
      p("Heat doesn't flow spontaneously from a cold body to a hot one, and no engine can be 100% efficient — some "
        "heat <i>must</i> be rejected to a sink. This law explains why processes have a preferred direction (entropy "
        "of an isolated system never decreases)."),
      mnemonic("First law = <b>bookkeeping</b> (energy is conserved). Second law = <b>direction</b> (which way things "
               "naturally go)."),
    ]),
  ],
  recap=[
    "Zeroth law defines thermal equilibrium and justifies using a thermometer.",
    "First law: ΔQ = ΔU + ΔW — energy conservation for thermodynamic systems.",
    "Isothermal (T const), adiabatic (Q=0), isochoric (W=0), cyclic (ΔU=0 overall).",
    "Second law: heat flows hot→cold spontaneously; no engine is 100% efficient.",
  ],
  exam_corner=[
    pyq(1, "State the zeroth law of thermodynamics."),
    pyq(1, "What is the value of work done in an isochoric process?"),
    pyq(2, "State the first law of thermodynamics and explain each term."),
    pyq(2, "Distinguish between isothermal and adiabatic processes."),
    pyq(3, "In a cyclic process, why is the net change in internal energy zero? Explain using the first law."),
    pyq(5, "State and explain the first law of thermodynamics. A gas absorbs 500 J of heat and its internal energy increases by 300 J — find the work done by the gas, and state whether it expanded or was compressed."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("IX", "Behaviour of Perfect Gases and Kinetic Theory of Gases", [
chapter("ch13", 13, "Kinetic Theory",
  "Gas pressure explained by billions of tiny, chaotic collisions.",
  ["ideal gas equation", "kinetic theory", "degrees of freedom"],
  sections=[
    section("Equation of State & Kinetic Theory Assumptions", [
      formula("Ideal gas equation", ["PV = nRT", "R = universal gas constant = 8.31 J mol⁻¹K⁻¹"]),
      diagram("kineticTheoryBox", "Kinetic theory pictures a gas as tiny particles in constant, random motion, colliding elastically.", 460, 240),
      lst([
        "Gas molecules are point masses in continuous random motion.",
        "Collisions between molecules (and with walls) are perfectly elastic.",
        "No intermolecular forces except during collision (ideal gas assumption).",
        "Pressure arises from the rate of momentum transfer to the walls.",
      ]),
    ]),
    section("Kinetic Interpretation of Temperature & rms Speed", [
      derivation("Pressure of an ideal gas (kinetic theory)", "N molecules of mass m each, in a cubical box of side L, moving randomly; consider one molecule moving with velocity component vx hitting a wall.",
        [
          "Each collision with the wall reverses vx, so change in momentum per collision = 2mvx.",
          "Time between successive collisions with the same wall = 2L/vx, so force from one molecule = 2mvx / (2L/vx) = mvx²/L.",
          "Summing over all N molecules and averaging, then extending to 3 dimensions (vx²=vy²=vz²=⟨v²⟩/3), total pressure P = (1/3)(Nm/V)⟨v²⟩ = (1/3)ρ⟨v²⟩",
        ],
        "P = (1/3) ρ ⟨v²⟩ ,  i.e. PV = (1/3)Nm⟨v²⟩"),
      formula("Kinetic theory results", [
        "Average KE per molecule: (3/2)kT  (k = Boltzmann constant)",
        "rms speed: vrms = √(3RT/M)",
      ]),
      solved(
        "Find the rms speed of oxygen molecules at 27°C. (M = 32×10⁻³ kg/mol, R = 8.31 J/mol·K)",
        [
          "T = 27 + 273 = 300 K",
          "vrms = √(3RT/M) = √(3×8.31×300/32×10⁻³) = √(7479/0.032) = √(233719)",
        ],
        "vrms ≈ 483 m/s",
      ),
      p("Temperature is simply a measure of the <b>average kinetic energy</b> of gas molecules — this is kinetic theory's "
        "biggest insight."),
    ]),
    section("Degrees of Freedom & Specific Heats", [
      p("<b>Degrees of freedom</b> = independent ways a molecule can store energy (translation, rotation, vibration). "
        "By the <b>law of equipartition of energy</b>, each degree of freedom gets (1/2)kT of energy on average."),
      sticky("Quick counts", "Monatomic gas: f = 3 (only translation). Diatomic gas: f = 5 (3 translation + 2 rotation, "
             "at moderate temperatures).", "yellow"),
    ]),
  ],
  recap=[
    "PV = nRT connects pressure, volume, moles and temperature for an ideal gas.",
    "Kinetic theory: pressure comes from molecular collisions; temperature ∝ average KE.",
    "vrms = √(3RT/M); rms speed increases with T, decreases with molar mass.",
    "Equipartition: each degree of freedom contributes (1/2)kT of average energy.",
  ],
  exam_corner=[
    pyq(1, "Define degrees of freedom of a gas molecule."),
    pyq(1, "What is the value of the universal gas constant R?"),
    pyq(2, "State the assumptions of kinetic theory of gases (any four)."),
    pyq(2, "Find the average kinetic energy of a gas molecule at 300 K. (k = 1.38×10⁻²³ J/K)"),
    pyq(3, "Derive the relation P = (1/3)ρ⟨v²⟩ using kinetic theory (basic outline)."),
    pyq(5, "State the postulates of kinetic theory of gases and derive the expression for pressure exerted by an ideal gas. Find the rms speed of hydrogen molecules at 300 K (M = 2×10⁻³ kg/mol)."),
  ]),
])

# ----------------------------------------------------------------------
add_unit("X", "Oscillations and Waves", [
chapter("ch14", 14, "Oscillations",
  "Back and forth, forever (almost) — the physics of anything that swings or bounces.",
  ["SHM", "spring-mass system", "simple pendulum"],
  sections=[
    section("Periodic Motion & SHM", [
      p("<b>Periodic motion</b> repeats itself at equal intervals of time (period T); <b>frequency</b> f = 1/T. "
        "<b>Simple Harmonic Motion (SHM)</b> is a special periodic motion where the restoring force is directly "
        "proportional to displacement and directed toward the mean position."),
      formula("SHM equations", [
        "F = −kx  (restoring force)",
        "x(t) = A sin(ωt + φ)",
        "ω = 2π/T = 2πf",
      ]),
    ]),
    section("Spring–Mass System", [
      diagram("springMass", "A block on a spring — the restoring force always pulls it back toward the centre.", 480, 220),
      derivation("Time period of a spring-mass system", "A block of mass m attached to a spring of force constant k, displaced by x from equilibrium.",
        [
          "Restoring force F = −kx (Hooke's law)",
          "By Newton's second law: ma = −kx → a = −(k/m)x",
          "Comparing with SHM equation a = −ω²x: ω² = k/m → ω = √(k/m)",
          "T = 2π/ω",
        ],
        "T = 2π√(m/k)"),
      formula("Spring oscillator", ["T = 2π√(m/k)", "Energy in SHM: E = ½kA² (total, constant throughout motion)"]),
      solved(
        "A 0.5 kg mass attached to a spring of force constant 200 N/m performs SHM. Find its time period.",
        ["T = 2π√(m/k) = 2π√(0.5/200) = 2π√(0.0025) = 2π(0.05)"],
        "T ≈ 0.314 s",
      ),
    ]),
    section("Simple Pendulum", [
      diagram("simplePendulum", "For small angles, a simple pendulum's motion is SHM about the vertical.", 460, 260),
      derivation("Time period of a simple pendulum", "A bob of mass m on a string of length L, displaced through a small angle θ.",
        [
          "Restoring force along the arc = −mg sinθ ≈ −mgθ (small angle approximation, sinθ ≈ θ)",
          "θ = x/L, so restoring force = −(mg/L)x, giving acceleration a = −(g/L)x",
          "Comparing with a = −ω²x: ω² = g/L → ω = √(g/L)",
        ],
        "T = 2π√(L/g)"),
      formula("Simple pendulum (small angle θ)", ["T = 2π√(L/g)"]),
      solved(
        "Find the length of a simple pendulum whose time period is 2 s. (g = 9.8 m/s²)",
        ["T = 2π√(L/g) → L = gT²/4π²", "L = 9.8 × 4 / (4×9.87) = 39.2/39.48"],
        "L ≈ 0.993 m (≈ 1 m — this is the 'seconds pendulum')",
      ),
      mnemonic("Pendulum time period does <b>not</b> depend on the mass of the bob or the amplitude (for small angles) "
               "— only on length L and gravity g. This is exactly what's used in the CHSE lab experiment with L~T² graphs!"),
    ]),
  ],
  recap=[
    "SHM: restoring force F = −kx, directed toward mean position.",
    "x(t) = A sin(ωt+φ); ω = 2π/T.",
    "Spring: T = 2π√(m/k); total energy E = ½kA² stays constant.",
    "Simple pendulum: T = 2π√(L/g) — independent of mass and (small) amplitude.",
  ],
  exam_corner=[
    pyq(1, "What is the phase difference between velocity and displacement in SHM?"),
    pyq(1, "Does the time period of a simple pendulum depend on the mass of the bob?"),
    pyq(2, "Define simple harmonic motion and write its differential equation."),
    pyq(2, "A spring of force constant 100 N/m carries a mass of 1 kg. Find the angular frequency of oscillation."),
    pyq(3, "Derive the expression for the time period of a simple pendulum performing SHM."),
    pyq(5, "Derive the time period of a mass-spring system executing SHM, and derive the expression for total energy in SHM. A particle executes SHM with amplitude 5 cm and period 2 s — find its maximum velocity and maximum acceleration."),
  ]),

chapter("ch15", 15, "Waves",
  "Energy travels, matter doesn't — the one-line summary of every wave.",
  ["transverse & longitudinal waves", "superposition", "standing waves", "beats"],
  sections=[
    section("Transverse & Longitudinal Waves", [
      diagram("transverseWave", "Transverse wave: particles vibrate perpendicular to the direction of wave travel.", 460, 200),
      diagram("longitudinalWave", "Longitudinal wave: particles vibrate along the direction of travel — compressions & rarefactions.", 460, 160),
      formula("Wave basics", ["v = f λ  (speed = frequency × wavelength)", "y(x,t) = A sin(kx − ωt)  — a progressive wave"]),
      solved(
        "A wave has frequency 500 Hz and wavelength 0.6 m. Find its speed.",
        ["v = fλ = 500 × 0.6"],
        "v = 300 m/s",
      ),
    ]),
    section("Superposition & Standing Waves", [
      p("The <b>principle of superposition</b>: when two or more waves overlap, the resultant displacement is the "
        "(vector) sum of individual displacements. When two identical waves travel in <b>opposite</b> directions "
        "(e.g. reflecting off a fixed end), they form a <b>standing wave</b>."),
      diagram("standingWave", "Standing wave: fixed nodes (no motion) and antinodes (maximum motion) appear at fixed points.", 460, 220),
      formula("Strings & organ pipes (fundamental + harmonics)", [
        "Stretched string, both ends fixed: fn = n v / 2L  (n = 1,2,3…)",
        "Closed organ pipe: only odd harmonics",
        "Open organ pipe: all harmonics",
      ]),
      solved(
        "A string of length 1 m fixed at both ends vibrates in its fundamental mode. If the wave speed on the string is 200 m/s, find the fundamental frequency.",
        ["f1 = v/2L = 200/(2×1)"],
        "f1 = 100 Hz",
      ),
    ]),
    section("Beats", [
      p("When two waves of slightly <b>different frequencies</b> overlap, the resultant amplitude rises and falls "
        "periodically — this is heard as <b>beats</b>, useful for tuning musical instruments."),
      formula("Beat frequency", ["fbeat = |f1 − f2|"]),
      mistake("Beat frequency is the DIFFERENCE of the two frequencies, not their sum or average — a very common slip under exam pressure."),
    ]),
  ],
  recap=[
    "Transverse: particle motion ⊥ wave direction; Longitudinal: particle motion ∥ wave direction.",
    "v = fλ links speed, frequency and wavelength for every wave.",
    "Standing waves = superposition of identical waves travelling in opposite directions — nodes & antinodes.",
    "Beat frequency = |f1 − f2|, from superposition of two close frequencies.",
  ],
  exam_corner=[
    pyq(1, "Define wavelength and frequency of a wave."),
    pyq(1, "What is the cause of beats?"),
    pyq(2, "Distinguish between transverse and longitudinal waves with one example each."),
    pyq(2, "Two tuning forks of frequency 256 Hz and 260 Hz are sounded together. Find the beat frequency."),
    pyq(3, "Explain the formation of standing waves in a stretched string fixed at both ends, and derive the frequency of the fundamental mode."),
    pyq(5, "State the principle of superposition of waves. Derive the expression for fundamental frequency and overtones of a stretched string fixed at both ends, with a labelled diagram of the first three harmonics."),
  ]),
])

CHAPTERS_FLAT = [ch for unit in UNITS for ch in unit["chapters"]]
