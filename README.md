# GovTech CDS DevOps Assignment – Visitor App

## Overview
This project demonstrates an end-to-end DevOps deployment of a containerized Python application on AWS using Terraform, Docker, Kubernetes (EKS), and Redis.

The application displays a visitor counter that increments on every page refresh using Redis as a backend.

---

## Architecture
- **Application**: Python Flask
- **Containerization**: Docker
- **Orchestration**: Kubernetes (AWS EKS)
- **Infrastructure as Code**: Terraform
- **Database**: Redis
- **Exposure**: Kubernetes LoadBalancer (AWS ELB)

---

## Repository Structure
govtech-cds-devops/
├── app/ # Flask application & Dockerfile
├── k8s/ # Kubernetes manifests
│ ├── app.yaml
│ ├── service.yaml
│ └── redis.yaml
├── terraform/ # EKS infrastructure code
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
└── README.md


---

## Prerequisites
- AWS CLI configured
- Terraform installed
- Docker installed
- kubectl installed
- AWS EKS permissions


---


## Infrastructure Setup (Terraform)
```bash
cd terraform
terraform init
terraform apply

This provisions:

VPC and networking

EKS cluster

Managed node group

Required IAM roles

Application Deployment (Kubernetes)
kubectl apply -f k8s/redis.yaml
kubectl apply -f k8s/app.yaml
kubectl apply -f k8s/service.yaml

Verify:

kubectl get pods
kubectl get svc
Accessing the Application

The application is exposed via a Kubernetes LoadBalancer service.

kubectl get svc visitor-service

Open the EXTERNAL-IP in a browser:

http://<EXTERNAL-IP>

The page displays:

Visitor count: <number>

Refreshing the page increments the counter.

Troubleshooting Summary

Fixed Docker image pull issues

Corrected Kubernetes Service targetPort

Resolved Redis connectivity by fixing Service selectors

Debugged application-level 500 errors using pod logs

Cleanup
kubectl delete -f k8s/
cd terraform
terraform destroy
