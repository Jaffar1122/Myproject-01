# MyProject - Flask + Docker + Kubernetes on AWS

This is a sample Flask application containerized with Docker and deployed on a Kubernetes cluster managed with kops on AWS.

## Project Structure

- `app.py` - Flask web application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image build instructions
- `k8s/deployment.yaml` - Kubernetes Deployment manifest
- `k8s/service.yaml` - Kubernetes Service manifest

## How to Run

1. Build Docker image and push to Docker Hub:

```bash
docker build -t mohammedjaffarhussain/myproject:latest .
docker push mohammedjaffarhussain/myproject:latest

