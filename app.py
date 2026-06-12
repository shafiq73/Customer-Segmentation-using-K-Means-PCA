import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import plotly.express as px

# 1. Dashboard Title & Description
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("📊 Customer Segmentation Dashboard (K-Means & PCA)")
st.write("Welcome Shafiq Ahmed! This dashboard allows you to explore customer groups interactively using Machine Learning.")

# 2. Generate/Load Dummy Data for Visualization
@st.cache_data
def load_data():
    np.random.seed(42)
    n_samples = 300
    data = {
        'Age': np.random.randint(18, 70, n_samples),
        'Annual_Income': np.random.randint(15, 140, n_samples),
        'Spending_Score': np.random.randint(1, 100, n_samples)
    }
    return pd.DataFrame(data)

df = load_data()

# 3. Sidebar Controls (Inputs)
st.sidebar.header("🔧 Settings & Parameters")
# Slider for user to choose number of clusters dynamically
num_clusters = st.sidebar.slider("Select Number of Clusters (K):", min_value=2, max_value=6, value=3, step=1)

# 4. Machine Learning Pipeline (Standardization -> PCA -> K-Means)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# Apply PCA
pca = PCA(n_components=2)
pca_features = pca.fit_transform(scaled_features)
df['PCA1'] = pca_features[:, 0]
df['PCA2'] = pca_features[:, 1]

# Apply K-Means
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(scaled_features)
df['Cluster'] = df['Cluster'].astype(str) # Convert to string for discrete color mapping

# 5. Dashboard Layout - Two Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 PCA Cluster Visualization")
    # Interactive 2D Scatter plot using Plotly
    fig_pca = px.scatter(
        df, x='PCA1', y='PCA2', color='Cluster',
        title=f"Customer Segments in PCA Space (K={num_clusters})",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_pca, use_container_width=True)

with col2:
    st.subheader("💰 Income vs Spending Score")
    fig_spend = px.scatter(
        df, x='Annual_Income', y='Spending_Score', color='Cluster',
        title="Original Feature Space",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_spend, use_container_width=True)

# 6. Cluster Summary Table
st.subheader("📋 Cluster Metrics Summary")
summary = df.groupby('Cluster')[['Age', 'Annual_Income', 'Spending_Score']].mean().reset_index()
st.dataframe(summary.style.format({'Age': '{:.1f}', 'Annual_Income': '{:.1f}', 'Spending_Score': '{:.1f}'}))
