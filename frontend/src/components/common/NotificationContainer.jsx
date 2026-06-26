import React from 'react';
import { useNotification } from '../../context/NotificationContext';
import { X } from 'lucide-react';

const Notification = ({ id, message, type }) => {
  const { removeNotification } = useNotification();

  return (
    <div className={`alert alert--${type}`}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span>{message}</span>
        <button
          onClick={() => removeNotification(id)}
          style={{ background: 'none', border: 'none', cursor: 'pointer' }}
        >
          <X size={18} />
        </button>
      </div>
    </div>
  );
};

const NotificationContainer = () => {
  const { notifications } = useNotification();

  return (
    <div style={{ position: 'fixed', top: 70, right: 20, zIndex: 1000, maxWidth: '400px' }}>
      {notifications.map((notif) => (
        <Notification key={notif.id} {...notif} />
      ))}
    </div>
  );
};

export default NotificationContainer;
