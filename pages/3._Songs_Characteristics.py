import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = st.session_state["df"]

# Dataframe yang dipakai
top_10_songs = df.nlargest(10, 'streams')
top_50_songs = df.nlargest(50, 'streams')
top_100_songs = df.nlargest(100, 'streams')


#Audio Features Heatmap
st.title("🔗 Correlation Heatmap of Audio Features")

# Kolom yang dipakai
corr_features = ['danceability_%','valence_%', 'energy_%', 'acousticness_%',
                 'instrumentalness_%','liveness_%', 'speechiness_%']

corr = df[corr_features].corr()

# Plotly heatmap
fig = px.imshow(
    corr,
    text_auto=True,       # tampilkan angka korelasi
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    labels=dict(color="Correlation"),
    aspect="auto"
)

fig.update_layout(
    title="Correlation Heatmap of Audio Features",
    title_font=dict(size=18, family="Arial Black"),
    xaxis_title="Features",
    yaxis_title="Features",
    width=800,
    height=650
)
fig.update_xaxes(tickangle=45)

st.plotly_chart(fig, use_container_width=True)


#Danceability(%) Distribution 
st.title("💃🏼 Danceability(%) Distribution")

dataframes = [df, top_100_songs, top_50_songs, top_10_songs]
labels = ["All Songs", "Top 100", "Top 50", "Top 10"]

danceability_min = []
danceability_max = []
danceability_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    danceability_min.append(d['danceability_%'].min())
    danceability_max.append(d['danceability_%'].max())
    danceability_avg.append(d['danceability_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=danceability_max,
    mode='lines+markers',
    name='Max Danceability',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.2f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=danceability_avg,
    mode='lines+markers',
    name='Average Danceability',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.2f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=danceability_min,
    mode='lines+markers',
    name='Min Danceability',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.2f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Danceability – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Danceability",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)



#Valence(%) Distribution 
st.title("😃 Valence(%) Distribution")

#Mengecek distribusi rata" valence
valence_min = []
valence_max = []
valence_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    valence_min.append(d['valence_%'].min())
    valence_max.append(d['valence_%'].max())
    valence_avg.append(d['valence_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=valence_max,
    mode='lines+markers',
    name='Max Valence',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.2f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=valence_avg,
    mode='lines+markers',
    name='Average Valence',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.2f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=valence_min,
    mode='lines+markers',
    name='Min Valence',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.2f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Valence – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Valence",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Energy(%) Distribution 
st.title("⚡ Energy(%) Distribution")

# Mengecek distribusi rata" energy
energy_min = []
energy_max = []
energy_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    energy_min.append(d['energy_%'].min())
    energy_max.append(d['energy_%'].max())
    energy_avg.append(d['energy_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=energy_max,
    mode='lines+markers',
    name='Max Energy',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.2f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=energy_avg,
    mode='lines+markers',
    name='Average Energy',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.2f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=energy_min,
    mode='lines+markers',
    name='Min Energy',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.2f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Energy – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Energy",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Acousticness(%) Distribution 
st.title("🎻 Acousticness(%) Distribution")

# Mengecek distribusi rata" acousticness
ac_min = []
ac_max = []
ac_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    ac_min.append(d['acousticness_%'].min())
    ac_max.append(d['acousticness_%'].max())
    ac_avg.append(d['acousticness_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=ac_max,
    mode='lines+markers',
    name='Max Acousticness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.2f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=ac_avg,
    mode='lines+markers',
    name='Average Acousticness',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.2f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=ac_min,
    mode='lines+markers',
    name='Min Acousticness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.2f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Acousticness – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Acousticness",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Instrumentalness(%) Distribution 
st.title("🎼 Instrumentalness(%) Distribution")

# Mengecek distribusi rata" instrumentalness
ins_min = []
ins_max = []
ins_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    ins_min.append(d['instrumentalness_%'].min())
    ins_max.append(d['instrumentalness_%'].max())
    ins_avg.append(d['instrumentalness_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=ins_max,
    mode='lines+markers',
    name='Max Instrumentalness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.6f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=ins_avg,
    mode='lines+markers',
    name='Average Instrumentalness',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.6f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=ins_min,
    mode='lines+markers',
    name='Min Instrumentalness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.6f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Instrumentalness – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Instrumentalness",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Liveness(%) Distribution 
st.title("🎤 Liveness(%) Distribution")

# Mengecek distribusi rata" liveness
liveness_min = []
liveness_max = []
liveness_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    liveness_min.append(d['liveness_%'].min())
    liveness_max.append(d['liveness_%'].max())
    liveness_avg.append(d['liveness_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=liveness_max,
    mode='lines+markers',
    name='Max Liveness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.3f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=liveness_avg,
    mode='lines+markers',
    name='Average Liveness',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.3f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=liveness_min,
    mode='lines+markers',
    name='Min Liveness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.3f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Liveness – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Liveness",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Speechiness(%) Distribution 
st.title("🎻 Speechiness(%) Distribution")

# Mengecek distribusi rata" speechiness
speechiness_min = []
speechiness_max = []
speechiness_avg = []

# Hitung nilai untuk setiap subset
for d in dataframes:
    speechiness_min.append(d['speechiness_%'].min())
    speechiness_max.append(d['speechiness_%'].max())
    speechiness_avg.append(d['speechiness_%'].mean())

fig = go.Figure()

# Max
fig.add_trace(go.Scatter(
    x=labels,
    y=speechiness_max,
    mode='lines+markers',
    name='Max Speechiness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Max: %{y:.3f}<extra></extra>"
))

# Average
fig.add_trace(go.Scatter(
    x=labels,
    y=speechiness_avg,
    mode='lines+markers',
    name='Average Speechiness',
    marker=dict(size=8),
    line=dict(color="green"),
    hovertemplate="Subset: %{x}<br>Avg: %{y:.3f}<extra></extra>"
))

# Min
fig.add_trace(go.Scatter(
    x=labels,
    y=speechiness_min,
    mode='lines+markers',
    name='Min Speechiness',
    marker=dict(size=8),
    hovertemplate="Subset: %{x}<br>Min: %{y:.3f}<extra></extra>"
))

fig.update_layout(
    title="Distribution of Speechiness – All, Top 100, Top 50, Top 10",
    xaxis_title="Subset of Songs",
    yaxis_title="Speechiness",
    width=1100,
    height=550,
    legend_title="Metrics",
    hovermode="x unified",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)