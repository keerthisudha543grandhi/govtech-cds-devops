# GovTech CDS DevOps Challenge – Visitor Counter Application

## Overview
This project is an end-to-end DevOps implementation for the GovTech CDS (Citizen Disbursement System) challenge.

It demonstrates how to design, deploy, and operate a scalable cloud-native application using AWS, Terraform, Docker, Kubernetes (EKS), and Redis.

The application displays a visitor counter on a webpage.  
Each page refresh increments the counter value, which is stored in Redis.

---

## Architecture Overview
The solution uses the following technologies:

- **Application**: Python Flask
- **Backend Store**: Redis
- **Containerization**: Docker
- **Orchestration**: Kubernetes (AWS EKS)
- **Infrastructure as Code**: Terraform
- **Cloud Provider**: AWS (ap-southeast-1)
- **Public Access**: Kubernetes LoadBalancer (AWS ELB)

---
### Architecture Flow
1. User accesses the application via a public AWS LoadBalancer URL
2. LoadBalancer routes traffic to EKS worker nodes
3. Visitor App pods handle incoming requests
4. Redis pod stores and updates the visitor count
5. Terraform provisions and manages the AWS infrastructure

---

### CI/CD Flow Explanation
1. Developer pushes code to the Git repository
2. GitLab CI/CD pipeline is triggered automatically
3. Docker image is built and pushed to Docker Hub
4. Terraform provisions or updates AWS EKS infrastructure
5. Kubernetes manifests are applied to deploy the application
6. Application is exposed via AWS LoadBalancer

---

## Repository Structure
govtech-cds-devops/
├── app/ # Flask application & Dockerfile
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── k8s/ # Kubernetes manifests
│ ├── app.yaml
│ ├── service.yaml
│ └── redis.yaml
├── terraform/ # Terraform IaC for AWS EKS
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
- Redis is used to persist visitor count
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
- AWS IAM permissions to create EKS resources

---
## Infrastructure Provisioning (Terraform)

Terraform provisions:
- VPC and networking
- EKS cluster
- Managed node group
- IAM roles and policies


### Commands
```bash
cd terraform
terraform init
terraform apply
Kubernetes Deployment
Deploy Redis
kubectl apply -f k8s/redis.yaml
Deploy Application
kubectl apply -f k8s/app.yaml
kubectl apply -f k8s/service.yaml
Verify
kubectl get pods
kubectl get svc
Public Access

Retrieve the LoadBalancer URL:

kubectl get svc visitor-service

Access the application:

http://<EXTERNAL-IP>

Scalability

Application runs with multiple replicas

Stateless application design

Redis used as shared backend

Kubernetes supports horizontal scaling

CI/CD Pipeline Design (GitLab)

The CI/CD pipeline is designed using GitLab CI/CD.

Pipeline Stages

Source

Developer pushes code to GitLab repository

Build

Build Docker image

Tag image with commit SHA

Push image to Docker Hub

Test

Validate container build

Run basic application checks

Infrastructure Deployment

Terraform init & plan

Terraform apply (manual approval)

Application Deployment

Deploy Kubernetes manifests

Rolling updates for zero downtime

Post-Deployment Verification

Validate pod health

Confirm service accessibility

Why GitLab CI/CD

Native CI/CD integration

Secure secrets management

Strong Docker and Kubernetes support

Well suited for Infrastructure as Code workflows

AWS Best Practices Followed

Infrastructure as Code using Terraform

Managed Kubernetes service (EKS)

LoadBalancer for public access

Stateless application design

Separation of infrastructure and application layers

Secure IAM-based access

Cost-efficient and scalable architecture

Troubleshooting Summary

Resolved Docker image pull errors

Corrected Kubernetes Service targetPort

Fixed Redis connectivity by correcting Service selectors

Debugged application errors using pod logs

Cleanup
kubectl delete -f k8s/
cd terraform
terraform destroy

Author
Keerthi Grandhi
