import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.style.use("seaborn-pastel")

def stats_year(df_clean_day):
    total_sewa_per_tahun = df_clean_day.groupby('yr').nunique().reset_index()
    total_sewa_per_tahun.rename(
        columns={'instant': 'sum'}, inplace=True)
    
    return total_sewa_per_tahun

def sidebar(df_clean_day):
    st.sidebar.image('D:\Documents\Pelatihan\Dicoding\Analisis data menggunakan python\Asset\girl-bike.png')

    min_date = pd.to_datetime(df_clean_day['dteday']).min()
    max_date = pd.to_datetime(df_clean_day['dteday']).max()

    date_input = st.sidebar.date_input(
        label='Rentang Waktu',
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    return date_input

def weather_impact(df_clean_day):
    cuaca_vs_permintaan = df_clean_day.groupby('weathersit').instant.nunique().reset_index()
    cuaca_vs_permintaan.rename(
        columns={'instant': 'sum'}, inplace=True)
    
    return cuaca_vs_permintaan

def season_impact(df_clean_day):
    rentals_per_season = df_clean_day.groupby('season').instant.nunique().reset_index()
    rentals_per_season.rename(
        columns={'instant': 'sum'}, inplace=True)
    return rentals_per_season

def holiday_impact(df_clean_day):
    rentals_on_holiday = df_clean_day.groupby('holiday').instant.nunique().reset_index()
    rentals_on_holiday.rename(
        columns={'instant': 'sum'}, inplace=True)
    return rentals_on_holiday

def year(df_clean_day):
    st.subheader('Tahun')

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.barplot(x='yr', y='sum', data=df_clean_day, ax=ax)
    ax.set_title('Jumlah Bike Sharing Per Tahun', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Tahun', fontsize=15)
    ax.set_ylabel('Jumlah', fontsize=15)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    for container in ax.containers:
        ax.bar_label(container, fontsize=12, padding=10)

    st.pyplot(fig)

def month(df_clean_day):
    st.subheader('Bulan')
    
    total_sepeda_per_bulan = df_clean_day.groupby('mnth')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.barplot(x='mnth', y='cnt', data=total_sepeda_per_bulan, ax=ax)
    ax.set_title('Jumlah Bike Sharing Per Bulan', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Bulan', fontsize=15)
    ax.set_ylabel('Jumlah', fontsize=15)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    for container in ax.containers:
        ax.bar_label(container, fontsize=12, padding=10)

    st.pyplot(fig)

def hour(df_clean_day):
    st.subheader('Jam')

    total_sepeda_per_jam = df_clean_day.groupby('hr')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))

    sns.barplot(x='hr', y='cnt', data=total_sepeda_per_jam, ax=ax)
    ax.set_title('Jumlah Bike Sharing Per Jam', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Jam', fontsize=15)
    ax.set_ylabel('Jumlah', fontsize=15)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    for container in ax.containers:
        ax.bar_label(container, fontsize=12, padding=10)

    st.pyplot(fig)

def visual_weathersit(df_clean_day):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(x='weathersit', y='sum', data=df_clean_day, ax=ax)
    ax.set_title('Pengaruh Cuaca Buruk Terhadap Permintaan Sepeda per Hari', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Kondisi Cuaca', fontsize=15)
    ax.set_ylabel('Rata-rata Permintaan Sepeda', fontsize=15)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain'])

    st.pyplot(fig)

def visual_season(df_clean_day):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(x='season', y='sum', data=df_clean_day, ax=ax)
    ax.set_title('Pengaruh Cuaca Buruk Terhadap Permintaan Sepeda per Hari', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Musim', fontsize=15)
    ax.set_ylabel('Rata-rata Permintaan Sepeda', fontsize=15)

    st.pyplot(fig)

def visual_holiday(df_clean_day):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(x='holiday', y='sum', data=df_clean_day, ax=ax)
    ax.set_title('Pengaruh Hari Libur Terhadap Penggunaan Sepeda', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Hari Libur', fontsize=15)
    ax.set_ylabel('Rata-rata Permintaan Sepeda', fontsize=15)

    st.pyplot(fig)