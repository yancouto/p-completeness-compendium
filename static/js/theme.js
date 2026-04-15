(function () {
  const STORAGE_KEY = 'theme-preference';

  function getStoredTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setStoredTheme(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) {
      // Ignore storage errors.
    }
  }

  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function getInitialTheme() {
    const stored = getStoredTheme();
    return stored === 'light' || stored === 'dark' ? stored : getSystemTheme();
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
  }

  function updateToggle(theme) {
    const button = document.getElementById('theme-toggle');
    if (!button) return;

    const icon = button.querySelector('.theme-toggle-icon');
    const label = button.querySelector('.theme-toggle-label');

    const isDark = theme === 'dark';
    button.setAttribute('aria-pressed', String(isDark));
    button.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');

    if (icon) icon.textContent = isDark ? 'light_mode' : 'dark_mode';
    if (label) label.textContent = isDark ? 'Light' : 'Dark';
  }

  function flashReferenceTarget(referenceId) {
    const target = document.getElementById(referenceId);
    if (!target || !target.classList.contains('reference-item')) return;
    target.classList.remove('reference-item-highlight');
    void target.offsetWidth;
    target.classList.add('reference-item-highlight');
    window.setTimeout(function () {
      target.classList.remove('reference-item-highlight');
    }, 1600);
  }

  function setupReferenceCitationHighlights() {
    const links = document.querySelectorAll('.problem-content a[href^="#"]');
    links.forEach(function (link) {
      const hash = link.getAttribute('href');
      if (!hash || !/^#\d+$/.test(hash)) return;
      link.classList.add('reference-citation');

      link.addEventListener('click', function () {
        flashReferenceTarget(hash.slice(1));
      });
    });

    if (window.location.hash && /^#\d+$/.test(window.location.hash)) {
      flashReferenceTarget(window.location.hash.slice(1));
    }

    window.addEventListener('hashchange', function () {
      if (window.location.hash && /^#\d+$/.test(window.location.hash)) {
        flashReferenceTarget(window.location.hash.slice(1));
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    const theme = getInitialTheme();
    applyTheme(theme);
    updateToggle(theme);
    setupReferenceCitationHighlights();

    const button = document.getElementById('theme-toggle');
    if (button) {
      button.addEventListener('click', function () {
        const current = document.documentElement.getAttribute('data-theme') || getInitialTheme();
        const next = current === 'dark' ? 'light' : 'dark';
        applyTheme(next);
        setStoredTheme(next);
        updateToggle(next);
      });
    }
  });
})();
