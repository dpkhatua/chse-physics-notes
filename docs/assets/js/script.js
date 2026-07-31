// Shared site behaviour: mobile nav, chapter search/filter, read-progress checkboxes
document.addEventListener('DOMContentLoaded', function () {

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  // Chapter search filter (used on class index pages)
  var searchBox = document.querySelector('.search-box');
  if (searchBox) {
    searchBox.addEventListener('input', function () {
      var q = searchBox.value.trim().toLowerCase();
      document.querySelectorAll('.chapter-card').forEach(function (card) {
        var text = card.textContent.toLowerCase();
        card.style.display = text.indexOf(q) !== -1 ? '' : 'none';
      });
    });
  }

  // Mark chapter as "read" — stored in localStorage, reflected on class index pages
  var chapterId = document.body.getAttribute('data-chapter-id');
  var progressKey = 'chsePhysicsProgress';

  function getProgress() {
    try { return JSON.parse(localStorage.getItem(progressKey)) || {}; }
    catch (e) { return {}; }
  }
  function setProgress(p) {
    localStorage.setItem(progressKey, JSON.stringify(p));
  }

  if (chapterId) {
    var checkbox = document.getElementById('mark-read');
    if (checkbox) {
      var progress = getProgress();
      checkbox.checked = !!progress[chapterId];
      checkbox.addEventListener('change', function () {
        var p = getProgress();
        p[chapterId] = checkbox.checked;
        setProgress(p);
      });
    }
  }

  // On class index pages, tick off cards already marked read
  document.querySelectorAll('.chapter-card[data-chapter-id]').forEach(function (card) {
    var id = card.getAttribute('data-chapter-id');
    var progress = getProgress();
    if (progress[id]) {
      card.style.borderColor = '#0e8a7d';
      var doneTag = document.createElement('span');
      doneTag.textContent = '✓ done';
      doneTag.style.float = 'right';
      doneTag.style.color = '#0e8a7d';
      doneTag.style.fontFamily = "'Caveat', cursive";
      doneTag.style.fontSize = '1.1rem';
      card.querySelector('h3') && card.querySelector('h3').insertAdjacentElement('afterend', doneTag);
    }
  });
});
