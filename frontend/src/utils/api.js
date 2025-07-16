import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8001';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API functions
export const apiService = {
  // Health check
  healthCheck: () => api.get('/api/health'),
  
  // Projects
  getProjects: (category = null) => {
    const params = category ? { category } : {};
    return api.get('/api/projects', { params });
  },
  
  getProject: (id) => api.get(`/api/projects/${id}`),
  
  createProject: (formData) => api.post('/api/projects', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  }),
  
  // Contact
  submitContact: (contactData) => api.post('/api/contact', contactData),
  
  getContactMessages: () => api.get('/api/contact'),
};

export default api;