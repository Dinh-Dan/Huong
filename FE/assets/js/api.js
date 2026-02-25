const API_BASE = 'http://localhost:5000/api';

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
        window.location.href = '/FE/login.html';
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
    window.location.href = '/FE/login.html';
    return false;
  }
  if (role) {
    const user = getUser();
    if (user.role !== role) {
      window.location.href = user.role === 'student'
        ? '/FE/student/dashboard.html'
        : '/FE/company/dashboard.html';
      return false;
    }
  }
  return true;
}

function redirectIfLoggedIn() {
  if (isLoggedIn()) {
    const user = getUser();
    window.location.href = user.role === 'student'
      ? '/FE/student/dashboard.html'
      : '/FE/company/dashboard.html';
  }
}
