import React, { useEffect, useState } from 'react';
import Header from '../components/common/Header';
import Sidebar from '../components/common/Sidebar';
import NotificationContainer from '../components/common/NotificationContainer';
import Loading from '../components/common/Loading';
import { dashboardService } from '../services/dashboardService';
import { useNotification } from '../context/NotificationContext';

const DashboardPage = () => {
  const [overview, setOverview] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const { addNotification } = useNotification();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await dashboardService.getOverview();
        setOverview(data);
      } catch (error) {
        addNotification('Failed to load dashboard', 'error');
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [addNotification]);

  if (isLoading) {
    return (
      <>
        <Header />
        <Sidebar />
        <div className="main">
          <Loading />
        </div>
      </>
    );
  }

  return (
    <>
      <Header />
      <Sidebar />
      <NotificationContainer />
      <div className="main">
        <h1>Dashboard</h1>
        <p style={{ color: '#6b7280', marginTop: '0.5rem' }}>Welcome to IBBA Farms Management System</p>

        {overview && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', marginTop: '2rem' }}>
            <div className="card">
              <h3 style={{ color: '#6b7280', fontSize: '0.875rem', fontWeight: '500' }}>Eggs Produced</h3>
              <p style={{ fontSize: '2rem', fontWeight: '700', marginTop: '0.5rem' }}>
                {overview.production?.eggs_produced || 0}
              </p>
            </div>

            <div className="card">
              <h3 style={{ color: '#6b7280', fontSize: '0.875rem', fontWeight: '500' }}>Revenue (RWF)</h3>
              <p style={{ fontSize: '2rem', fontWeight: '700', marginTop: '0.5rem' }}>
                {(overview.financial?.revenue || 0).toLocaleString()}
              </p>
            </div>

            <div className="card">
              <h3 style={{ color: '#6b7280', fontSize: '0.875rem', fontWeight: '500' }}>Daily Profit (RWF)</h3>
              <p style={{ fontSize: '2rem', fontWeight: '700', marginTop: '0.5rem', color: '#10b981' }}>
                {(overview.financial?.profit || 0).toLocaleString()}
              </p>
            </div>

            <div className="card">
              <h3 style={{ color: '#6b7280', fontSize: '0.875rem', fontWeight: '500' }}>Current Birds</h3>
              <p style={{ fontSize: '2rem', fontWeight: '700', marginTop: '0.5rem' }}>
                {overview.inventory?.current_birds || 0}
              </p>
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default DashboardPage;
