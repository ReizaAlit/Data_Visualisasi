import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Spotify 2023 Dashboard",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("spotify-2023.csv", encoding="latin-1")
    
    # Drop unnecessary columns
    cols_to_drop = ["in_apple_playlists", "in_apple_charts", "in_deezer_playlists", 
                    "in_deezer_charts", "in_shazam_charts"]
    df = df.drop(columns=cols_to_drop, errors="ignore")

    df = df.dropna()

    # Clean streams column
    df['streams'] = df['streams'].astype(str)
    df = df[~df['streams'].str.contains(r'[A-Za-z]', regex=True)]
    df['streams'] = df['streams'].replace({',': '', r'\.': ''}, regex=True).astype(int)

    return df

df = load_data()
st.session_state["df"] = df

st.markdown("<h1 style='text-align: center; color: #1DB954;'>📊 Spotify 2023 - Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

with st.expander("ℹ️ Tentang Dataset", expanded=True):
    st.markdown("""
    Dataset yang digunakan adalah **“Most Streamed Spotify Songs 2023”** dari Kaggle.  
    Dataset ini disusun oleh Nidula Elgiriyewithana melalui web scraping dari API Spotify dan situs resmi lagu.  

    Spotify adalah sumber **sangat kredibel** karena data (streams, playlists, BPM, danceability, energy, dll) berasal langsung dari **sistem analitik internal Spotify** yang digunakan secara global oleh industri musik.  

    Dataset ini memiliki:
    - **953 baris** dan **24 kolom**  
    - **7 kolom kategorikal**  
    - **17 kolom numerik**
    """)

st.subheader("🎯 Tujuan Analisis")
st.write("Menentukan **karakteristik lagu** yang paling diminati pengguna Spotify dan membantu **produser dan musisi** dalam merancang lagu sesuai tren pasar")

#Preview metrik
total_songs = df.shape[0]
total_artists = df["artist(s)_name"].nunique()
total_streams = df["streams"].sum()

st.subheader("Data After Cleaning")
col1, col2, col3 = st.columns(3)
col1.metric("Total Songs", f"{total_songs}")
col2.metric("Unique Artists", f"{total_artists}")
col3.metric("Total Streams", f"{total_streams:,}")

st.markdown("---")

st.subheader("📊 Statistik Deskriptif (Kolom Numerik)")
numeric_cols = df.select_dtypes(include='number').columns
desc_stats = df[numeric_cols].describe().T  # transpose agar lebih readable

# Styling dengan gradient hijau
desc_stats = desc_stats.style.format("{:.2f}")

st.dataframe(desc_stats, use_container_width=True)

st.markdown("---")

st.subheader("📋 Preview Dataset")
st.dataframe(df, use_container_width=True)
