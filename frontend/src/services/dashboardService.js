import api from './api';

export const dashboardService = {
  getOverview: async () => {
    const response = await api.get('/dashboard/overview');
    return response.data;
  },

  getCharts: async (days = 30) => {
    const response = await api.get('/dashboard/charts', { params: { days } });
    return response.data;
  },
};
