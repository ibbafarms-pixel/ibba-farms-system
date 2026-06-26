# IBBA Farms Management System - API Specification

## Overview

This document provides complete API specification for the IBBA Farms Management System. The API is built with FastAPI and follows RESTful principles.

**Base URL**: `https://api.ibba-farms.com/v1`

**Authentication**: JWT Bearer Token (required for most endpoints)

---

## Table of Contents

1. [Authentication](#authentication)
2. [Production Recording](#production-recording)
3. [Egg Sales](#egg-sales)
4. [Expense Recording](#expense-recording)
5. [Feed Inventory](#feed-inventory)
6. [Dashboard](#dashboard)
7. [Error Handling](#error-handling)
8. [Rate Limiting](#rate-limiting)

---

## Authentication

### POST /auth/login

Authenticate user and receive JWT token.

**Request**
```json
{
  "email": "admin@ibba-farms.com",
  "password": "secure_password_123"
}
```

**Response (200 OK)**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "uuid",
    "email": "admin@ibba-farms.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "admin"
  }
}
```

**Error Responses**
- 400: Invalid credentials
- 401: User not found
- 429: Too many login attempts

---

### POST /auth/logout

Invalidate current session token.

**Headers**
```
Authorization: Bearer <token>
```

**Response (200 OK)**
```json
{
  "message": "Successfully logged out"
}
```

---

### POST /auth/refresh-token

Refresh expired access token.

**Request**
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response (200 OK)**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 3600
}
```

---

### GET /auth/me

Get current authenticated user information.

**Headers**
```
Authorization: Bearer <token>
```

**Response (200 OK)**
```json
{
  "id": "uuid",
  "email": "admin@ibba-farms.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "admin",
  "created_at": "2026-06-26T10:00:00Z",
  "last_login": "2026-06-26T14:30:00Z"
}
```

---

## Production Recording

### POST /production

Record daily production data.

**Headers**
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request**
```json
{
  "date": "2026-06-26",
  "house": "Layer 1",
  "number_of_birds": 1200,
  "eggs_collected": 1120,
  "broken_eggs": 15,
  "cracked_eggs": 5,
  "mortality": 0,
  "birds_culled": 0,
  "water_consumption_liters": 450,
  "feed_used_kg": 145.5,
  "notes": "Normal production day"
}
```

**Response (201 Created)**
```json
{
  "id": "uuid",
  "date": "2026-06-26",
  "house": "Layer 1",
  "number_of_birds": 1200,
  "eggs_collected": 1120,
  "broken_eggs": 15,
  "cracked_eggs": 5,
  "good_eggs": 1100,
  "mortality": 0,
  "birds_culled": 0,
  "water_consumption_liters": 450,
  "feed_used_kg": 145.5,
  "production_percentage": 93.33,
  "notes": "Normal production day",
  "created_at": "2026-06-26T10:30:00Z",
  "updated_at": "2026-06-26T10:30:00Z"
}
```

**Error Responses**
- 400: Invalid data
- 409: Record already exists for this date/house

---

### GET /production

List all production records with filtering and pagination.

**Query Parameters**
```
date_from=2026-06-01
date_to=2026-06-30
house=Layer 1
page=1
per_page=20
```

**Response (200 OK)**
```json
{
  "data": [
    {
      "id": "uuid",
      "date": "2026-06-26",
      "house": "Layer 1",
      "number_of_birds": 1200,
      "eggs_collected": 1120,
      "production_percentage": 93.33,
      "created_at": "2026-06-26T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 26,
    "pages": 2
  }
}
```

---

### GET /production/{id}

Get specific production record.

**Response (200 OK)**
```json
{
  "id": "uuid",
  "date": "2026-06-26",
  "house": "Layer 1",
  "number_of_birds": 1200,
  "eggs_collected": 1120,
  "broken_eggs": 15,
  "cracked_eggs": 5,
  "good_eggs": 1100,
  "mortality": 0,
  "birds_culled": 0,
  "water_consumption_liters": 450,
  "feed_used_kg": 145.5,
  "production_percentage": 93.33,
  "notes": "Normal production day",
  "created_at": "2026-06-26T10:30:00Z",
  "updated_at": "2026-06-26T10:30:00Z"
}
```

---

### PUT /production/{id}

Update production record (admin/manager only).

**Request** (same structure as POST)

**Response (200 OK)** (same structure as GET)

---

### DELETE /production/{id}

Delete production record (admin only).

**Response (204 No Content)**

---

### GET /production/stats/daily

Get daily production statistics.

**Query Parameters**
```
date_from=2026-06-01
date_to=2026-06-30
```

**Response (200 OK)**
```json
{
  "date": "2026-06-26",
  "total_eggs_collected": 2240,
  "total_broken_eggs": 30,
  "total_good_eggs": 2210,
  "total_mortality": 0,
  "total_birds_live": 2400,
  "average_production_percentage": 93.33,
  "total_feed_used_kg": 291,
  "total_water_consumption_liters": 900,
  "records_count": 2
}
```

---

## Egg Sales

### POST /sales

Record egg sale.

**Request**
```json
{
  "customer_id": "uuid",
  "date": "2026-06-26",
  "trays": 32,
  "loose_eggs": 4500,
  "price_per_unit": 4500,
  "payment_method": "cash",
  "paid": true,
  "invoice_number": "INV-2026-0001",
  "notes": "Regular customer, on credit"
}
```

**Response (201 Created)**
```json
{
  "id": "uuid",
  "customer_id": "uuid",
  "customer_name": "John",
  "date": "2026-06-26",
  "trays": 32,
  "loose_eggs": 4500,
  "total_eggs": 40500,
  "price_per_unit": 4500,
  "total_revenue": 144000,
  "payment_method": "cash",
  "paid": true,
  "invoice_number": "INV-2026-0001",
  "notes": "Regular customer, on credit",
  "created_at": "2026-06-26T15:00:00Z"
}
```

---

### GET /sales

List all sales records.

**Query Parameters**
```
date_from=2026-06-01
date_to=2026-06-30
customer_id=uuid
paid=true
page=1
per_page=20
```

**Response (200 OK)**
```json
{
  "data": [
    {
      "id": "uuid",
      "customer_name": "John",
      "date": "2026-06-26",
      "total_eggs": 40500,
      "total_revenue": 144000,
      "paid": true,
      "invoice_number": "INV-2026-0001"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 45,
    "pages": 3
  },
  "summary": {
    "total_revenue": 1500000,
    "paid_revenue": 1350000,
    "outstanding_revenue": 150000
  }
}
```

---

### GET /sales/stats/daily

Get daily sales statistics.

**Response (200 OK)**
```json
{
  "date": "2026-06-26",
  "total_sales": 5,
  "total_eggs_sold": 202500,
  "total_revenue": 720000,
  "paid_amount": 650000,
  "outstanding_amount": 70000,
  "average_price_per_tray": 4500,
  "paid_percentage": 90.28
}
```

---

## Expense Recording

### POST /expenses

Record expense.

**Request**
```json
{
  "category": "feed",
  "supplier_id": "uuid",
  "date": "2026-06-26",
  "amount": 92800,
  "currency": "RWF",
  "description": "Feed purchase - 145kg",
  "invoice_number": "SUP-2026-001",
  "payment_method": "cash",
  "paid": true,
  "notes": "Quality feed"
}
```

**Response (201 Created)**
```json
{
  "id": "uuid",
  "category": "feed",
  "supplier_name": "Farm Supplies Ltd",
  "date": "2026-06-26",
  "amount": 92800,
  "currency": "RWF",
  "description": "Feed purchase - 145kg",
  "invoice_number": "SUP-2026-001",
  "payment_method": "cash",
  "paid": true,
  "notes": "Quality feed",
  "created_at": "2026-06-26T16:00:00Z"
}
```

---

### GET /expenses

List all expenses with filtering.

**Query Parameters**
```
date_from=2026-06-01
date_to=2026-06-30
category=feed
paid=true
page=1
per_page=20
```

**Response (200 OK)**
```json
{
  "data": [
    {
      "id": "uuid",
      "category": "feed",
      "supplier_name": "Farm Supplies Ltd",
      "date": "2026-06-26",
      "amount": 92800,
      "paid": true
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 30,
    "pages": 2
  },
  "summary_by_category": {
    "feed": 1856000,
    "vaccines": 150000,
    "electricity": 75000,
    "labour": 300000,
    "other": 125000
  },
  "total_expenses": 2506000
}
```

---

### GET /expenses/by-category

Get expense summary by category.

**Query Parameters**
```
date_from=2026-06-01
date_to=2026-06-30
```

**Response (200 OK)**
```json
{
  "period": {
    "from": "2026-06-01",
    "to": "2026-06-30"
  },
  "categories": [
    {
      "category": "feed",
      "total": 1856000,
      "percentage": 74.1,
      "count": 26
    },
    {
      "category": "labour",
      "total": 300000,
      "percentage": 11.96,
      "count": 4
    },
    {
      "category": "electricity",
      "total": 75000,
      "percentage": 3.0,
      "count": 1
    },
    {
      "category": "vaccines",
      "total": 150000,
      "percentage": 5.98,
      "count": 2
    },
    {
      "category": "other",
      "total": 125000,
      "percentage": 4.98,
      "count": 8
    }
  ],
  "total": 2506000
}
```

---

## Feed Inventory

### POST /feed/purchase

Record feed purchase and update inventory.

**Request**
```json
{
  "supplier_id": "uuid",
  "date": "2026-06-26",
  "quantity_kg": 1000,
  "price_per_kg": 640,
  "total_cost": 640000,
  "invoice_number": "FEED-001",
  "notes": "High quality feed"
}
```

**Response (201 Created)**
```json
{
  "id": "uuid",
  "supplier_name": "Farm Supplies Ltd",
  "date": "2026-06-26",
  "quantity_kg": 1000,
  "price_per_kg": 640,
  "total_cost": 640000,
  "invoice_number": "FEED-001",
  "notes": "High quality feed",
  "current_stock_kg": 7245,
  "previous_stock_kg": 6245,
  "created_at": "2026-06-26T09:00:00Z"
}
```

---

### GET /feed/inventory

Get current feed inventory status.

**Response (200 OK)**
```json
{
  "current_stock_kg": 7245,
  "minimum_threshold_kg": 2000,
  "low_stock_alert": false,
  "average_daily_consumption_kg": 145,
  "estimated_days_remaining": 49.97,
  "last_purchase": {
    "date": "2026-06-26",
    "quantity_kg": 1000,
    "price_per_kg": 640
  },
  "average_cost_per_kg": 637.5,
  "total_cost_in_stock": 4618387.5
}
```

---

### GET /feed/transactions

Get feed transaction history.

**Query Parameters**
```
type=purchase|consumption
date_from=2026-06-01
date_to=2026-06-30
page=1
per_page=50
```

**Response (200 OK)**
```json
{
  "data": [
    {
      "id": "uuid",
      "type": "purchase",
      "date": "2026-06-26",
      "quantity_kg": 1000,
      "price_per_kg": 640,
      "stock_after_kg": 7245,
      "reference": "FEED-001"
    },
    {
      "id": "uuid",
      "type": "consumption",
      "date": "2026-06-26",
      "quantity_kg": 145,
      "from_production_record": "uuid",
      "stock_after_kg": 7100
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 50,
    "total": 156
  }
}
```

---

### PUT /feed/threshold

Update feed minimum threshold for alerts.

**Request**
```json
{
  "minimum_threshold_kg": 2500
}
```

**Response (200 OK)**
```json
{
  "minimum_threshold_kg": 2500,
  "current_stock_kg": 7245,
  "alert_active": false,
  "message": "Threshold updated successfully"
}
```

---

## Dashboard

### GET /dashboard/overview

Get main dashboard overview for today.

**Response (200 OK)**
```json
{
  "date": "2026-06-26",
  "production": {
    "eggs_produced": 3240,
    "eggs_sold": 2900,
    "production_percentage": 93.3,
    "broken_eggs": 30,
    "mortality": 0
  },
  "financial": {
    "revenue": 435000,
    "feed_cost": 92800,
    "other_expenses": 8500,
    "total_expenses": 101300,
    "profit": 333700
  },
  "inventory": {
    "current_birds": 1184,
    "feed_remaining_kg": 6245,
    "low_stock_alert": false
  },
  "trends": {
    "production_trend": "up",
    "revenue_trend": "up",
    "profit_trend": "stable"
  }
}
```

---

### GET /dashboard/charts

Get data for dashboard charts.

**Query Parameters**
```
days=30
```

**Response (200 OK)**
```json
{
  "production_chart": [
    {
      "date": "2026-05-27",
      "eggs_produced": 3100,
      "production_percentage": 91.2
    },
    {
      "date": "2026-05-28",
      "eggs_produced": 3150,
      "production_percentage": 92.5
    }
  ],
  "revenue_chart": [
    {
      "date": "2026-05-27",
      "revenue": 419000
    }
  ],
  "feed_consumption_chart": [
    {
      "date": "2026-05-27",
      "feed_used_kg": 142,
      "cost": 90880
    }
  ],
  "profit_chart": [
    {
      "date": "2026-05-27",
      "profit": 310000
    }
  ],
  "summary": {
    "avg_daily_production": 3150,
    "avg_daily_revenue": 430000,
    "total_monthly_profit": 8100000,
    "avg_production_percentage": 92.8
  }
}
```

---

## Error Handling

All errors follow this format:

**Error Response**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ],
    "timestamp": "2026-06-26T10:30:00Z",
    "request_id": "req-uuid"
  }
}
```

**Common Error Codes**
- `VALIDATION_ERROR` (400): Invalid input data
- `UNAUTHORIZED` (401): Missing or invalid authentication token
- `FORBIDDEN` (403): Insufficient permissions
- `NOT_FOUND` (404): Resource not found
- `CONFLICT` (409): Resource already exists
- `RATE_LIMITED` (429): Too many requests
- `INTERNAL_ERROR` (500): Server error

---

## Rate Limiting

- **Standard Rate Limit**: 1000 requests per hour per user
- **Login Endpoint**: 10 requests per 5 minutes per IP
- **Report Generation**: 100 requests per hour per user

**Rate Limit Headers**
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 987
X-RateLimit-Reset: 1624704600
```

---

*API Version: 1.0.0*
*Last Updated: 2026-06-26*