# GovTech CDS DevOps Challenge – Visitor Counter Application

## Overview
This repository contains an end-to-end DevOps implementation for the GovTech CDS DevOps Challenge.  
It demonstrates building, containerizing, deploying, and operating a visitor counter application on AWS using Kubernetes, Terraform, Docker, and CI/CD automation.

The application displays a visitor count that increments on every page refresh. The counter value is stored in Redis.

---

## Application Architecture
- **Frontend / API**: Python Flask application
- **Backend**: Redis (in-cluster)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (AWS EKS)
- **Infrastructure as Code**: Terraform
- **CI/CD**: GitLab CI/CD
- **Cloud Provider**: AWS

---

## Kubernetes Deployment
- All application resources are deployed into a **dedicated Kubernetes namespace** (`visitor-app`)
- Kubernetes manifests include:
  - Namespace
  - Deployment for visitor application
  - Deployment and Service for Redis
  - LoadBalancer Service for public access
- Rolling updates are enabled with multiple replicas for high availability

---

## CI/CD Pipeline (GitLab CI/CD)
The deployment is fully automated using GitLab CI/CD.

### Pipeline Stages
1. **Build**
   - Build Docker image for the visitor application
2. **Push**
   - Push the Docker image to Docker Hub
3. **Deploy**
   - Apply Kubernetes manifests to the EKS cluster using `kubectl`

### CI/CD Features
- Secure pipeline variables for:
  - Docker Hub credentials
  - AWS credentials
  - Kubernetes kubeconfig (base64-encoded)
- Fully automated build and deployment
- No manual kubectl or docker commands required after pipeline execution

---

## Terraform Infrastructure
Terraform is used to provision AWS infrastructure required for Kubernetes deployment.

### Current Scope
- EKS cluster provisioning
- Networking and base AWS resources

### Notes on Terraform Enhancements
The following enhancements are acknowledged and can be added as future improvements:
- Managed or self-managed EKS Node Groups
- Explicit IAM roles and policies for EKS and worker nodes
- Fine-grained security group rules
- Remote Terraform backend (S3 with DynamoDB state locking)

The current setup focuses on functional EKS provisioning and CI/CD-driven deployment as per challenge requirements.

---

## Repository Structure
├── app/ # Flask application source code
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── k8s/ # Kubernetes manifests
│ ├── namespace.yml
│ ├── deployment.yml
│ ├── redis.yml
│ └── service.yml
├── terraform/ # Terraform infrastructure code
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
├── .gitlab-ci.yml # GitLab CI/CD pipeline definition
└── README.md

---

## Verification
After a successful pipeline execution:
- Application is accessible via AWS LoadBalancer URL
- Visitor counter increments correctly on page refresh
- Redis stores and persists counter values
- Kubernetes pods are healthy and running in the `visitor-app` namespace

---

## Submission Notes
- CI/CD pipeline execution screenshots are included as proof
- Kubernetes namespace usage is implemented
- Docker build, push, and deploy are automated
- Sensitive credentials are securely masked in CI/CD variables

---

## Conclusion
This project demonstrates a complete DevOps workflow including infrastructure provisioning, containerization, Kubernetes deployment, and CI/CD automation, aligned with GovTech CDS DevOps Challenge requirements.

