# Tax 1120 AI Advisor System — Demo Presentation Guide

# Executive Summary

## Project Vision

The Tax 1120 AI Advisor System is an AI-powered enterprise tax intelligence platform that automates corporate federal tax preparation (IRS Form 1120) while providing:

* Intelligent account classification
* Legal tax optimization recommendations
* Explainable AI insights
* Prior Year vs Current Year tax savings analysis
* Financial dashboards for customer engagement

---

# Business Problem

Traditional corporate tax filing involves:

* Manual trial balance review
* Time-intensive account mapping
* Human classification errors
* Missed deduction opportunities
* Limited explainability
* Minimal advisory intelligence

## Pain Points

### Tax Teams:

* High operational cost
* Compliance complexity
* Slow turnaround time
* Inconsistent categorization

### Clients:

* Lower tax efficiency
* Poor savings visibility
* Reduced strategic planning

---

# Our Solution

## AI + Rule-Based Hybrid Platform

We built a system that:

### Input:

* Uploads Trial Balance (CSV/Excel)

### Processing:

* Parses accounts
* Uses XGBoost ML classification
* Applies IRS tax rules
* Calculates Form 1120 tax liability
* Generates advisor insights
* Produces explainability metrics

### Output:

* Tax return summary
* Tax savings opportunities
* Dashboard analytics
* Explainable model metrics

---

# Technology Stack

## Backend:

* FastAPI
* Python
* Pandas
* XGBoost
* Scikit-learn
* Joblib

## Frontend:

* Angular
* Chart.js
* SCSS Dark Dashboard

## AI Components:

* TF-IDF Vectorizer
* XGBoost Classifier
* Confidence Scoring
* Rule-Based IRS Tax Logic
* Explainability Engine

---

# Demo Workflow

# Step 1 — Upload Trial Balance

### User uploads:

* Current Year TB
* Prior Year TB

### Sample Accounts:

* Sales Revenue
* Office Rent
* Employee Salary
* Client Meals
* Penalty Expense

---

# Step 2 — AI Classification Engine

### ML Classifies Accounts Into:

* Income
* Expense
* Meals
* Penalty
* Charity
* Depreciation
* COGS
* Asset
* Non-Deductible

### Example:

| Account       | Prediction |
| ------------- | ---------- |
| Sales Revenue | Income     |
| Client Meals  | Meals      |
| IRS Penalty   | Penalty    |

---

# Step 3 — Tax Rule Engine

### Legal IRS Rules Applied:

* Meals → 50% deductible
* Penalties → Non-deductible
* Charity → Deduction limits
* Expenses → Full deduction

### Result:

* Gross Receipts
* Deductions
* Taxable Income
* Tax Liability

---

# Step 4 — Tax Advisor Intelligence

## Dashboard Recommendations:

### Examples:

### Client Meals:

> Only 50% deductible. Potential optimization available.

### Penalty Expense:

> Non-deductible. Reduce compliance violations.

### Low Confidence Accounts:

> Manual review recommended.

---

# Step 5 — Explainability Dashboard

## Metrics Displayed:

* Accuracy
* Precision
* Recall
* F1 Score
* Class-Level Performance
* Feature Importance

### Example Top Features:

* penalty
* meals
* rent
* salary
* revenue

---

# Step 6 — PY vs CY Comparison

## Business Insights:

* Tax liability increase/decrease
* Deduction efficiency changes
* Profitability comparison
* Strategic savings suggestions

### Example:

> CY tax reduced by 12% due to optimized deductible expenses.

---

# Model Performance

## Current Performance:

* Accuracy: ~98%
* Macro F1: ~97%
* Weighted F1: ~98%

## Key Note:

This is a high-performing baseline supported by:

* Expanded training dataset
* Synonym augmentation
* Rule overrides
* Explainability layers

---

# Competitive Advantage

## What Makes This Unique

### Traditional Tax Software:

* Rule-only
* Manual-heavy
* Limited advisory

### Our System:

* ML classification
* Explainability
* Tax optimization
* Advisory intelligence
* Dashboard analytics

---

# Customer Engagement Value

## Firms Gain:

* Faster filing
* Reduced prep costs
* Higher consistency
* Better advisory margins

## Clients Gain:

* More savings visibility
* Better tax planning
* Transparent recommendations
* Year-over-year comparisons

---

# Demo Talking Points

## Suggested Presentation Script

### Opening:

> “We built an AI-powered corporate tax advisor that automates Form 1120 preparation while identifying legal tax savings opportunities.”

### ML Layer:

> “Our XGBoost + TF-IDF engine classifies financial accounts with high accuracy and confidence scoring.”

### Compliance Layer:

> “We integrate IRS-based rule engines to ensure deductions follow federal compliance.”

### Explainability:

> “Unlike black-box models, we expose model metrics and feature drivers directly to users.”

### Strategic Value:

> “This transforms tax preparation from compliance-only into proactive financial advisory.”

---

# Live Demo Checklist

## Before Demo:

### Backend:

```bash
python train_model.py
python -m uvicorn app.main:app --reload
```

### Frontend:

```bash
ng serve
```

---

## During Demo:

### Show:

* File upload
* Classification preview
* KPI cards
* Pie chart
* Bar chart
* Tax advisor insights
* Explainability dashboard
* PY vs CY comparison

---

# Potential Questions & Answers

## Q: Why use XGBoost?

### A:

* Strong performance on structured tabular text features
* Handles classification well
* Efficient for production APIs

---

## Q: How is explainability handled?

### A:

* Feature importance
* Confidence scores
* Rule-based reasoning
* Dashboard metrics

---

## Q: Is this production-ready?

### A:

Current version is a mature prototype with strong extensibility for:

* Multi-state taxes
* LLM advisory chat
* PDF filing generation
* Audit scoring

---

# Roadmap

## Phase 2:

* SHAP explainability
* GPT tax assistant
* Schedule M automation
* CRM integration
* Real ERP connectors
* Multi-jurisdiction tax support

---

# Final Closing Statement

> “The Tax 1120 AI Advisor System modernizes corporate tax preparation by combining machine learning, explainable AI, and legal tax intelligence into a scalable enterprise platform.”

---

# Key Outcome

## This project demonstrates:

* AI engineering
* Tax domain expertise
* Full-stack development
* ML explainability
* Enterprise product thinking

---

# Demo Success Goal

## Audience should leave understanding:

### This is not just tax filing software.

### It is an intelligent tax optimization ecosystem.
