---
layout: post
title: "Customer Segmentation Using K-Means Clustering & PCA"
date: 2026-06-11
categories: machine-learning data-science
---

# Customer Segmentation Analysis

In this project, I developed a machine learning pipeline to perform customer segmentation. By grouping customers based on their purchasing behavior and profiles, businesses can launch targeted marketing campaigns and optimize resource allocation.

## 1. Dimensionality Reduction with PCA
Before clustering, I applied **Principal Component Analysis (PCA)**. High-dimensional data often contains noise and redundancy. PCA helped compress the features into principal components while retaining maximum variance, making the clustering algorithm more efficient.

## 2. K-Means Clustering
Using the reduced dimensions from PCA, I implemented the **K-Means Clustering** algorithm. 
* **The Elbow Method:** I utilized the elbow method to determine the optimal number of clusters ($K$).
* **Segmentation:** The algorithm successfully segmented the customer base into distinct, actionable groups.

## 3. Business Insights
Each cluster represents a specific customer persona:
* **Cluster 0:** High earners with high spending scores (Premium Customers).
* **Cluster 1:** Low spenders who require targeted engagement.
* **Cluster 2:** Balanced customers with average income and spending.

---
*Developed using Python, Scikit-Learn, Pandas, and PCA.*
