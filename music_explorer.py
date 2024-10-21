import streamlit as st
import pandas as pd

# 샘플 데이터
music_data = {
    "Pop": ["Taylor Swift", "Dua Lipa", "Ariana Grande"],
    "Rock": ["Foo Fighters", "Queen", "Nirvana"],
    "Hip-Hop": ["Kendrick Lamar", "Drake", "Lil Nas X"],
    "Jazz": ["Miles Davis", "John Coltrane", "Louis Armstrong"],
    "Classical": ["Beethoven", "Mozart", "Bach"],
}

# 비슷한 아티스트 데이터
similar_music = {
    "Taylor Swift": ["Olivia Rodrigo", "Halsey", "Bebe Rexha"],
    "Dua Lipa": ["Rita Ora", "Charli XCX", "Lizzo"],
    "Ariana Grande": ["Maroon 5", "Sia", "Jason Derulo"],
    "Foo Fighters": ["Nirvana", "Pearl Jam", "Linkin Park"],
    "Queen": ["David Bowie", "Guns N' Roses", "Led Zeppelin"],
    "Kendrick Lamar": ["J Cole", "Drake", "Tyler, The Creator"],
    "Drake": ["Lil Wayne", "Future", "Post Malone"],
    "Lil Nas X": ["Megan Thee Stallion", "Doja Cat", "Cardi B"],
    "Miles Davis": ["John Coltrane", "Dizzy Gillespie", "Herbie Hancock"],
    "Beethoven": ["Mozart", "Chopin", "Bach"],
}

# 세션 상태 초기화
if 'saved_music' not in st.session_state:
    st.session_state.saved_music = []

# 앱 제목
st.title("음악 탐색기")

# 장르 검색 기능 추가
genre_search = st.text_input("장르를 검색하세요:", "")
filtered_genres = [genre for genre in music_data.keys() if genre_search.lower() in genre.lower()]

# 장르 선택
selected_genre = st.selectbox("장르를 선택하세요:", filtered_genres if filtered_genres else list(music_data.keys()))

# 선택한 장르에 따른 아티스트 출력
if selected_genre:
    st.subheader(f"{selected_genre} 장르 아티스트")
    artists = music_data[selected_genre]

    # 아티스트 검색 기능 추가
    artist_search = st.text_input("아티스트를 검색하세요:", "")
    filtered_artists = [artist for artist in artists if artist_search.lower() in artist.lower()]

    for artist in filtered_artists:
        st.write(artist)

    # 아티스트 선택
    if filtered_artists:
        selected_artist = st.selectbox("아티스트를 선택하세요:", filtered_artists)

        # 선택한 아티스트에 대한 비슷한 음악 추천
        st.subheader(f"{selected_artist}와 비슷한 아티스트")
        if selected_artist in similar_music:
            similar_artists = similar_music[selected_artist]
            for similar_artist in similar_artists:
                st.write(similar_artist)
        else:
            st.write("추천할 비슷한 아티스트가 없습니다.")

        # 음악 저장 기능
        if st.button("추천 아티스트 저장하기"):
            if selected_artist not in st.session_state.saved_music:
                st.session_state.saved_music.append(selected_artist)
                st.success(f"{selected_artist}이(가) 저장되었습니다.")
            else:
                st.error("이미 저장된 아티스트입니다.")

# 저장된 음악 목록 표시
st.subheader("저장된 아티스트 목록")
if st.session_state.saved_music:
    saved_music_df = pd.DataFrame(st.session_state.saved_music, columns=["저장된 아티스트"])
    st.dataframe(saved_music_df)
else:
    st.write("저장된 아티스트가 없습니다.")