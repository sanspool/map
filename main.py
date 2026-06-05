# main.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 1. 웹 페이지 설정
st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("🏔️2026 학교 등산 행사 안내 지도")
st.markdown("우리 동아리가 직접 발로 뛰며 만든 코스 가이드 입니다.")
st.markdown("왼쪽 메뉴에서 코스를 선택하고 행사에 참여해 보세요.")
st.markdown("# 큰 제목 ")
st.markdown("## 작은 제목 ")
st.markdown("**굵은 글씨**와 *이텔릭체* ")

st.header("헤더입니다")
st.subheader("서브헤더입니다")
st.caption("캡션입니다")
st.code("print('hello world')")

st.text("userskin1")

# 2. 데이터 읽어오기(데이터 수집 csv)
df = pd.read_csv('듬배산등산경로.csv', encoding='UTF-8')
df_latlon = df[['위도','경도']]
df_latlon = df_latlon.rename(columns={'위도':'lat', '경도':'lon'})
print(df_latlon)
#st.map(df_latlon)

# 지도 생성 및 마커 표시 (지도 시각화 단계)
m = folium.Map(
    location = [37.40583317, 126.7214872],
    zoom_start=13
)

for i in range(len(df)):
    folium.Marker(
        location=df_latlon,
        popup = df.iloc[i]['위치명'],
        tooltip="클릭해보세요",
        icon = folium.Icon(color='cadetblue', icon='info-sign')
        #{'darkgreen', 'purple', 'blue', 'white', 'darkblue', 'red', 'darkred', 'lightgreen', 'pink', 'cadetblue', 'lightred', 'darkpurple', 'lightgray', 'gray', 'black', 'lightblue', 'green', 'orange', 'beige'}
    ).add_to(m)

# 4. 화면 출력
st_folium(m, width=700, height=500)
