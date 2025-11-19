import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = st.session_state["df"]

df_features = df
df = pd.get_dummies(df, columns=['key', 'mode'], prefix=['key', 'mode'])

top_10_songs = df.nlargest(10, 'streams')
top_50_songs = df.nlargest(50, 'streams')
top_100_songs = df.nlargest(100, 'streams')

key_colors = {
    'key_A': 'red',
    'key_A#': 'blue',
    'key_B': 'green',
    'key_C#': 'purple',
    'key_D': 'orange',
    'key_D#': 'cyan',
    'key_E': 'magenta',
    'key_F': 'yellow',
    'key_F#': 'lime',
    'key_G': 'pink',
    'key_G#': 'brown'
}

key_columns = ['key_A', 'key_A#', 'key_B', 'key_C#', 'key_D', 'key_D#', 'key_E', 'key_F', 'key_F#', 'key_G', 'key_G#']

#Keys Distribution 
st.title("🎵 Keys Distribution")

# Penyebaran keys di semua lagu
key_df = df[key_columns]
key_counts = key_df.eq(1).sum()

# Siapkan data untuk Plotly
plot_df = key_counts.reset_index()
plot_df.columns = ["key", "count"]

# Ambil warna sesuai key
plot_df["color"] = plot_df["key"].map(key_colors)

# Total keseluruhan
total_keys = plot_df["count"].sum()

# Buat pie chart interaktif
fig = px.pie(
    plot_df,
    names="key",
    values="count",
    title="Overall Keys Distribution",
    color="key",
    color_discrete_map=key_colors,
    hole=0.4     # bikin donut biar ada tempat buat total
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>Total: %{value}<br>Persen: %{percent}"
)

# Tambahkan total di tengah
fig.update_layout(
    annotations=[
        dict(
            text=f"<b>Total<br>{total_keys}</b>",
            x=0.5,
            y=0.5,
            font_size=18,
            showarrow=False
        )
    ],  
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Keys Distribution in Top 10, Top 50, and Top 100
st.title("🎵 Keys Distribution in Top 10, Top 50, and Top 100")

# Dataframes dan judul chart
dataframes = [top_10_songs, top_50_songs, top_100_songs]
chart_titles = ["Top 10 Songs", "Top 50 Songs", "Top 100 Songs"]

# Siapkan subplot interaktif
fig = make_subplots(
    rows=1, cols=3,
    specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
    subplot_titles=chart_titles
)

for i, (df_temp, title) in enumerate(zip(dataframes, chart_titles)):
    key_df = df_temp[key_columns]
    key_counts = key_df.eq(1).sum()

    # Hanya ambil key yang muncul
    key_counts_filtered = key_counts[key_counts > 0]

    fig.add_trace(
        go.Pie(
            labels=key_counts_filtered.index,
            values=key_counts_filtered.values,
            name=title,
            marker=dict(colors=[key_colors[k] for k in key_counts_filtered.index]),
            hovertemplate="<b>%{label}</b><br>Total: %{value}<br>Persen: %{percent}"
        ),
        row=1, col=i+1
    )

# Judul utama
fig.update_layout(
    title_text="Keys Distribution Comparison",
    legend_title="Keys",
    width=1200,
    height=500,
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)


#Mode Distribution
st.title("🎵 Mode Distribution")

# Dataframes untuk mode analysis
dataframes = [top_10_songs, top_50_songs, top_100_songs]
labels = ['Top 10', 'Top 50', 'Top 100']
columns_of_interest = ['mode_Major', 'mode_Minor']

# Hitung jumlah untuk setiap subset
counts_1 = {col: [] for col in columns_of_interest}

for d in dataframes:
    for col in columns_of_interest:
        counts_1[col].append(d[col].eq(1.0).sum())

# Ambil hasil hitungan
major_counts = counts_1['mode_Major']
minor_counts = counts_1['mode_Minor']

# Grafik interaktif
fig = go.Figure()

# Mode Major
fig.add_trace(go.Bar(
    x=labels,
    y=major_counts,
    name="Mode Major",
    marker_color="skyblue",
    text=major_counts,
    textposition="outside",
    hovertemplate="Subset: %{x}<br>Major: %{y}<extra></extra>"
))

# Mode Minor
fig.add_trace(go.Bar(
    x=labels,
    y=minor_counts,
    name="Mode Minor",
    marker_color="lightcoral",
    text=minor_counts,
    textposition="outside",
    hovertemplate="Subset: %{x}<br>Minor: %{y}<extra></extra>"
))

# Layout
fig.update_layout(
    title="Distribution of Mode Major and Minor",
    xaxis_title="Subset of Songs",
    yaxis_title="Count",
    barmode="group",
    bargap=0.25,
    bargroupgap=0.1,
    width=1000,
    height=500,
    legend_title="Mode",
    title_font=dict(size=18, family='Arial Black')
)

st.plotly_chart(fig, use_container_width=True)

#BPM Distribution
st.title("🎧 Distribusi BPM Setiap Subset Lagu")

fig = go.Figure()

bpm_avg = []

# Warna lebih terang untuk setiap subset
bright_colors = [
    "lightskyblue", "lightgreen", "khaki", "plum",
    "lightsalmon", "lightpink", "lightcoral"
]

for i, df_temp in enumerate(dataframes):

    # custom data: track name + artist
    custom_data = np.stack([
        df_temp['track_name'],
        df_temp['artist(s)_name']
    ], axis=-1)

    fig.add_trace(go.Scatter(
        x=[labels[i]] * len(df_temp),
        y=df_temp['bpm'],
        mode="markers",
        name=f"{labels[i]} BPM",
        opacity=0.7,
        customdata=custom_data,
        marker=dict(
            color=bright_colors[i % len(bright_colors)],
            size=9,
            opacity=0.8
        ),
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Artist: %{customdata[1]}<br>"
            "Subset: %{x}<br>"
            "BPM: %{y}<extra></extra>"
        )
    ))

    bpm_avg.append(df_temp['bpm'].mean())

# Garis rata-rata
fig.add_trace(go.Scatter(
    x=labels,
    y=bpm_avg,
    mode='lines+markers',
    line=dict(color='red'),
    name='Average BPM',
    hovertemplate="Rata-rata BPM: %{y}<extra></extra>"
))

fig.update_layout(
    title="Distribution of BPM for Each Subset (Interactive)",
    xaxis_title="Subset of Songs",
    yaxis_title="BPM",
    xaxis=dict(tickmode='array', tickvals=labels),
    title_font=dict(size=18, family='Arial Black'),
    height=550
)

st.plotly_chart(fig, use_container_width=True)