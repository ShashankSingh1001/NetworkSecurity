# 🛡️ Network Intrusion Detection System using Machine Learning

A production-ready **Network Intrusion Detection System (NIDS)** built using Machine Learning, FastAPI, Docker, and deployed on AWS EC2. This system detects and classifies potential malicious network activity in real-time, offering a scalable and modular approach to cybersecurity automation.

---

## 🚀 Key Features

- ✅ **End-to-End ML Pipeline**  
  Data Ingestion → Validation → Transformation → Model Training → Inference

- 🌐 **FastAPI-Powered Web API**  
  Lightweight and high-performance backend for prediction serving

- 🗄️ **MongoDB Integration**  
  Stores and manages cleaned datasets for future training and analysis

- 🐳 **Dockerized Architecture**  
  Seamless deployment across environments

- ☁️ **Cloud Deployment on AWS EC2**  
  Production-ready deployment using EC2 (t2.micro free tier)

- 🧪 **Robust Exception Handling and Logging**  
  Ensures reliability and traceability in every pipeline stage

---

## 🛠️ Tech Stack

| Layer              | Tools & Frameworks                          |
|--------------------|---------------------------------------------|
| Programming Lang.  | Python 3.x                                  |
| ML Libraries       | scikit-learn, pandas, numpy                 |
| Web Framework      | FastAPI + Uvicorn                           |
| Data Storage       | MongoDB (cloud-hosted)                      |
| Environment Mgmt   | python-dotenv, logging                      |
| Containerization   | Docker                                      |
| Deployment         | AWS EC2 (t2.micro)                          |

---

## 📁 Project Structure

```bash
NetworkSecurity/
├── app.py                  # FastAPI application
├── main.py                 # Training pipeline launcher
├── push_data.py            # Push transformed data to MongoDB
├── src/
│   ├── components/         # Ingestion, validation, transformation
│   ├── configuration/      # Configuration manager
│   ├── constant/           # Constants
│   ├── entity/             # Entity classes for config/data
│   ├── logger/             # Logging module
│   ├── exception/          # Custom exception handling
│   └── utils/              # Utility functions
├── artifacts/              # Stores intermediate pipeline files
├── models/                 # Trained model pickle files
├── .env                    # Environment variables (add your own)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
````

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/network-security-ml.git
cd network-security-ml
```

2. **Set up environment variables**

```bash
cp .env.example .env  # Then edit your MongoDB URL and other secrets
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Train the model**

```bash
python main.py
```

5. **Run the API server**

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

6. **Push processed data to MongoDB (optional)**

```bash
python push_data.py
```

---

## 🐳 Docker Deployment

```bash
docker build -t nids-app .
docker run -p 8000:8000 nids-app
```

---

## 📡 AWS EC2 Deployment Notes

* Use an EC2 instance (t2.micro if free tier).
* Open **port 8000** in your EC2 instance’s **Security Group**.
* Run:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

* Access via:
  `http://<your-ec2-public-ip>:8000`

---

## 🧪 Sample API Usage

```http
POST /predict
Content-Type: multipart/form-data
Body: CSV file containing network activity records
```

---

## 🧠 Project Purpose

The project addresses a critical cybersecurity challenge: real-time detection of network intrusions. By using machine learning and a clean modular architecture, the system can be extended to production environments in enterprise and cloud-native infrastructures.

---

## 🙋‍♂️ Author

**Shashank Singh**  
B.Tech CSE (Cloud Computing & AI)  
📧 shashanksinghofficial101@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/shashanksingh1001)

---

## ⭐ Contributions

Feel free to fork this project, open issues, or submit pull requests.

---




