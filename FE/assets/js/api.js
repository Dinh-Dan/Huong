// Chế độ chạy: 'apache' hoặc 'liveserver'
// Đổi thành 'apache' khi deploy qua Apache/XAMPP
const RUN_MODE = 'liveserver';
const API_BASE = RUN_MODE === 'liveserver' ? 'http://localhost:5000/api' : '/api';

// Helper: URL cho file uploads (ảnh, CV, submissions)
const UPLOAD_BASE = RUN_MODE === 'liveserver' ? 'http://localhost:5000' : '';

// Prefix thư mục FE khi Live Server serve từ thư mục cha
const FE_PREFIX = RUN_MODE === 'liveserver' ? '/FE' : '';

// Helper: thêm prefix FE + .html cho Live Server
function pageUrl(path) {
  if (RUN_MODE !== 'liveserver') return path;
  // Bỏ qua nếu đã có extension, hoặc là thư mục (kết thúc bằng /)
  if (path.includes('.') || path.endsWith('/')) return FE_PREFIX + path;
  // Giữ query string
  const [pathname, query] = path.split('?');
  return query ? `${FE_PREFIX}${pathname}.html?${query}` : `${FE_PREFIX}${pathname}.html`;
}


function getToken() {
  return localStorage.getItem('token');
}

function getUser() {
  const user = localStorage.getItem('user');
  return user ? JSON.parse(user) : null;
}

function setAuth(token, user) {
  localStorage.setItem('token', token);
  localStorage.setItem('user', JSON.stringify(user));
}

function clearAuth() {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
}

function isLoggedIn() {
  return !!getToken();
}

function getHeaders(isFormData = false) {
  const headers = {};
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;
  if (!isFormData) headers['Content-Type'] = 'application/json';
  return headers;
}

async function apiRequest(method, endpoint, data = null, isFormData = false) {
  const url = `${API_BASE}${endpoint}`;
  const options = {
    method,
    headers: getHeaders(isFormData)
  };

  if (data) {
    options.body = isFormData ? data : JSON.stringify(data);
  }

  try {
    const response = await fetch(url, options);
    const result = await response.json();

    if (!response.ok) {
      // Only auto-redirect on 401 if user was previously logged in (token expired)
      // Don't redirect if we're on the login page (login attempt failed)
      if (response.status === 401 && getToken()) {
        clearAuth();
        window.location.href = pageUrl('/login');
        return;
      }
      throw { status: response.status, ...result };
    }

    return result;
  } catch (err) {
    if (err.status) throw err;
    throw { status: 500, message: 'Network error. Please try again.' };
  }
}

function apiGet(endpoint) {
  return apiRequest('GET', endpoint);
}

function apiPost(endpoint, data, isFormData = false) {
  return apiRequest('POST', endpoint, data, isFormData);
}

function apiPut(endpoint, data, isFormData = false) {
  return apiRequest('PUT', endpoint, data, isFormData);
}

function apiDelete(endpoint) {
  return apiRequest('DELETE', endpoint);
}

// Redirect helpers
function requireAuth(role = null) {
  if (!isLoggedIn()) {
    window.location.href = pageUrl('/login');
    return false;
  }
  if (role) {
    const user = getUser();
    if (user.role !== role) {
      window.location.href = pageUrl(user.role === 'student'
        ? '/student/dashboard'
        : '/company/dashboard');
      return false;
    }
  }
  return true;
}

function redirectIfLoggedIn() {
  if (isLoggedIn()) {
    const user = getUser();
    window.location.href = pageUrl(user.role === 'student'
      ? '/student/dashboard'
      : '/company/dashboard');
  }
}
