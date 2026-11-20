# 🚀 MLOps Class Activity: CI/CD Pipeline using GitHub Actions

This repository is part of the **MLOps course activity** on **Continuous Integration and Deployment (CI/CD)** for Machine Learning.  
The goal is to automate an ML workflow using **GitHub Actions** — from preprocessing to training, evaluation, and containerization.

---

## 🎯 Learning Objectives

By the end of this activity, you will be able to:

- Understand CI/CD concepts applied to ML projects  
- Automate data preprocessing, model training, and evaluation using GitHub Actions  
- Upload trained model artifacts automatically  
- (Optionally) Build and push Docker containers after successful training  

---

## 🧩 Repository Structure

```
mlops-ci-activity/
│
├── data/                      # Optional: sample dataset (if used)
│
├── preprocess.py              # Preprocessing script
├── train.py                   # Model training script
├── evaluate.py                # Model evaluation script
├── requirements.txt           # Dependencies
├── Dockerfile.train           # Docker image for training
├── Dockerfile.serve           # Docker image for serving
│
└── .github/
    └── workflows/
        └── ci-pipeline.yml    # GitHub Actions workflow definition
```

---

## ⚙️ Step-by-Step Instructions

1️⃣ Fork this Repository → 2️⃣ Add Secrets (optional) → 3️⃣ Push to `main` → 4️⃣ Observe Actions tab  
Artifacts and Docker builds will appear automatically.

---
#### Change github actions
---

## 📚 References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [MLOps with GitHub Actions](https://mlops.community/github-actions-for-mlops/)
- [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html)



# Triggering CI/CD run by Ali Hashim
