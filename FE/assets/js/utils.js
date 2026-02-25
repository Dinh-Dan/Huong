// Toast notifications
function showToast(message, type = 'success') {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 3000);
}

// Loading state
function showLoading(btn) {
  if (!btn) return;
  btn.disabled = true;
  btn.dataset.originalText = btn.innerHTML;
  btn.innerHTML = '<span class="spinner"></span> Loading...';
}

function hideLoading(btn) {
  if (!btn) return;
  btn.disabled = false;
  btn.innerHTML = btn.dataset.originalText || 'Submit';
}

// Date formatting
function formatDate(dateStr) {
  if (!dateStr) return '-';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

function formatDateTime(dateStr) {
  if (!dateStr) return '-';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', {
    year: 'numeric', month: 'short', day: 'numeric',
    hour: '2-digit', minute: '2-digit'
  });
}

// Status badge
function statusBadge(status) {
  const badges = {
    pending: '<span class="badge-pending px-3 py-1 rounded-full text-xs font-semibold">Pending</span>',
    reviewed: '<span class="badge-reviewed px-3 py-1 rounded-full text-xs font-semibold">Reviewed</span>',
    interested: '<span class="badge-interested px-3 py-1 rounded-full text-xs font-semibold">Accepted</span>',
    rejected: '<span class="badge-rejected px-3 py-1 rounded-full text-xs font-semibold">Rejected</span>',
    active: '<span class="badge-interested px-3 py-1 rounded-full text-xs font-semibold">Active</span>',
    closed: '<span class="badge-rejected px-3 py-1 rounded-full text-xs font-semibold">Closed</span>',
    draft: '<span class="badge-pending px-3 py-1 rounded-full text-xs font-semibold">Draft</span>'
  };
  return badges[status] || status;
}

// Difficulty badge
function difficultyBadge(level) {
  const badges = {
    easy: '<span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-xs font-semibold">Easy</span>',
    medium: '<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-xs font-semibold">Medium</span>',
    hard: '<span class="bg-red-100 text-red-700 px-3 py-1 rounded-full text-xs font-semibold">Hard</span>'
  };
  return badges[level] || level;
}

// Score bar HTML
function scoreBar(score) {
  if (score === null || score === undefined) return '-';
  return `
    <div class="flex items-center gap-2">
      <div class="score-bar w-20">
        <div class="score-bar-fill" style="width:${score}%"></div>
      </div>
      <span class="text-sm font-semibold">${score}</span>
    </div>
  `;
}

// Truncate text
function truncate(text, maxLen = 100) {
  if (!text) return '';
  return text.length > maxLen ? text.substring(0, maxLen) + '...' : text;
}

// URL query params
function getQueryParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}
