// Client-side search and filtering for problems
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-input');
  const categoryFilter = document.getElementById('category-filter');
  const statusFilter = document.getElementById('status-filter');
  const tagFilter = document.getElementById('tag-filter');
  const problemsGrid = document.getElementById('problems-grid');
  const visibleCount = document.getElementById('visible-count');
  
  if (!problemsGrid || !searchInput || !categoryFilter || !statusFilter || !tagFilter) return;
  
  const problems = problemsGrid.querySelectorAll('.problem-card');

  function getSelectedValues(selectElement) {
    return Array.from(selectElement.selectedOptions)
      .map(function(option) { return option.value.toLowerCase(); })
      .filter(Boolean);
  }

  function setMultiSelectFromParam(selectElement, value) {
    const selectedValues = (value || '')
      .split(',')
      .map(function(item) { return item.trim().toLowerCase(); })
      .filter(Boolean);

    Array.from(selectElement.options).forEach(function(option) {
      option.selected = selectedValues.includes(option.value.toLowerCase());
    });
  }
  
  function filterProblems() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    const selectedCategories = getSelectedValues(categoryFilter);
    const selectedStatuses = getSelectedValues(statusFilter);
    const selectedTags = getSelectedValues(tagFilter);
    
    let visible = 0;
    
    problems.forEach(function(card) {
      const title = card.dataset.title || '';
      const acronym = card.dataset.acronym || '';
      const categories = (card.dataset.category || '')
        .split('|')
        .map(function(item) { return item.trim().toLowerCase(); })
        .filter(Boolean);
      const status = (card.dataset.status || '').toLowerCase();
      const tags = (card.dataset.tags || '')
        .split('|')
        .map(function(item) { return item.trim().toLowerCase(); })
        .filter(Boolean);
      const tagsText = tags.join(' ');
      
      // Check search term
      const matchesSearch = !searchTerm || 
        title.includes(searchTerm) || 
        acronym.includes(searchTerm) ||
        tagsText.includes(searchTerm);
      
      // Check category filter
      const matchesCategory = selectedCategories.length === 0 ||
        selectedCategories.some(function(category) {
          return categories.includes(category);
        });
      
      // Check status filter
      const matchesStatus = selectedStatuses.length === 0 || selectedStatuses.includes(status);

      // Check tag filter
      const matchesTags = selectedTags.length === 0 ||
        selectedTags.some(function(tag) {
          return tags.includes(tag);
        });
      
      // Show/hide card
      if (matchesSearch && matchesCategory && matchesStatus && matchesTags) {
        card.style.display = '';
        visible++;
      } else {
        card.style.display = 'none';
      }
    });
    
    visibleCount.textContent = visible;
  }
  
  // Attach event listeners
  searchInput.addEventListener('input', filterProblems);
  categoryFilter.addEventListener('change', filterProblems);
  statusFilter.addEventListener('change', filterProblems);
  tagFilter.addEventListener('change', filterProblems);
  
  // URL parameter support for direct linking to filtered views
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('category')) {
    setMultiSelectFromParam(categoryFilter, urlParams.get('category'));
  }
  if (urlParams.has('status')) {
    setMultiSelectFromParam(statusFilter, urlParams.get('status'));
  }
  if (urlParams.has('tags')) {
    setMultiSelectFromParam(tagFilter, urlParams.get('tags'));
  }
  if (urlParams.has('q')) {
    searchInput.value = urlParams.get('q');
  }
  
  // Initial filter
  filterProblems();
});
