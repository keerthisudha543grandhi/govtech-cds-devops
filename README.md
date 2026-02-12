# GovTech CDS DevOps Challenge – Visitor Counter Application

## Overview
This project is an end-to-end DevOps implementation for the GovTech CDS (Citizen Disbursement System) challenge.

It demonstrates how to design, deploy, and operate a scalable cloud-native application using AWS, Terraform, Docker, Kubernetes (EKS), and Redis.

The application displays a visitor counter on a webpage.  
Each page refresh increments the counter value, which is stored in Redis.

---

## Architecture Overview
The solution uses the following technologies:

- Application: Python Flask
- Backend Store: Redis
- Containerization: Docker
- Orchestration: Kubernetes (AWS EKS)
- Infrastructure as Code: Terraform
- Cloud Provider: AWS (ap-southeast-1)
- Public Access: Kubernetes LoadBalancer (AWS ELB)

---

### Architecture Flow
1. User accesses the application via a public AWS LoadBalancer
2. Traffic is routed to EKS worker nodes
3. Visitor App pods process requests
4. Redis pod stores and updates visitor count
5. Terraform provisions and manages AWS infrastructure

---

## CI/CD Pipeline (Build → Test → Deploy)

The CI/CD pipeline follows a simple and effective **Build → Test → Deploy** model using GitLab CI/CD.

### 1️.Build Stage
- Triggered when code is pushed to the repository
- Docker image for the Flask application is built
- Image is tagged with commit SHA or version
- Image is pushed to Docker Hub

### 2️.Test Stage
- Basic validation of Docker image
- Ensures image builds successfully
- Verifies application startup inside container

### 3️. Deploy Stage
- Terraform is used to provision or update AWS EKS infrastructure
- Kubernetes manifests are applied using `kubectl`
- Rolling updates ensure zero downtime
- Application is exposed via AWS LoadBalancer

govtech-cds-devops/
├── app/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── k8s/
│ ├── app.yaml
│ ├── service.yaml
│ └── redis.yaml
├── terraform/
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
├── diagrams/
│ ├── architecture.png
│ └── cicd-pipeline.png
├── .gitignore
└── README.md

---

## Application Details
- Displays visitor count on the homepage
- Redis stores visitor count
- Application listens on port `5000`
- Multiple replicas are deployed for scalability

Example output:

Visitor count: 3

---

## Prerequisites
- AWS CLI configured
- Terraform installed
- Docker installed
- kubectl installed
- AWS IAM permissions for EKS

---

## Infrastructure Provisioning (Terraform)


```bash
cd terraform
terraform init
terraform apply

This provisions:

VPC and networking

EKS cluster

Managed node group

IAM roles and policies

Kubernetes Deployment
kubectl apply -f k8s/redis.yaml
kubectl apply -f k8s/app.yaml
kubectl apply -f k8s/service.yaml

Verify:

kubectl get pods
kubectl get svc
Public Access
kubectl get svc visitor-service

Open in browser:

http://<EXTERNAL-IP>
Scalability

Stateless application design

Multiple replicas for high availability

Redis as centralized datastore

Kubernetes supports horizontal scaling

AWS Best Practices Followed

Infrastructure as Code using Terraform

Managed EKS cluster

LoadBalancer for public access

Secure IAM-based access

Separation of infra and application layers

Cost-efficient and scalable architecture

Troubleshooting Summary

Fixed Docker image pull issues

Corrected Kubernetes Service targetPort

Resolved Redis connectivity by fixing Service selectors

Debugged application errors using pod logs

Cleanup
kubectl delete -f k8s/
cd terraform
terraform destroy

Author
Keerthi Grandhi



