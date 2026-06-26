import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BarChart3, ShoppingCart, TrendingUp, Package, FileText, Settings } from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();

  const menuItems = [
    { icon: BarChart3, label: 'Dashboard', path: '/dashboard' },
    { icon: TrendingUp, label: 'Production', path: '/production' },
    { icon: ShoppingCart, label: 'Sales', path: '/sales' },
    { icon: Package, label: 'Expenses', path: '/expenses' },
    { icon: Package, label: 'Feed', path: '/feed' },
    { icon: FileText, label: 'Reports', path: '/reports' },
    { icon: Settings, label: 'Settings', path: '/settings' },
  ];

  return (
    <aside className="sidebar">
      {menuItems.map((item) => {
        const Icon = item.icon;
        const isActive = location.pathname === item.path;
        return (
          <Link
            key={item.path}
            to={item.path}
            className={`sidebar__item ${isActive ? 'active' : ''}`}
          >
            <Icon size={20} style={{ marginRight: '0.5rem' }} />
            {item.label}
          </Link>
        );
      })}
    </aside>
  );
};

export default Sidebar;
