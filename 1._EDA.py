import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = st.session_state["df"] 
if df is None:
    df = pd.read_csv("spotify-2023.csv", encoding="latin-1")

st.title("📌 Distribusi Kolom Menggunakan Bar Chart")
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, bins=30, color="skyblue", ax=ax)
    st.pyplot(fig)

st.title("📌 Boxplot Untuk Setiap Kolom Numerik")
for col in numeric_cols:
    fig, ax = plt.subplots()
    sns.boxplot(x=df[col], color="skyblue", ax=ax)
    st.pyplot(fig)

st.title("📌 Heatmap Korelasi")
features = ["danceability_%", "energy_%", "valence_%", "acousticness_%",
            "speechiness_%", "instrumentalness_%", "liveness_%", "bpm"]

fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(df[features + ["streams"]].corr(), annot=True, cmap="coolwarm", ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig)