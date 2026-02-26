function renderNavbar() {
  const user = getUser();
  const nav = document.getElementById('navbar');
  if (!nav) return;

  // Detect dark theme (landing page)
  const isDark = document.body.classList.contains('bg-slate-950') || document.body.classList.contains('dark-nav');
  const textColor = isDark ? 'text-slate-300 hover:text-white' : 'text-slate-600 hover:text-blue-600';
  const brandColor = isDark ? 'text-white' : 'text-slate-900';
  const loginColor = isDark ? 'text-slate-300 hover:text-white' : 'text-slate-600 hover:text-slate-900';
  const mobileHover = isDark ? 'hover:bg-white/5' : 'hover:bg-slate-100';
  const mobileBorder = isDark ? 'border-white/10' : 'border-slate-200';
  const menuBtnHover = isDark ? 'hover:bg-white/10' : 'hover:bg-slate-100';
  const menuBtnColor = isDark ? 'text-white' : '';

  let links = '';
  let authButtons = '';

  if (!user) {
    // Public navbar
    links = `
      <a href="${FE_PREFIX}/" class="${textColor} font-medium transition">Home</a>
      <a href="${pageUrl('/browse-tasks')}" class="${textColor} font-medium transition">Browse Tasks</a>
      <a href="${pageUrl('/pricing')}" class="${textColor} font-medium transition">Pricing</a>
    `;
    authButtons = `
      <a href="${pageUrl('/login')}" class="${loginColor} font-medium px-4 py-2 transition">Login</a>
      <a href="${pageUrl('/register-student')}" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2.5 rounded-lg font-semibold transition shadow-lg shadow-blue-600/30">Register</a>
    `;
  } else if (user.role === 'student') {
    // Student navbar
    links = `
      <a href="${FE_PREFIX}/" class="${textColor} font-medium transition">Home</a>
      <a href="${pageUrl('/browse-tasks')}" class="${textColor} font-medium transition">Browse Tasks</a>
      <a href="${pageUrl('/student/my-submissions')}" class="${textColor} font-medium transition">My Submissions</a>
      <a href="${pageUrl('/student/profile')}" class="${textColor} font-medium transition">Profile</a>
    `;
    authButtons = `
      <span class="${isDark ? 'text-slate-400' : 'text-slate-500'} text-sm mr-2">Hi, ${user.name}</span>
      <button onclick="logout()" class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg font-medium transition">Logout</button>
    `;
  } else if (user.role === 'company') {
    // Company navbar
    links = `
      <a href="${pageUrl('/company/dashboard')}" class="${textColor} font-medium transition">Dashboard</a>
      <a href="${pageUrl('/company/create-task')}" class="${textColor} font-medium transition">Create Task</a>
      <a href="${pageUrl('/company/applicants')}" class="${textColor} font-medium transition">Applicants</a>
      <a href="${pageUrl('/company/subscription')}" class="${textColor} font-medium transition">Subscription</a>
      <a href="${pageUrl('/company/profile')}" class="${textColor} font-medium transition">Profile</a>
    `;
    authButtons = `
      <span class="${isDark ? 'text-slate-400' : 'text-slate-500'} text-sm mr-2">${user.name}</span>
      <button onclick="logout()" class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg font-medium transition">Logout</button>
    `;
  }

  nav.innerHTML = `
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">
        <a href="${FE_PREFIX}/" class="flex items-center gap-2">
          <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
            </svg>
          </div>
          <span class="font-bold text-xl tracking-tight ${brandColor}">SkillRank</span>
        </a>
        <div class="hidden md:flex items-center space-x-6">
          ${links}
        </div>
        <div class="flex items-center gap-3">
          ${authButtons}
        </div>
        <!-- Mobile menu button -->
        <button onclick="toggleMobileMenu()" class="md:hidden p-2 rounded-lg ${menuBtnHover} ${menuBtnColor}">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
      </div>
      <!-- Mobile menu -->
      <div id="mobile-menu" class="hidden md:hidden pb-4 space-y-2">
        ${links.replace(/class="[^"]*"/g, `class="block px-3 py-2 rounded-lg ${isDark ? 'text-slate-300 hover:bg-white/5' : 'text-slate-600 hover:bg-slate-100'} font-medium"`)}
        <div class="pt-2 border-t ${mobileBorder} flex gap-2">
          ${authButtons}
        </div>
      </div>
    </div>
  `;
}

function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  if (menu) menu.classList.toggle('hidden');
}

function logout() {
  clearAuth();
  window.location.href = pageUrl('/login');
}

// Auto-render on load
document.addEventListener('DOMContentLoaded', renderNavbar);
