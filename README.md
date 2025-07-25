# 💸 Personal Finance Dashboard

An interactive, cloud-hosted dashboard to analyze your financial data across multiple years, built with [Streamlit](https://streamlit.io).

---

## 📦 Features

- Upload and combine multiple bank statement CSVs
- Filter by date, category, type, or counterparty
- Visualize spending by category
- Track income sources
- Monthly net flow charts
- Export filtered transactions

---

## 🚀 Deployment

### ✅ Deploy to Streamlit Cloud

1. Fork or clone this repo:  
   `https://github.com/NightMonk/personal-finance-dashboard`

2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)  
   Log in and click **“New app”**

3. Choose your repo and set:
   - **Main file:** `streamlit_app.py`

4. Click **Deploy** – your dashboard will be live in seconds!

---

## 📁 CSV Format Expected

Each CSV should have the following columns:

- `Date`
- `Counter Party`
- `Reference`
- `Type`
- `Amount (GBP)`
- `Balance (GBP)`
- `Spending Category`
- `Notes`

Make sure to place all your `.csv` files inside the `data/` folder.

---

## 📊 Example

![Dashboard Screenshot](https://user-images.githubusercontent.com/your-screenshot.png)

---

## 🛠 Built With

- Python
- Streamlit
- Pandas
- Plotly

Enjoy your financial insights!
