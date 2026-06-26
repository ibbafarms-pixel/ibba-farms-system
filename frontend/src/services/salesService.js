import api from './api';

export const salesService = {
  recordSale: async (data) => {
    const response = await api.post('/sales', data);
    return response.data;
  },

  getSales: async (filters = {}) => {
    const response = await api.get('/sales', { params: filters });
    return response.data;
  },

  getSaleById: async (id) => {
    const response = await api.get(`/sales/${id}`);
    return response.data;
  },

  updateSale: async (id, data) => {
    const response = await api.put(`/sales/${id}`, data);
    return response.data;
  },

  deleteSale: async (id) => {
    await api.delete(`/sales/${id}`);
  },

  getDailyStats: async (dateFrom, dateTo) => {
    const response = await api.get('/sales/stats/daily', {
      params: { date_from: dateFrom, date_to: dateTo },
    });
    return response.data;
  },
};
