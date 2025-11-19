import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

df = st.session_state["df"] 

#TOP ARTIST
st.title("🎤 Top Artists With The Most Songs in Spotify 2023")

artist_count = df["artist(s)_name"].value_counts().head(10).reset_index()
artist_count.columns = ["artist", "Number of Songs"]

fig = px.bar(
    artist_count,
    x="Number of Songs",
    y="artist",
    orientation="h",
    color="Number of Songs",
    color_continuous_scale="viridis"
)

fig.update_layout(yaxis=dict(autorange="reversed"))

st.plotly_chart(fig, use_container_width=True)


# TOP STREAMED SONGS
st.title("🎵 Top 10 Most Streamed Songs in Spotify 2023")

top10 = df.nlargest(10, "streams")

fig = px.bar(
    top10,
    x="streams",
    y="track_name",
    orientation="h",
    color="streams",
    color_continuous_scale="viridis",
    hover_data={"artist(s)_name": True, "streams": True} 
)

# Custom hover agar tampil lebih rapi
fig.update_traces(
    hovertemplate="<b>%{y}</b><br>" +
                  "Artist: %{customdata[0]}<br>" +
                  "Streams: %{x:,}"
)

# Pastikan customdata ikut dikirim
fig.update_traces(customdata=top10[["artist(s)_name"]])

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)


#TOP ARTIST WITH MOST STREAM
st.title("🎵 Top 10 Artists with the Most Total Streams in Spotify 2023")

# Ambil 10 artis dengan total streams terbanyak
top_10_artistas = (
    df.groupby('artist(s)_name', as_index=False)['streams']
    .sum()
    .sort_values(by='streams', ascending=False)
    .head(10)
)

# Buat grafik interaktif
fig = px.bar(
    top_10_artistas,
    x='streams',
    y='artist(s)_name',
    color='streams',  
    orientation='h',
    text='streams',
    color_continuous_scale='viridis'
)

# Layout tampilan
fig.update_traces(
    texttemplate='%{text:,}', 
    textposition='outside'
)

fig.update_layout(
    yaxis=dict(categoryorder='total ascending'), 
    xaxis_title='Total Streams',
    yaxis_title='Artist',
    coloraxis_showscale=True,
    font=dict(size=12, family='Arial', color='black'),
    margin=dict(l=100, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True)


#RELATION BETWEEN PLAYLIST AND STREAMS
st.title("🎵 Relationship Between Playlist Count and Streams")

# Buat grafik scatter interaktif
fig = px.scatter(
    df,
    x="in_spotify_playlists",
    y="streams",
    color="streams",  
    size="streams",   
    hover_name="track_name",  
    hover_data=["artist(s)_name"],
    color_continuous_scale="viridis",
    labels={
        "in_spotify_playlists": "Number of Playlists",
        "streams": "Streams (Billions)"
    }
)

# Ubah tampilan layout agar lebih bersih
fig.update_layout(
    xaxis=dict(showgrid=True, gridcolor='lightgrey'),
    yaxis=dict(showgrid=True, gridcolor='lightgrey'),
)

# Tampilkan grafik
st.plotly_chart(fig, use_container_width=True)