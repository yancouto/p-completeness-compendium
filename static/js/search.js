// Client-side search and filtering for problems
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-input');
  const categoryFilter = document.getElementById('category-filter');
  const statusFilter = document.getElementById('status-filter');
  const problemsGrid = document.getElementById('problems-grid');
  const visibleCount = document.getElementById('visible-count');
  
  if (!problemsGrid) return;
  
  const problems = problemsGrid.querySelectorAll('.problem-card');
  
  function filterProblems() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    const selectedCategory = categoryFilter.value;
    const selectedStatus = statusFilter.value;
    
    let visible = 0;
    
    problems.forEach(function(card) {
      const title = card.dataset.title || '';
      const acronym = card.dataset.acronym || '';
      const category = card.dataset.category || '';
      const status = card.dataset.status || '';
      const tags = card.dataset.tags || '';
      
      // Check search term
      const matchesSearch = !searchTerm || 
        title.includes(searchTerm) || 
        acronym.includes(searchTerm) ||
        tags.includes(searchTerm);
      
      // Check category filter
      const matchesCategory = !selectedCategory || category === selectedCategory;
      
      // Check status filter
      const matchesStatus = !selectedStatus || status === selectedStatus;
      
      // Show/hide card
      if (matchesSearch && matchesCategory && matchesStatus) {
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
  
  // URL parameter support for direct linking to filtered views
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('category')) {
    categoryFilter.value = urlParams.get('category');
  }
  if (urlParams.has('status')) {
    statusFilter.value = urlParams.get('status');
  }
  if (urlParams.has('q')) {
    searchInput.value = urlParams.get('q');
  }
  
  // Initial filter
  filterProblems();
});
