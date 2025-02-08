import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import time
import os

# App Title
st.title("Baixar vídeos do Youtube")

# Instructions
st.write("Copie o link da música e clique no botão")

# YouTube Link Input
youtube_link = st.text_input("Link do Youtube", "", placeholder="Copie o link aqui")

# Centered and Large Button
button_clicked = st.button("Buscar vídeo", use_container_width=True, type="primary")

if button_clicked:
    if youtube_link.strip():
        try:
            # Download the video
            yt = YouTube(youtube_link, on_progress_callback=on_progress)
            st.write(f"Buscando vídeo: {yt.title}")
            time.sleep(2)
            
            ys = yt.streams.get_highest_resolution()
            video_file = ys.download(output_path=".")

            with open(video_file, "rb") as file:
                st.download_button(
                    label="Pronto para baixar: Clique Aqui ✅",
                    data=file,
                    file_name=os.path.basename(video_file),
                    mime="video/mp4",
                    type="primary",
                    icon="✅",
                    use_container_width=True
                )

            os.remove(video_file)
        
        except Exception as e:
            st.error(f"Erro ao baixar o vídeo. Verifique o link e tente novamente.")
            st.error(f"Detalhes do erro: {str(e)}")
    else:
        st.warning("O link não é válido.")
