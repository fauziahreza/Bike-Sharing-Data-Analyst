import datetime
import pandas as pd
import streamlit as st
from func import (
  stats_year, season_impact, holiday_impact, weather_impact, 
  visual_holiday, visual_season, visual_weathersit,
  year, month, hour, sidebar
)

if __name__ == '__main__':
  st.header('Bike Sharing Dashboard 🚵🏻‍♀️')

  DF_CLEAN_DAY_PATH = 'D:\Documents\Pelatihan\Dicoding\Analisis data menggunakan python\dataset\clean_day.csv'
  DF_HOUR_PATH = 'D:\Documents\Pelatihan\Dicoding\Analisis data menggunakan python\dataset\hour.csv'

  df_clean_day = pd.read_csv(DF_CLEAN_DAY_PATH)
  df_hour = pd.read_csv(DF_HOUR_PATH)

  date = sidebar(df_clean_day)
  if len(date) == 2:
    df_main = df_clean_day[
      (df_clean_day["dteday"] >= str(date[0])) & (df_clean_day["dteday"] <= str(date[1]))
    ]
  else:
    df_main = df_clean_day[
      (df_clean_day["dteday"] >= str(st.session_state.date[0])) & (
        df_clean_day["dteday"] <= str(st.session_state.date[1])
      )
    ]

  with st.container():
    st.subheader('Total Sewa Sepeda')
    tab_year, tab_month, tab_hour = st.tabs(['Tahun', 'Bulan',  'Jam'])
    df_year = stats_year(df_main)

    with tab_year:
      year(df_year)

    with tab_month:
      month(df_main)

    with tab_hour:
      hour(df_hour)

  with st.container():
    st.subheader('Pengaruh Cuaca Buruk Terhadap Permintaan Sepeda')
    df_weathersit = weather_impact(df_main)
    visual_weathersit(df_weathersit)

    with st.expander('Keterangan'):
      st.write(
        """
        `Mist + Cloudy`: Berkabut dan berawan  
        `Light Snow`: Sedikit bersalju  
        `Clear`: Cuaca cerah
        `Heavy Rain`: Hujan Deras
        """
      )

  with st.container():
    st.subheader('Tren Musiman dalam Penggunaan Sepeda')
    df_season = season_impact(df_main)
    visual_season(df_season)

    with st.expander('Keterangan'):
      st.write(
        """
        `Fall`: Musim Gugur  
        `Springer`: Musim Semi  
        `Summer`: Musim Panas
        `Winter`: Musim Dingin
        """
      )

  with st.container():
    st.subheader('Pengaruh Hari Libur Terhadap Penggunaan Sepeda')
    df_holiday = holiday_impact(df_main)
    visual_holiday(df_holiday)

    with st.expander('Keterangan'):
      st.write(
        """
        `Holiday`: Hari Libur  
        `Non Holiday`: Bukan Hari Libur 

        """
      )

  st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">', unsafe_allow_html=True)
  year_now = datetime.date.today().year
  footer_text = (
      f"© {year_now} Bike Sharing Data Analyst. "
      "Made with ❤ by Fauziah Reza Oktaviyani | "
      '<a href="https://github.com/fauziahreza" target="_blank"><i class="ti ti-brand-github"></i></a> | '
      '<a href="https://www.linkedin.com/in/fauziah-reza-oktaviyani-085a16150/" target="_blank"><i class="ti ti-brand-linkedin"></i></a>'
  )
  st.markdown(footer_text, unsafe_allow_html=True)