import streamlit as st
from pytube import YouTube

import whisper


# Function to download YouTube video
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        stream.download(output_path="/downloads", filename="video.mp4")
        st.success("Video berhasil diunduh!")
    except Exception as e:
        st.error(f"Error: {e}")


def transcribe_audio():
    model = whisper.load_model("base")
    result = model.transcribe("/download/video.mp4", language="id")

    print(result["text"])
    return result


# Streamlit UI
def main():
    st.title("Downloader Video YouTube")

    # Input URL
    url = st.text_input("Masukkan URL video YouTube:")

    # Button to download
    if st.button("Download"):
        if url:
            download_video(url, ".")
            st.write(transcribe_audio())


if __name__ == "__main__":
    main()
