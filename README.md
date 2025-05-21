# Flask + Docker + Kubernetes (kops) on AWS

This project demonstrates how to deploy a Flask web application using Docker and Kubernetes (kops) on AWS. It includes containerizing the app, pushing to Docker Hub, provisioning a Kubernetes cluster using `kops`, and deploying via `kubectl`.

---

## 🚀 Technologies Used

- **Flask** (Python web framework)
- **Docker** (for containerizing the app)
- **Docker Hub** (as image registry)
- **Kubernetes (kops)** (for cluster provisioning)
- **AWS EC2, S3, and Load Balancer**

---

## 📁 Project Structure

```
myproject/
├── app.py
├── requirements.txt
├── Dockerfile
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

---

## ⚙️ Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/yourusername/myproject.git
cd myproject
```

### 2. Build and Push Docker Image
```bash
docker build -t mohammedjaffarhussain/myproject:latest .
docker login
# Enter Docker Hub username and password
docker push mohammedjaffarhussain/myproject:latest
```

### 3. Set up Kubernetes cluster with kops (on AWS)
```bash
export KOPS_STATE_STORE=s3://your-s3-bucket-name
kops create cluster \
  --name=myprojectcluster.k8s.local \
  --zones=your-aws-zone \
  --state=$KOPS_STATE_STORE \
  --node-count=2 \
  --node-size=t3.medium \
  --master-size=t3.medium \
  --yes
```

### 4. Deploy the App to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 5. Get External IP and Access App
```bash
kubectl get svc
# Visit the EXTERNAL-IP in your browser
```

---

## 📦 Dockerfile
```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🐍 app.py
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from MyProject!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## 📄 requirements.txt
```
Flask
```

---
## ✅ Outcome
Deployed a live Flask app at:

🔗 [http://a873cd2da1c0c4a25968c0c42163672f-977527883.eu-north-1.elb.amazonaws.com/](http://a873cd2da1c0c4a25968c0c42163672f-977527883.eu-north-1.elb.amazonaws.com/)

----


## 👨‍💻 Author
**Mohammed Jaffar Hussain**  
DockerHub: [mohammedjaffarhussain](https://hub.docker.com/u/mohammedjaffarhussain)

---

## 📝 License
This project is open-source and free to use under the [MIT License](LICENSE).
