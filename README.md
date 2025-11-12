# 🛍️ Flipkart Product Recommender

The **Flipkart Product Recommender** is a data-driven system that recommends the **best Flipkart products** from a given dataset based on various attributes like ratings, price, and reviews.  
It integrates analytics, configuration handling, and performance monitoring tools like **Grafana** and **Prometheus** to provide an efficient and scalable recommendation pipeline.

---

## 🚀 Features

- 📊 Recommends top-rated or most relevant products from Flipkart dataset  
- 🔍 Allows searching or filtering by category, brand, or specifications  
- ⚙️ Modular architecture — configurations and data pipelines separated  
- 📈 Performance monitoring integrated with **Prometheus** and **Grafana**  
- 🧠 Uses Python data manipulation and recommendation logic  
- 🌐 Web-ready structure with templates and static files for visualization  

---

## 🧰 Technologies Used

### **Core Technologies**
- **Programming Language:** Python 3.8+
- **Data Handling:** pandas, numpy
- **Recommendation Logic:** scikit-learn, cosine similarity / ML-based model
- **Configuration:** python-dotenv, custom `config.py`
- **Monitoring:** Prometheus, Grafana
- **Environment Management:** venv

### **Supporting Tools**
- **VS Code** — development environment  
- **Git & GitHub** — version control  
- **Flask (optional)** — for web interface (using `templates/` and `static/`) 

### 📊 **Monitoring with Prometheus and Grafana**

This project includes integration for performance monitoring and visualization.

**Prometheus**

- Collects metrics from the recommender system (latency, requests, accuracy, etc.)

- Configuration files located in /prometheus/

**Grafana**

- Visualizes performance dashboards and product metrics

- Configuration and dashboard JSON files in /grafana/

### 🧠 **How It Works**

Loads dataset from data/ folder.

Cleans and converts the raw product data using data_converter.py.

Loads configurations from config.py and .env.

Runs the recommendation algorithm (rule-based or ML-based) to find the best products.

Outputs ranked products or displays them on a simple web interface.
### _🧩 Example Output_

Top 5 Recommended Products:
- 1️⃣ iPhone 13 - Rating: 4.8 ⭐
- 2️⃣ Samsung Galaxy S22 - Rating: 4.7 ⭐
- 3️⃣ OnePlus 10 Pro - Rating: 4.6 ⭐
- 4️⃣ Mi 11 Ultra - Rating: 4.5 ⭐
- 5️⃣ Realme GT Neo - Rating: 4.4 ⭐
