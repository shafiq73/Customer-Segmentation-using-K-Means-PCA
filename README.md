1. Problem Statement & Business Context
In the modern retail environment, a "one-size-fits-all" marketing strategy is no longer effective. This project addresses the challenge of understanding a diverse customer base by analyzing 2,240 customer profiles. By identifying distinct personas, the business can shift from generic mass marketing to personalized engagement, thereby increasing the return on investment (ROI) for marketing campaigns and improving customer retention.  

2. Advanced Feature Engineering Strategy
To capture the true essence of customer behavior, several raw data points were combined into meaningful metrics:

Customer Seniority (Customer_Days): Calculated by measuring the time elapsed since enrollment, allowing us to distinguish between long-term loyalists and new acquisitions.  

Share of Wallet (Total_Spending): Aggregated spending across six product categories (Wines, Fruits, Meat, Fish, Sweets, and Gold) to identify high-value vs. low-value segments.  

Family Dynamics (Children): Consolidated kids and teenagers into a single feature to understand how household size influences purchase frequency.  

3. Overcoming High Dimensionality (The PCA Approach)
The dataset originally contained over 25 features, which can lead to the "Curse of Dimensionality" in clustering. By applying Principal Component Analysis (PCA), I reduced the data to 3 orthogonal components that explain the majority of the variance. This step was crucial not only for 2D/3D visualization but also for ensuring that the K-Means algorithm focuses on the most significant patterns rather than random noise.  

4. Cluster Validation & Optimization
The optimal number of clusters was not chosen at random. I utilized:

The Elbow Method: To find the "point of diminishing returns" for the Sum of Squared Distances (Inertia).  

Silhouette Analysis: To ensure that the resulting clusters were well-separated and cohesive, confirming that each customer truly belongs to their assigned segment.  

5. Strategic Recommendations
Targeting VIPs (Cluster 0): Recommend exclusive loyalty rewards and early access to premium products.  

Engagement for Budget Shoppers (Cluster 1): Focus on discount-driven campaigns and bundle deals.  

Family Retention (Cluster 2): Market bulk-buy offers and family-friendly product categories.
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
