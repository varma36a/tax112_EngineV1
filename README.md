
# Tax 1120 AI Advisor System

## Overview

The Tax 1120 AI Advisor System is an end-to-end enterprise-grade tax intelligence platform designed to automate:

* Trial Balance (TB) ingestion
* Account classification under IRS Form 1120 categories
* Tax adjustment and deduction logic
* Legal tax-saving recommendations
* Prior Year (PY) vs Current Year (CY) tax comparison
* Explainable AI dashboards
* Financial analytics for customer engagement

This project combines:

* **FastAPI Backend** for tax engine + ML APIs
* **Angular Frontend** for interactive dashboards
* **XGBoost + TF-IDF ML Model** for account classification
* **Rule-Based Tax Engine** for IRS compliance
* **Explainability Layer** for model transparency

---

# Core Features

## 1. Trial Balance Upload

Users upload CSV/Excel trial balance files containing:

* Account Name
* Debit
* Credit

### Example:

| account_name    | debit  | credit |
| --------------- | ------ | ------ |
| Sales Revenue   | 0      | 500000 |
| Office Rent     | 20000  | 0      |
| Employee Salary | 100000 | 0      |

---

## 2. AI Account Classification

The system classifies accounts into:

* income
* expense
* meals
* penalty
* depreciation
* charity
* cogs
* asset
* non_deductible

### ML Stack:

* TF-IDF Vectorizer
* XGBoost Classifier
* Confidence Scoring
* Fallback to `review_needed`

---

## 3. Tax Rule Engine

IRS-inspired legal tax logic:

### Examples:

* Meals → 50% deductible
* Penalties → Non-deductible
* Charity → Limited deductibility
* Expenses → Fully deductible

---

## 4. Form 1120 Tax Calculation

Automatically computes:

* Gross Receipts
* Deductions
* Taxable Income
* Federal Tax Liability

---

## 5. AI Tax Advisor

Provides recommendations such as:

* Expense optimization opportunities
* Non-deductible account alerts
* Low-confidence account review flags
* Tax savings suggestions

### Example:

> “Client Meals are only 50% deductible. Consider reclassification where legally applicable.”

---

## 6. PY vs CY Comparison

Compares:

* Tax liability changes
* Deduction improvements
* Profitability shifts
* Savings opportunities

---

## 7. Explainability Dashboard

Displays:

* Accuracy
* Precision
* Recall
* F1 Score
* Top predictive features
* Category-level model performance

---

# Project Architecture

```text
Frontend (Angular)
   |
   | Upload TB / Dashboard Requests
   v
Backend (FastAPI)
   |
   |--> TB Parser
   |--> ML Classifier (XGBoost)
   |--> Tax Rule Engine
   |--> Form 1120 Generator
   |--> Advisor Engine
   |--> Explainability Engine
   v
Dashboard Response
```

---

# Repository Structure

```text
tax-1120-ai/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   └── tax.py
│   │   ├── services/
│   │   │   ├── tb_parser.py
│   │   │   ├── classifier.py
│   │   │   ├── tax_engine.py
│   │   │   ├── form1120.py
│   │   │   ├── advisor.py
│   │   │   ├── explainer.py
│   │   │   ├── explainability.py
│   │   │   └── comparison.py
│   │   └── ml/
│   │       ├── xgb_model.pkl
│   │       ├── vectorizer.pkl
│   │       ├── label_encoder.pkl
│   │       └── model_metrics.json
│   ├── data/
│   │   └── training_data.csv
│   ├── train_model.py
│   └── requirements.txt
│
└── frontend/
    └── tax-widget/
        ├── src/app/
        │   ├── app.component.ts
        │   ├── app.component.html
        │   ├── app.component.scss
        │   ├── app.module.ts
        │   └── tax.service.ts
        └── package.json
```

---

# Installation Guide

## Backend Setup

```bash
cd backend
conda create -n tax1120 python=3.11 -y
conda activate tax1120
pip install -r requirements.txt
```

### Train Model:

```bash
python train_model.py
```

### Run Backend:

```bash
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend/tax-widget
npm install
npm install chart.js
npm install --save-dev @types/chart.js
ng serve
```

Frontend URL:

```text
http://localhost:4200
```

---

# Key API Endpoints

## Upload Trial Balance

```http
POST /upload-tb
```

### Returns:

* Tax Result
* Classified Accounts
* Preview Table
* Category Breakdown
* Advisor Insights

---

## Explainability Metrics

```http
GET /explainability
```

### Returns:

* Model Accuracy
* Macro Avg
* Weighted Avg
* Feature Importance
* Class Metrics

---

# Model Performance

### Current Baseline:

* Accuracy: ~98%
* Macro F1: ~97%
* Weighted F1: ~98%

### Limitations:

* Synthetic training bias
* Real-world account diversity may reduce accuracy
* Rule engine remains critical for production compliance

---

# Future Enhancements

## Recommended Upgrades:

* SHAP Explainability
* GPT-powered Tax Chat Assistant
* Multi-state tax logic
* Schedule M-1/M-2 automation
* PDF Form generation
* CRM integrations
* Customer engagement analytics
* Audit risk scoring

---

# Business Value

## Benefits:

### For Firms:

* Reduce manual tax prep time
* Improve classification consistency
* Increase legal tax savings
* Enhance client advisory services

### For Customers:

* Better deduction visibility
* Year-over-year tax savings insights
* Explainable recommendations
* Faster filing workflows

---

# Team Talking Points

## Positioning Statement:

> “We built a hybrid AI-powered corporate tax advisory system that automates Form 1120 preparation using machine learning, rule-based IRS compliance, explainable AI dashboards, and financial optimization recommendations.”

---

# Troubleshooting

## Common Issues:

### Uvicorn not found:

```bash
python -m uvicorn app.main:app --reload
```

### Missing model:

```bash
python train_model.py
```

### Angular dependency conflicts:

```bash
npm install --legacy-peer-deps
```

### Missing python-multipart:

```bash
pip install python-multipart
```

---

# Author Notes

This system is designed for:

* AI/ML demos
* Tax automation prototypes
* Enterprise finance innovation
* GenAI + traditional ML hybrid systems

---

# Final Vision

This platform evolves from:

### Traditional Tax Software → Intelligent Tax Advisory Ecosystem

By combining:

* Automation
* Explainability
* Legal optimization
* ML scalability

It represents a modern finance transformation project suitable for:

* Hackathons
* Internal enterprise tools
* Tax innovation initiatives
* Portfolio demonstrations
