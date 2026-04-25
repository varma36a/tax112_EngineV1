
# 🧾 AI-Powered Form 1120 Tax Engine

An end-to-end intelligent tax computation system that processes **Trial Balance (TB)** data, classifies accounts using  **Machine Learning (XGBoost)** , applies tax rules, and generates **Form 1120 federal tax outputs** with an interactive Angular dashboard.

---

## 🚀 Features

* 📂 Upload Trial Balance (Excel)
* 🤖 ML-based Account Classification (XGBoost)
* 🧮 Automated Tax Rule Engine
* 🧾 Form 1120 Tax Computation
* 📊 Angular Dashboard (Preview + Results)
* 🔍 Confidence-based classification fallback

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* Pandas
* Scikit-learn
* XGBoost
* Joblib

### Frontend

* Angular
* TypeScript
* Chart.js (optional for dashboards)

---

## 📁 Project Structure

```
tax-1120-ai/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── ml/
│   ├── train_model.py
│   ├── requirements.txt
│
├── frontend/
│   └── tax-widget/
│
└── README.md
```

---

## ⚙️ Setup & Run Instructions

---

### 🧠 1. Backend Setup (FastAPI)

#### 📍 Navigate

```
cd backend
```

---

#### 📍 Activate environment

Using Conda:

```
conda activate tax1120
```

OR using venv:

```
python3 -m venv venv
source venv/bin/activate
```

---

#### 📍 Install dependencies

```
python -m pip install -r requirements.txt
```

---

#### 📍 Train ML Model (IMPORTANT)

```
python train_model.py
```

This will generate:

```
app/ml/xgb_model.pkl
app/ml/vectorizer.pkl
app/ml/label_encoder.pkl
```

---

#### 📍 Start Backend Server

```
python -m uvicorn app.main:app --reload
```

---

#### 🌐 Backend URLs

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000/)
* Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 🎨 2. Frontend Setup (Angular)

#### 📍 Navigate

```
cd frontend/tax-widget
```

---

#### 📍 Install dependencies

```
npm install
```

---

#### 📍 Start Angular App

```
ng serve
```

---

#### 🌐 Frontend URL

```
http://localhost:4200
```

---

## 🔁 Application Flow

1. Upload Trial Balance (Excel)
2. Backend parses data
3. ML model classifies accounts
4. Tax rules applied
5. Form 1120 generated
6. Results displayed in UI

---

## 📊 Sample Output

* Gross Receipts
* Deductions
* Taxable Income
* Tax Liability
* Category Breakdown
* Preview Table

---

## ⚠️ Troubleshooting

---

### ❌ pip not found

```
python -m pip install -r requirements.txt
```

---

### ❌ uvicorn not found

```
python -m uvicorn app.main:app --reload
```

---

### ❌ Model not found

```
python train_model.py
```

---

### ❌ Port already in use

```
python -m uvicorn app.main:app --reload --port 8001
```

---

## 🔮 Future Enhancements

* 📊 Advanced dashboard with charts
* 🧾 Full IRS Form 1120 mapping
* 🔍 Explainable AI (feature importance)
* ☁️ Deployment (Docker + Cloud)
* 🔐 User authentication & audit logs

---

## 👨‍💻 Author

Developed as part of AI Tax Automation Project 🚀

---

## ⭐ Contribute

Pull requests are welcome! Feel free to enhance features or improve accuracy.

---
