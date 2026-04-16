document.addEventListener('DOMContentLoaded', function() {
  const input = document.getElementById('home-problem-search');
  const menu = document.getElementById('home-search-results');
  const problems = Array.isArray(window.homeProblems) ? window.homeProblems : [];

  if (!input || !menu || problems.length === 0) return;

  const statusLabel = {
    'p-complete': 'P-complete',
    'p-hard': 'P-hard',
    'open': 'Open'
  };

  function clearResults() {
    menu.innerHTML = '';
    menu.hidden = true;
  }

  function renderResults(matches) {
    if (matches.length === 0) {
      clearResults();
      return;
    }

    menu.innerHTML = '';
    matches.forEach(function(problem) {
      const item = document.createElement('li');
      item.className = 'autocomplete-item';

      const link = document.createElement('a');
      link.className = 'autocomplete-link';
      link.href = problem.url;

      const title = document.createElement('span');
      title.className = 'autocomplete-title';
      title.textContent = problem.acronym
        ? problem.title + ' (' + problem.acronym + ')'
        : problem.title;

      const status = document.createElement('span');
      status.className = 'status autocomplete-status status-' + (problem.status || 'p-complete');
      status.textContent = statusLabel[problem.status] || 'P-complete';

      link.appendChild(title);
      link.appendChild(status);
      item.appendChild(link);
      menu.appendChild(item);
    });

    menu.hidden = false;
  }

  input.addEventListener('input', function() {
    const query = input.value.trim().toLowerCase();
    if (!query) {
      clearResults();
      return;
    }

    const matches = problems
      .filter(function(problem) {
        const title = (problem.title || '').toLowerCase();
        const acronym = (problem.acronym || '').toLowerCase();
        return title.includes(query) || acronym.includes(query);
      })
      .slice(0, 8);

    renderResults(matches);
  });

  input.addEventListener('focus', function() {
    if (input.value.trim()) {
      input.dispatchEvent(new Event('input'));
    }
  });

  document.addEventListener('click', function(event) {
    if (!menu.contains(event.target) && event.target !== input) {
      clearResults();
    }
  });
});
