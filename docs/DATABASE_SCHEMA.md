# IBBA Farms Management System - Database Schema

## Overview

This document defines the PostgreSQL database schema for the IBBA Farms Management System.

**Database Engine**: PostgreSQL 12+
**Connection Pooling**: pgBouncer
**Backup Strategy**: Daily backups with 30-day retention

---

## Table of Contents

1. [Core Tables](#core-tables)
2. [Production Module](#production-module)
3. [Sales Module](#sales-module)
4. [Expense Module](#expense-module)
5. [Feed Inventory Module](#feed-inventory-module)
6. [User Management](#user-management)
7. [Indexes & Performance](#indexes--performance)

---

## Core Tables

### users

Stores user account information.

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'manager', 'worker', 'accountant')),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  last_login TIMESTAMP WITH TIME ZONE,
  deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_is_active ON users(is_active);
```

---

### houses

Defines physical poultry houses.

```sql
CREATE TABLE houses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL UNIQUE,
  capacity INT NOT NULL,
  description TEXT,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_houses_is_active ON houses(is_active);
```

---

## Production Module

### production_records

Daily egg production data per house.

```sql
CREATE TABLE production_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  date DATE NOT NULL,
  house_id UUID NOT NULL REFERENCES houses(id),
  number_of_birds INT NOT NULL CHECK (number_of_birds > 0),
  eggs_collected INT NOT NULL CHECK (eggs_collected >= 0),
  broken_eggs INT NOT NULL DEFAULT 0 CHECK (broken_eggs >= 0),
  cracked_eggs INT NOT NULL DEFAULT 0 CHECK (cracked_eggs >= 0),
  good_eggs INT GENERATED ALWAYS AS (eggs_collected - broken_eggs - cracked_eggs) STORED,
  mortality INT NOT NULL DEFAULT 0 CHECK (mortality >= 0),
  birds_culled INT NOT NULL DEFAULT 0 CHECK (birds_culled >= 0),
  water_consumption_liters INT NOT NULL DEFAULT 0 CHECK (water_consumption_liters >= 0),
  feed_used_kg DECIMAL(8,2) NOT NULL CHECK (feed_used_kg >= 0),
  production_percentage DECIMAL(5,2) GENERATED ALWAYS AS 
    (CASE WHEN number_of_birds > 0 THEN (eggs_collected::DECIMAL / number_of_birds * 100) ELSE 0 END) STORED,
  notes TEXT,
  recorded_by UUID NOT NULL REFERENCES users(id),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(date, house_id)
);

CREATE INDEX idx_production_date ON production_records(date);
CREATE INDEX idx_production_house_id ON production_records(house_id);
CREATE INDEX idx_production_recorded_by ON production_records(recorded_by);
CREATE INDEX idx_production_date_house ON production_records(date, house_id);
```

---

## Sales Module

### customers

Stores customer information.

```sql
CREATE TABLE customers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  email VARCHAR(255),
  location VARCHAR(255),
  contact_person VARCHAR(255),
  credit_limit DECIMAL(15,2) NOT NULL DEFAULT 0,
  current_balance DECIMAL(15,2) NOT NULL DEFAULT 0,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_customers_name ON customers(name);
CREATE INDEX idx_customers_phone ON customers(phone);
CREATE INDEX idx_customers_is_active ON customers(is_active);
```

---

### sales_records

Egg sales transactions.

```sql
CREATE TABLE sales_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id UUID NOT NULL REFERENCES customers(id),
  date DATE NOT NULL,
  trays INT NOT NULL CHECK (trays >= 0),
  loose_eggs INT NOT NULL DEFAULT 0 CHECK (loose_eggs >= 0),
  total_eggs INT GENERATED ALWAYS AS (trays * 30 + loose_eggs) STORED,
  price_per_unit INT NOT NULL CHECK (price_per_unit > 0),
  total_revenue DECIMAL(15,2) GENERATED ALWAYS AS 
    ((trays * 30 + loose_eggs) * price_per_unit) STORED,
  payment_method VARCHAR(50) NOT NULL CHECK (payment_method IN ('cash', 'check', 'mobile_money', 'bank_transfer', 'credit')),
  paid BOOLEAN NOT NULL DEFAULT false,
  invoice_number VARCHAR(100) UNIQUE,
  notes TEXT,
  recorded_by UUID NOT NULL REFERENCES users(id),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_sales_customer_id ON sales_records(customer_id);
CREATE INDEX idx_sales_date ON sales_records(date);
CREATE INDEX idx_sales_paid ON sales_records(paid);
CREATE INDEX idx_sales_recorded_by ON sales_records(recorded_by);
CREATE INDEX idx_sales_date_customer ON sales_records(date, customer_id);
```

---

## Expense Module

### suppliers

Stores supplier information.

```sql
CREATE TABLE suppliers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL UNIQUE,
  phone VARCHAR(20),
  email VARCHAR(255),
  contact_person VARCHAR(255),
  specialization VARCHAR(100),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_suppliers_name ON suppliers(name);
CREATE INDEX idx_suppliers_is_active ON suppliers(is_active);
```

---

### expense_records

Tracking of all farm expenses.

```sql
CREATE TABLE expense_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  category VARCHAR(50) NOT NULL CHECK (category IN ('feed', 'vaccines', 'fuel', 'electricity', 'labour', 'repairs', 'transport', 'packaging', 'medicine', 'water', 'internet', 'phone', 'other')),
  supplier_id UUID REFERENCES suppliers(id),
  date DATE NOT NULL,
  amount DECIMAL(15,2) NOT NULL CHECK (amount > 0),
  currency VARCHAR(3) NOT NULL DEFAULT 'RWF',
  description TEXT,
  invoice_number VARCHAR(100),
  payment_method VARCHAR(50) NOT NULL CHECK (payment_method IN ('cash', 'check', 'mobile_money', 'bank_transfer')),
  paid BOOLEAN NOT NULL DEFAULT false,
  notes TEXT,
  recorded_by UUID NOT NULL REFERENCES users(id),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_expenses_category ON expense_records(category);
CREATE INDEX idx_expenses_date ON expense_records(date);
CREATE INDEX idx_expenses_supplier_id ON expense_records(supplier_id);
CREATE INDEX idx_expenses_paid ON expense_records(paid);
CREATE INDEX idx_expenses_category_date ON expense_records(category, date);
```

---

## Feed Inventory Module

### feed_inventory

Current feed stock levels.

```sql
CREATE TABLE feed_inventory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  current_stock_kg DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (current_stock_kg >= 0),
  minimum_threshold_kg DECIMAL(10,2) NOT NULL DEFAULT 2000,
  average_cost_per_kg DECIMAL(10,2),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

---

### feed_transactions

All feed purchase and consumption transactions.

```sql
CREATE TABLE feed_transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  type VARCHAR(20) NOT NULL CHECK (type IN ('purchase', 'consumption')),
  date DATE NOT NULL,
  quantity_kg DECIMAL(10,2) NOT NULL CHECK (quantity_kg > 0),
  price_per_kg DECIMAL(10,2),
  total_cost DECIMAL(15,2),
  stock_before_kg DECIMAL(10,2) NOT NULL,
  stock_after_kg DECIMAL(10,2) NOT NULL,
  reference_type VARCHAR(50),
  reference_id UUID,
  supplier_id UUID REFERENCES suppliers(id),
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT valid_purchase_fields CHECK (
    (type = 'purchase' AND price_per_kg IS NOT NULL AND supplier_id IS NOT NULL) OR
    (type = 'consumption' AND price_per_kg IS NULL)
  )
);

CREATE INDEX idx_feed_trans_type ON feed_transactions(type);
CREATE INDEX idx_feed_trans_date ON feed_transactions(date);
CREATE INDEX idx_feed_trans_reference ON feed_transactions(reference_id);
CREATE INDEX idx_feed_trans_date_type ON feed_transactions(date, type);
```

---

## Audit & Logging

### audit_logs

Track all critical changes for compliance.

```sql
CREATE TABLE audit_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  action VARCHAR(100) NOT NULL,
  entity_type VARCHAR(100) NOT NULL,
  entity_id UUID NOT NULL,
  old_values JSONB,
  new_values JSONB,
  ip_address VARCHAR(45),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_audit_user_id ON audit_logs(user_id);
CREATE INDEX idx_audit_entity ON audit_logs(entity_type, entity_id);
CREATE INDEX idx_audit_created_at ON audit_logs(created_at);
```

---

## Indexes & Performance

### Critical Indexes for Query Performance

```sql
-- Multi-column indexes for common queries
CREATE INDEX idx_production_house_date ON production_records(house_id, date DESC);
CREATE INDEX idx_sales_customer_date ON sales_records(customer_id, date DESC);
CREATE INDEX idx_expenses_category_date ON expense_records(category, date DESC);

-- Partial indexes for active records
CREATE INDEX idx_users_active ON users(id) WHERE is_active = true;
CREATE INDEX idx_customers_active ON customers(id) WHERE is_active = true;
CREATE INDEX idx_suppliers_active ON suppliers(id) WHERE is_active = true;

-- Indexes for date range queries
CREATE INDEX idx_production_date_range ON production_records(date) WHERE deleted_at IS NULL;
CREATE INDEX idx_sales_date_range ON sales_records(date) WHERE deleted_at IS NULL;
CREATE INDEX idx_expenses_date_range ON expense_records(date) WHERE deleted_at IS NULL;
```

---

### Views for Common Queries

```sql
-- Daily production summary
CREATE VIEW v_daily_production_summary AS
SELECT
  date,
  COUNT(*) as records_count,
  SUM(eggs_collected) as total_eggs_collected,
  SUM(broken_eggs) as total_broken_eggs,
  SUM(good_eggs) as total_good_eggs,
  SUM(mortality) as total_mortality,
  SUM(feed_used_kg) as total_feed_used_kg,
  AVG(production_percentage) as avg_production_percentage
FROM production_records
GROUP BY date
ORDER BY date DESC;

-- Daily sales summary
CREATE VIEW v_daily_sales_summary AS
SELECT
  date,
  COUNT(*) as sales_count,
  SUM(total_eggs) as total_eggs_sold,
  SUM(total_revenue) as total_revenue,
  SUM(CASE WHEN paid = true THEN total_revenue ELSE 0 END) as paid_amount,
  SUM(CASE WHEN paid = false THEN total_revenue ELSE 0 END) as outstanding_amount
FROM sales_records
GROUP BY date
ORDER BY date DESC;

-- Daily expense summary
CREATE VIEW v_daily_expense_summary AS
SELECT
  date,
  category,
  COUNT(*) as expense_count,
  SUM(amount) as total_amount
FROM expense_records
GROUP BY date, category
ORDER BY date DESC;

-- Customer outstanding balance
CREATE VIEW v_customer_balances AS
SELECT
  c.id,
  c.name,
  c.phone,
  c.credit_limit,
  SUM(CASE WHEN sr.paid = false THEN sr.total_revenue ELSE 0 END) as outstanding_balance,
  MAX(sr.date) as last_sale_date
FROM customers c
LEFT JOIN sales_records sr ON c.id = sr.customer_id
WHERE c.is_active = true
GROUP BY c.id, c.name, c.phone, c.credit_limit;
```

---

### Constraints & Data Integrity

```sql
-- Foreign key constraints for referential integrity
ALTER TABLE production_records 
  ADD CONSTRAINT fk_production_house 
  FOREIGN KEY (house_id) REFERENCES houses(id) ON DELETE RESTRICT;

ALTER TABLE sales_records 
  ADD CONSTRAINT fk_sales_customer 
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE RESTRICT;

ALTER TABLE expense_records 
  ADD CONSTRAINT fk_expense_supplier 
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE SET NULL;

-- Check constraints for data validation
ALTER TABLE customers
  ADD CONSTRAINT check_credit_limit CHECK (credit_limit >= 0),
  ADD CONSTRAINT check_balance CHECK (current_balance >= 0);
```

---

### Maintenance & Optimization

```sql
-- Vacuum and analyze for optimal performance
VACUUM ANALYZE production_records;
VACUUM ANALYZE sales_records;
VACUUM ANALYZE expense_records;

-- Monitor table sizes
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

---

*Database Version: PostgreSQL 12+*
*Last Updated: 2026-06-26*