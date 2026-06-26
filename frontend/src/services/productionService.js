import api from './api';

export const productionService = {
  recordProduction: async (data) => {
    const response = await api.post('/production', data);
    return response.data;
  },

  getProduction: async (filters = {}) => {
    const response = await api.get('/production', { params: filters });
    return response.data;
  },

  getProductionById: async (id) => {
    const response = await api.get(`/production/${id}`);
    return response.data;
  },

  updateProduction: async (id, data) => {
    const response = await api.put(`/production/${id}`, data);
    return response.data;
  },

  deleteProduction: async (id) => {
    await api.delete(`/production/${id}`);
  },

  getDailyStats: async (dateFrom, dateTo) => {
    const response = await api.get('/production/stats/daily', {
      params: { date_from: dateFrom, date_to: dateTo },
    });
    return response.data;
  },
};
