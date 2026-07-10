import axios, { AxiosInstance } from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient: AxiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

// Handle responses
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  },
);

// Auth API
export const authApi = {
  login: (email: string, password: string) =>
    apiClient.post('/auth/login', { email, password }),
  register: (email: string, username: string, password: string, full_name?: string) =>
    apiClient.post('/auth/register', { email, username, password, full_name }),
  me: () => apiClient.get('/auth/me'),
};

// Users API
export const usersApi = {
  getProfile: () => apiClient.get('/users/profile'),
  updateProfile: (data: any) => apiClient.put('/users/profile', data),
};

// Interviews API
export const interviewsApi = {
  startInterview: (data: any) => apiClient.post('/interviews/start', data),
  listInterviews: (skip?: number, limit?: number) =>
    apiClient.get('/interviews/list', { params: { skip, limit } }),
  getInterview: (id: string) => apiClient.get(`/interviews/${id}`),
};

// Resumes API
export const resumesApi = {
  uploadResume: (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    return apiClient.post('/resumes/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
  listResumes: () => apiClient.get('/resumes/list'),
};

// Reports API
export const reportsApi = {
  getReport: (id: string) => apiClient.get(`/reports/${id}`),
};

// Analytics API
export const analyticsApi = {
  getDashboard: () => apiClient.get('/analytics/dashboard'),
};

export default apiClient;
