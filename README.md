**GovTech CDS DevOps Challenge – Visitor Counter Application**
Overview

This repository contains an end-to-end DevOps implementation for the GovTech CDS DevOps Challenge.
It demonstrates building, containerizing, deploying, and operating a Visitor Counter Application on AWS using Docker, Kubernetes (EKS), Terraform, and CI/CD automation.

The application displays a visitor count that increments on every page refresh.
The counter value is stored in Redis, running inside the Kubernetes cluster.

Application Architecture

Frontend / API: Python Flask application

Backend: Redis (in-cluster)

Containerization: Docker

Orchestration: Kubernetes (AWS EKS)

Infrastructure as Code: Terraform

CI/CD: GitLab CI/CD

Cloud Provider: AWS

Kubernetes Deployment

All application resources are deployed into a dedicated Kubernetes namespace:

visitor-app

Kubernetes Manifests Include

Namespace definition

Deployment for Visitor Application

Deployment and ClusterIP Service for Redis

LoadBalancer Service for public access

Key Kubernetes Features

Namespace isolation (no default namespace usage)

Multiple replicas for high availability

Rolling update strategy enabled

Internal service discovery using Kubernetes DNS

External access via AWS LoadBalancer (ELB)

CI/CD Pipeline (GitLab CI/CD)

The application build and deployment are fully automated using GitLab CI/CD.

**Pipeline Stages**
1. Build

Build Docker image for the visitor application

2. Push

Push Docker image to Docker Hub

3. Deploy

Configure Kubernetes access using kubeconfig

Apply Kubernetes manifests to the EKS cluster using kubectl

**CI/CD Features**

Secure CI/CD variables for:

Docker Hub credentials

AWS credentials

Kubernetes kubeconfig (base64 encoded)

Fully automated build and deployment

No manual Docker or kubectl commands required after pipeline execution

Pipeline execution history maintained in GitLab

Terraform Infrastructure

Terraform is used to provision the AWS infrastructure required for Kubernetes deployment.

Provisioned Resources

Amazon EKS cluster

VPC and networking components

Managed EKS node group

Security groups for cluster and worker nodes

IAM roles and policies required for EKS operation

Terraform Backend

Remote backend configured using Amazon S3

Ensures centralized and consistent state management

Suitable for CI/CD-based Terraform execution

Terraform Enhancements Implemented

The following enhancements have been implemented as part of this solution:

✅ Managed EKS Node Group

✅ Required IAM roles and policies

✅ Security group rules for control plane and worker nodes

✅ Remote Terraform backend using S3 (state management)

These additions improve security, scalability, and production readiness of the infrastructure.

Repository Structure
├── app/                     # Flask application source code
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── k8s/                     # Kubernetes manifests
│   ├── namespace.yml
│   ├── deployment.yml
│   ├── redis.yml
│   └── service.yml
│
├── terraform/               # Terraform infrastructure code
│   ├── backend.tf
│   ├── main.tf
│   ├── nodegroup.tf
│   ├── iam.tf
│   ├── security_groups.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── .gitlab-ci.yml            # GitLab CI/CD pipeline definition
└── README.md

Verification

After a successful pipeline execution:

Application is accessible via AWS LoadBalancer URL

Visitor counter increments correctly on page refresh

Redis stores and persists counter values

Kubernetes pods are healthy and running in the visitor-app namespace

CI/CD pipeline completes successfully without manual intervention

Submission Notes

CI/CD pipeline execution screenshots are included as proof

Kubernetes namespace usage is implemented

Docker build, push, and deployment are automated

Terraform remote backend (S3) is configured

Sensitive credentials are securely masked in CI/CD variables

**Conclusion**

This project demonstrates a complete DevOps workflow, including:

Infrastructure provisioning using Terraform

Secure and scalable Kubernetes deployment on AWS EKS

Application containerization using Docker

Fully automated CI/CD using GitLab

Best practices such as namespace isolation, managed node groups, and remote state management

The solution aligns with GovTech CDS DevOps Challenge requirements and follows industry-standard DevOps practices.

Author 
Grandhi keerthisudha
