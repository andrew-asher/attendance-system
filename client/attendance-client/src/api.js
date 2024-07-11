// api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Ensure this matches your Django backend URL
});

export default api;
