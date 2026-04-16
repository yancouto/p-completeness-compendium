document.addEventListener('DOMContentLoaded', function () {
  const statusLabels = {
    'p-complete': 'P-complete',
    'p-hard': 'P-hard',
    'open': 'Open'
  };

  function normalize(value) {
    return (value || '').toString().trim().toLowerCase();
  }

  function parsePipeList(value) {
    return (value || '')
      .split('|')
      .map(function (item) { return normalize(item); })
      .filter(Boolean);
  }

  function parseQueryValues(params, keys) {
    const values = new Set();
    keys.forEach(function (key) {
      params.getAll(key).forEach(function (rawValue) {
        rawValue.split(',').forEach(function (value) {
          const normalized = normalize(value);
          if (normalized) {
            values.add(normalized);
          }
        });
      });
    });
    return values;
  }

  function initHomeSearch() {
    const input = document.getElementById('home-search-input');
    const results = document.getElementById('home-search-results');
    const dataEl = document.getElementById('home-problems-data');

    if (!input || !results) return;

    let dataset = [];
    if (Array.isArray(window.__HOME_PROBLEMS__)) {
      dataset = window.__HOME_PROBLEMS__;
    } else if (dataEl) {
      try {
        dataset = JSON.parse(dataEl.textContent || '[]');
        if (typeof dataset === 'string') {
          dataset = JSON.parse(dataset);
        }
      } catch (error) {
        dataset = [];
      }
    }

    const problems = dataset.map(function (item) {
      return {
        title: item.title || '',
        acronym: item.acronym || '',
        status: normalize(item.status) || 'p-complete',
        url: item.url || '#',
        titleLower: normalize(item.title),
        acronymLower: normalize(item.acronym)
      };
    });

    let matches = [];
    let activeIndex = -1;

    function closeResults() {
      matches = [];
      activeIndex = -1;
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
      results.hidden = true;
      results.innerHTML = '';
    }

    function renderMatches() {
      if (!matches.length) {
        closeResults();
        return;
      }

      results.innerHTML = '';
      matches.forEach(function (item, index) {
        const option = document.createElement('li');
        option.id = 'home-search-option-' + index;
        option.className = 'home-search-option' + (index === activeIndex ? ' is-active' : '');
        option.setAttribute('role', 'option');
        option.setAttribute('aria-selected', index === activeIndex ? 'true' : 'false');

        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'home-search-hit';
        button.dataset.url = item.url;

        const title = document.createElement('span');
        title.className = 'home-search-name';
        title.textContent = item.acronym ? item.title + ' (' + item.acronym + ')' : item.title;

        const status = document.createElement('span');
        status.className = 'status status-' + item.status;
        status.textContent = statusLabels[item.status] || 'P-complete';

        button.appendChild(title);
        button.appendChild(status);
        option.appendChild(button);
        results.appendChild(option);
      });

      if (activeIndex >= 0) {
        input.setAttribute('aria-activedescendant', 'home-search-option-' + activeIndex);
      } else {
        input.removeAttribute('aria-activedescendant');
      }

      input.setAttribute('aria-expanded', 'true');
      results.hidden = false;
    }

    function updateMatches() {
      const term = normalize(input.value);
      if (!term) {
        closeResults();
        return;
      }

      matches = problems.filter(function (item) {
        return item.titleLower.includes(term) || item.acronymLower.includes(term);
      }).slice(0, 8);

      activeIndex = -1;
      renderMatches();
    }

    input.addEventListener('input', updateMatches);
    input.addEventListener('focus', function () {
      if (normalize(input.value)) {
        updateMatches();
      }
    });

    input.addEventListener('keydown', function (event) {
      if (!matches.length) return;

      if (event.key === 'ArrowDown') {
        event.preventDefault();
        activeIndex = (activeIndex + 1) % matches.length;
        renderMatches();
      } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        activeIndex = activeIndex <= 0 ? matches.length - 1 : activeIndex - 1;
        renderMatches();
      } else if (event.key === 'Enter') {
        event.preventDefault();
        const selected = activeIndex >= 0 ? matches[activeIndex] : matches[0];
        if (selected && selected.url) {
          window.location.assign(selected.url);
        }
      } else if (event.key === 'Escape') {
        closeResults();
      }
    });

    results.addEventListener('click', function (event) {
      const hit = event.target.closest('.home-search-hit');
      if (!hit || !hit.dataset.url) return;
      window.location.assign(hit.dataset.url);
    });

    document.addEventListener('click', function (event) {
      if (!event.target.closest('.home-search-box')) {
        closeResults();
      }
    });
  }

  function initProblemsFilters() {
    const searchInput = document.getElementById('search-input');
    const problemsGrid = document.getElementById('problems-grid');
    const visibleCount = document.getElementById('visible-count');

    if (!searchInput || !problemsGrid) return;

    const cards = Array.from(problemsGrid.querySelectorAll('.problem-card'));
    const multiSelectNodes = Array.from(document.querySelectorAll('.multi-select[data-filter-group]'));
    const urlParams = new URLSearchParams(window.location.search);
    let openSelect = null;

    function queryKeysForGroup(groupKey) {
      if (groupKey === 'category') return ['category', 'categories'];
      if (groupKey === 'status') return ['status', 'statuses'];
      if (groupKey === 'tag') return ['tag', 'tags'];
      return [groupKey, groupKey + 's'];
    }

    function closeMultiSelect(config) {
      if (!config) return;
      config.panel.hidden = true;
      config.toggle.setAttribute('aria-expanded', 'false');
      if (openSelect === config) {
        openSelect = null;
      }
    }

    function renderGroup(config) {
      const selectedValues = Array.from(config.selected);
      const labels = selectedValues.map(function (value) {
        return config.labelMap.get(value) || value;
      });

      if (!labels.length) {
        config.text.textContent = config.placeholder;
      } else if (labels.length === 1) {
        config.text.textContent = labels[0];
      } else {
        config.text.textContent = labels.length + ' selected';
      }

      config.chips.innerHTML = '';
      labels.forEach(function (label) {
        const normalized = normalize(label);
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'filter-chip';
        chip.dataset.value = normalized;
        chip.textContent = label + ' ×';
        config.chips.appendChild(chip);
      });
    }

    function updateUrl() {
      const nextParams = new URLSearchParams();
      const searchValue = searchInput.value.trim();

      if (searchValue) {
        nextParams.set('q', searchValue);
      }

      groups.forEach(function (group) {
        Array.from(group.selected)
          .map(function (value) { return group.paramMap.get(value) || value; })
          .sort(function (a, b) { return a.localeCompare(b); })
          .forEach(function (value) {
            nextParams.append(group.queryKey, value);
          });
      });

      const query = nextParams.toString();
      const newUrl = query ? window.location.pathname + '?' + query : window.location.pathname;
      window.history.replaceState({}, '', newUrl);
    }

    function applyFilters() {
      const searchTerm = normalize(searchInput.value);
      const selectedByGroup = {};
      groups.forEach(function (group) {
        selectedByGroup[group.groupKey] = group.selected;
      });

      const selectedCategory = selectedByGroup.category || new Set();
      const selectedStatus = selectedByGroup.status || new Set();
      const selectedTag = selectedByGroup.tag || new Set();

      let visible = 0;

      cards.forEach(function (card) {
        const cardCategories = parsePipeList(card.dataset.categories);
        const cardTags = parsePipeList(card.dataset.tags);
        const cardStatus = normalize(card.dataset.status);
        const searchableText = [
          card.dataset.title || '',
          card.dataset.acronym || '',
          card.dataset.categories || '',
          card.dataset.tags || ''
        ].join(' ');

        const matchesSearch = !searchTerm || normalize(searchableText).includes(searchTerm);
        const matchesCategory = !selectedCategory.size || cardCategories.some(function (value) {
          return selectedCategory.has(value);
        });
        const matchesStatus = !selectedStatus.size || selectedStatus.has(cardStatus);
        const matchesTags = !selectedTag.size || cardTags.some(function (value) {
          return selectedTag.has(value);
        });

        const shouldShow = matchesSearch && matchesCategory && matchesStatus && matchesTags;
        card.style.display = shouldShow ? '' : 'none';
        if (shouldShow) visible += 1;
      });

      if (visibleCount) {
        visibleCount.textContent = String(visible);
      }

      updateUrl();
    }

    const groups = multiSelectNodes.map(function (node) {
      const groupKey = node.dataset.filterGroup;
      const queryKey = node.dataset.queryKey || groupKey;
      const placeholder = node.dataset.placeholder || 'Any';
      const toggle = node.querySelector('.multi-select-toggle');
      const panel = node.querySelector('.multi-select-panel');
      const text = node.querySelector('.multi-select-text');
      const chips = node.querySelector('.selected-chips');
      const checkboxes = Array.from(node.querySelectorAll('input[type="checkbox"]'));
      const hydratedValues = parseQueryValues(urlParams, queryKeysForGroup(groupKey));
      const selected = new Set();
      const labelMap = new Map();
      const paramMap = new Map();

      checkboxes.forEach(function (checkbox) {
        const normalized = normalize(checkbox.value);
        labelMap.set(normalized, checkbox.dataset.label || checkbox.value);
        paramMap.set(normalized, checkbox.value);
        checkbox.dataset.normalized = normalized;

        if (hydratedValues.has(normalized)) {
          checkbox.checked = true;
          selected.add(normalized);
        }

        checkbox.addEventListener('change', function () {
          if (checkbox.checked) {
            selected.add(normalized);
          } else {
            selected.delete(normalized);
          }
          renderGroup(config);
          applyFilters();
        });
      });

      const config = {
        groupKey: groupKey,
        queryKey: queryKey,
        placeholder: placeholder,
        toggle: toggle,
        panel: panel,
        text: text,
        chips: chips,
        selected: selected,
        labelMap: labelMap,
        paramMap: paramMap
      };

      toggle.addEventListener('click', function () {
        const willOpen = panel.hidden;
        if (openSelect && openSelect !== config) {
          closeMultiSelect(openSelect);
        }
        panel.hidden = !willOpen;
        toggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
        openSelect = willOpen ? config : null;
      });

      chips.addEventListener('click', function (event) {
        const chip = event.target.closest('.filter-chip');
        if (!chip) return;
        const normalized = chip.dataset.value;
        selected.delete(normalized);
        checkboxes.forEach(function (checkbox) {
          if (checkbox.dataset.normalized === normalized) {
            checkbox.checked = false;
          }
        });
        renderGroup(config);
        applyFilters();
      });

      renderGroup(config);
      return config;
    });

    searchInput.value = urlParams.get('q') || '';
    searchInput.addEventListener('input', applyFilters);

    document.addEventListener('click', function (event) {
      if (!event.target.closest('.multi-select') && openSelect) {
        closeMultiSelect(openSelect);
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && openSelect) {
        closeMultiSelect(openSelect);
      }
    });

    applyFilters();
  }

  initHomeSearch();
  initProblemsFilters();
});
