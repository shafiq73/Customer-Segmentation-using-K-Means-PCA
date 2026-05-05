# Customer-Segmentation-using-K-Means-PCA
"An end-to-end Data Science project using K-Means Clustering and PCA to segment customers based on their personality traits, income, and purchasing behavior. Includes data cleaning, feature engineering, and dimensionality reduction for targeted marketing insights."
# 🎯 Customer Personality Analysis & Segmentation

## 📖 Project Overview
This project performs **Customer Personality Analysis** to help a business understand its customers' ideal segments. Instead of a "one-size-fits-all" marketing strategy, this analysis allows for targeted marketing by grouping customers with similar needs, behaviors, and lifestyles.

## 🛠️ Technical Workflow
The project follows a structured Data Science pipeline:

1. **Data Preprocessing & Cleaning:** 
   - Handled missing values in the `Income` column using median imputation.
   - Removed redundant features and handled duplicate records.[cite: 1]
2. **Feature Engineering:** 
   - Created new features: `Age`, `Total_Spending`, `Children` (Kids + Teens), and `Customer_Days` (Seniority).[cite: 1]
   - Simplified categorical data like `Marital_Status` for better model interpretation.[cite: 1]
3. **Outlier Management:** 
   - Used the IQR method to cap extreme values in `Income` and `Age` to prevent cluster distortion.[cite: 1]
4. **Dimensionality Reduction (PCA):** 
   - Applied **Principal Component Analysis (PCA)** to reduce the feature space to 3 components while retaining ~70% of the variance.[cite: 1]
5. **Clustering:** 
   - Implemented **K-Means Clustering**.[cite: 1]
   - Used the **Elbow Method** and **Silhouette Score** to determine the optimal number of clusters (4).[cite: 1]

## 📊 Customer Segments Identified
Based on the analysis, the customers are divided into 4 distinct groups:

*   **Cluster 0 (High-Value VIPs):** High income and high spending levels across all product categories.[cite: 1]
*   **Cluster 1 (Budget-Conscious):** Lower income and cautious spending habits, primarily focusing on essential deals.[cite: 1]
*   **Cluster 2 (Family-Oriented):** Customers with more children at home who show moderate spending patterns.[cite: 1]
*   **Cluster 3 (Loyal Seniors):** Older customers with long-term membership and steady, reliable purchasing history.[cite: 1]

## 📈 Visualizations
![Customer Segments](Capture200.PNG)
*The 2D PCA plot shows clear separation between the four customer segments, confirming the effectiveness of the clustering model.*[cite: 1]

## 📂 Project Structure
- `customer_segmentation.ipynb`: The main notebook containing the Python code.
- `customer_segmentation.csv`: The raw dataset used for analysis.
- `Capture200.PNG`: Visualization of the final clusters.

## 💡 Conclusion
This segmentation provides actionable insights for the marketing team. By understanding these 4 clusters, the business can optimize its marketing budget by offering the right promotions to the right group of people.[cite: 1]
