# TripGenie India IN

### AI-Powered Multi-Agent Travel Planning System

TripGenie India is an intelligent travel planning platform that generates personalized travel itineraries, destination insights, hotel recommendations, budget planning, packing checklists, and downloadable travel reports using a Multi-Agent AI Architecture.

---

## 🚀 Features

### 👤 Profile Extraction Agent

Extracts:

* Destination
* Duration
* Budget
* Travel Type

### 🔍 Research Agent

Provides:

* Best time to visit
* Top attractions
* Popular foods
* Adventure activities
* Travel insights

### 🗺️ Planner Agent

Generates:

* Day-wise itinerary
* Sightseeing plan
* Food recommendations
* Activities

### 🌦️ Weather Agent

Provides destination weather information.

### 🏨 Hotel Agent

Recommends accommodation based on budget.

### 💰 Budget Agent

Creates a detailed budget breakdown.

### 🎒 Packing Checklist Agent

Generates destination-specific packing suggestions.

### 📄 PDF Report Generator

Exports the complete travel plan as a downloadable PDF.

---

## 🏗️ Multi-Agent Architecture

```text
User Query
    │
    ▼
Profile Extraction Agent
    │
    ▼
Research Agent
    │
    ▼
Travel Supervisor
    ├── Planner Agent
    ├── Weather Agent
    ├── Hotel Agent
    ├── Budget Agent
    └── Packing Agent
    │
    ▼
PDF Generator
    │
    ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Ollama
* Qwen 2.5
* ReportLab
* Multi-Agent Architecture

---
## 🎥 Project Demo
▶️ Watch the project demo here:
https://www.youtube.com/watch?v=jLxfCl_vFq8

## 📸 Project Screenshots

### Home Page
<img width="1920" height="1200" alt="Screenshot (1221)" src="https://github.com/user-attachments/assets/bcedbf35-423f-47cb-b95f-4de4c9d53033" />


<img width="1920" height="1200" alt="Screenshot (1222)" src="https://github.com/user-attachments/assets/01cb810a-4da3-4f5e-827f-ca74d5b373e9" />


### Travel Plan Generation

<img width="1920" height="1200" alt="Screenshot (1223)" src="https://github.com/user-attachments/assets/706f1f4d-6ec7-4560-88c8-6e3190855478" />
<img width="1920" height="1200" alt="Screenshot (1224)" src="https://github.com/user-attachments/assets/1124cb17-5424-405b-a53d-b7c5a71b4f2e" />
<img width="1920" height="1200" alt="Screenshot (1225)" src="https://github.com/user-attachments/assets/b67a6035-6cc2-4db4-bd3e-3cd5d55ac5be" />
<img width="1920" height="1200" alt="Screenshot (1226)" src="https://github.com/user-attachments/assets/fade5592-9afd-4819-b0c5-00789e459966" />



### PDF Report
<img width="353" height="1000" alt="Screenshot 2026-06-30 161948" src="https://github.com/user-attachments/assets/47659203-9770-4e85-b56e-6d6b421ae7ea" />





## 📸 Project Screenshots

### Jaipur Trip

![Jaipur Trip](screenshots/Jaipur.png)

### Kerala Trip

![Kerala Trip](screenshots/Kerala.png)

### Goa Trip

![Goa Trip](screenshots/Goa.png)

### Manali Trip

![Manali Trip](screenshots/Manali.png)

## 📂 Project Structure

```text
TripGenie-India/
│
├── agents/
│   ├── profile_agent.py
│   ├── planner_agent.py
│   ├── research_agent.py
│   ├── weather_agent.py
│   ├── hotel_agent.py
│   ├── budget_agent.py
│   └── packing_agent.py
│
├── supervisor/
│   ├── intelligent_supervisor.py
│   └── travel_supervisor.py
│
├── assets/
├── screenshots/
├── reports/
├── utils/
├── app_v2.py
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Sonali1554/TripGenie-India.git
```

Move into project directory:

```bash
cd TripGenie-India
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app_v2.py
```

---

## 🎯 Sample Query

```text
Plan a family trip to Jaipur for 4 days under ₹40,000
```

---

## 🌟 Future Enhancements

* Flight Recommendation Agent
* Travel Tips Agent
* Interactive Maps
* Real-Time Weather API
* Hotel Booking API
* Memory-Based Personalization

---

## 👩‍💻 Author

**Sonali Kumari**

* GitHub: https://github.com/Sonali1554
* LinkedIn: https://www.linkedin.com/in/sonali-kumari1207/

---

Built with ❤️ using Python, Streamlit, Ollama, and Multi-Agent AI.
