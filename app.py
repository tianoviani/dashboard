 # Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib
import matplotlib.image as mpimg
from scipy import stats
import seaborn as sns
import streamlit as st


# Sample data, replace this with your actual data
df = pd.read_csv('df.csv')

# Streamlit app
st.set_page_config(page_title="Products Category")

# Create containers for each tab
tab1 = st.container()
tab2 = st.container()


# Header
st.title("Top 10 Product")

# Plotting
plt.figure(figsize=(10, 6), facecolor='white')
top_categories = df['product_category_name'].value_counts().head(10)
sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
plt.title('Top 10 Product Categories by Number of Products')
plt.xlabel('Number of Products')
plt.ylabel('Product Category')
plt.tight_layout()

# Display the plot using Streamlit
fig1 = plt.gcf()  # Get the current figure
st.pyplot(fig1)

# Explanation
st.write("""
1. The category "cama_mesa_banho" stands out as the category with the highest number of products, indicating a significant presence in the dataset. This category is followed closely by "esporte_lazer" and "moveis_decoracao" in terms of product count. 
2. The plot showcases the diversity of products available in different categories, with varying quantities across the top 10 categories. This diversity reflects the range of offerings in the dataset.
3. By visualizing the product distribution, stakeholders can gain insights into the popularity and abundance of products in each category. This information can be valuable for inventory management, marketing strategies, and product development decisions.
""")


# Header
st.title("Product Distribution")

# Plotting
plt.figure(figsize=(14, 10), facecolor='white')
sns.pairplot(data=df, hue='product_category_name', vars=['product_length_cm', 'product_height_cm', 'product_width_cm'])
plt.suptitle('Distribution of Product Dimensions Across Different Categories', y=1.02)

# Display the plot using Streamlit 
fig = plt.gcf()
st.pyplot(fig)

# Explanation for "hr"

st.write("""
The pair plot displays the distribution of product dimensions (length, height, width) across different product categories. Each point on the plot represents a product, with colors indicating the product category. By analyzing the relationships between the dimensions within each category, you can observe how the dimensions vary and potentially identify any patterns or outliers. This visualization offers a comprehensive view of how product dimensions are distributed across various product categories, providing insights into the relationships and variations in dimension values within each category.""")




