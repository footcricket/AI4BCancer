#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# In[2]:


# Load the Wisconsin Breast Cancer dataset
file_path = r"C:\Users\Shaurya\Downloads\data.csv"
df = pd.read_csv(file_path)


# In[3]:


# Drop unnecessary columns
df = df.drop(columns=['id', 'Unnamed: 32'])


# In[4]:


# Encode the 'diagnosis' column (M=1, B=0)
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['diagnosis'] = label_encoder.fit_transform(df['diagnosis'])


# In[5]:


# Handle missing values by dropping rows with null values
df = df.dropna()


# In[6]:


# Split the dataset into features (X) and target variable (y)
X = df.drop(columns=['diagnosis'])
y = df['diagnosis']


# In[7]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[8]:


# Apply PCA
pca = PCA(n_components=10)  # You can adjust the number of components
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)


# In[9]:


# Apply K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_train_pca)


# In[10]:


# Predict clusters for the training and test sets
train_cluster_labels = kmeans.predict(X_train_pca)
test_cluster_labels = kmeans.predict(X_test_pca)


# In[11]:


# Evaluate clustering results using accuracy and classification report
train_accuracy = accuracy_score(y_train, train_cluster_labels)
test_accuracy = accuracy_score(y_test, test_cluster_labels)

print("Training Set Accuracy:", train_accuracy)
print("Test Set Accuracy:", test_accuracy)

print("\nClassification Report - Training Set:")
print(classification_report(y_train, train_cluster_labels, zero_division=1))

print("\nClassification Report - Test Set:")
print(classification_report(y_test, test_cluster_labels, zero_division=1))


# In[ ]:




