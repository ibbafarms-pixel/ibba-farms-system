import React from 'react';
import { useNavigate } from 'react-router-dom';

const NotFoundPage = () => {
  const navigate = useNavigate();

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: '#f9fafb',
      }}
    >
      <h1 style={{ fontSize: '3rem', fontWeight: '700', marginBottom: '0.5rem' }}>404</h1>
      <p style={{ fontSize: '1.5rem', color: '#6b7280', marginBottom: '2rem' }}>Page Not Found</p>
      <button className="btn btn--primary" onClick={() => navigate('/dashboard')}>
        Go to Dashboard
      </button>
    </div>
  );
};

export default NotFoundPage;
