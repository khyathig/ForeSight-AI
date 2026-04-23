# ForeSight AI  
### Smart Retail Demand Intelligence Platform

ForeSight AI is a full-stack analytics project that helps retailers make smarter inventory decisions by combining **historical sales patterns, customer feedback, external trends, events, and policy signals** into one interactive dashboard.

The goal of the project is to move beyond static reports and demonstrate how businesses can use data + machine learning to make proactive stocking decisions.

> Built as a practical retail intelligence prototype using React, Flask, Pandas, and forecasting models.

---

## 🚀 Key Features

### 📊 Executive Dashboard
An interactive dashboard that visualizes demand and inventory insights through charts and reports.

Includes:
- Demand vs Available Inventory
- Forecasted Demand Trends
- Inventory Action Distribution
- KPI Cards for stock recommendations
- Product-level recommendations

---

### 📈 Demand Forecasting
Uses time-series forecasting techniques on historical order data to estimate future demand.

Forecasting output helps answer:
- Which products may face stockouts?
- Which products are overstocked?
- Where should inventory be increased or reduced?

---

### 💬 Customer Feedback Intelligence
Transforms ratings into actionable inventory decisions.

Example:
- High ratings → Increase inventory
- Low ratings → Reduce inventory
- Neutral ratings → Maintain inventory

This creates a direct connection between customer satisfaction and supply planning.

---

### 🌍 External Trend Signals
The system experiments with real-world signals such as:
- Search trends
- Public interest spikes
- Social demand signals

These signals can help detect emerging product demand before it appears in internal sales data.

---

### 🎉 Event-Based Demand Planning
Local or regional events can temporarily change demand patterns.

Examples:
- Festivals
- Sports events
- Community gatherings
- Seasonal demand spikes

The system maps events to affected categories and recommends inventory actions.

---

### 🏛️ Policy / Geopolitical Impact Awareness
External changes such as regulations, taxes, import restrictions, or packaging rules can affect supply and demand.

The project includes a module to simulate how such signals can influence stocking strategies.

---

## 🛠️ Tech Stack

### Frontend
- React.js
- Recharts
- Axios
- CSS / Inline Styling

### Backend
- Flask
- Flask-CORS
- Pandas
- NumPy

### ML / Analytics
- Prophet (Time Series Forecasting)
- Rule-based Decision Logic
- Data Aggregation using Pandas

---

## 📂 Project Structure

```bash
ForeSight-AI/
│
├── backend/
│   ├── app.py
│   ├── model/
│   │   ├── forecast.py
│   │   └── rules.py
│   ├── utils/
│   │   └── trends.py
│   └── data/
│       ├── blinkit_orders.csv
│       ├── blinkit_order_items.csv
│       ├── blinkit_products.csv
│       ├── blinkit_inventory.csv
│       ├── blinkit_customer_feedback.csv
│       ├── events.csv
│       └── policy_impact.csv
│
├── frontend/
│   └── src/
│       ├── App.js
│       ├── pages/
│       │   ├── Dashboard.js
│       │   ├── Feedback.js
│       │   ├── Events.js
│       │   ├── Policies.js
│       │   └── SocialTrends.js
│       └── services/
│           └── api.js
│
└── README.md
