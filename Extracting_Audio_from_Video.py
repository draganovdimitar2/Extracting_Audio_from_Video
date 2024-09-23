from moviepy.editor import VideoFileClip

# Load the video clip 
try:
    video_clip = VideoFileClip(# enter the path of the video clip here)
except Exception as e:
    print("An error occurred while loading the video clip:", e)
else:
    try:
        # Extract the audio from the video clip
        audio_clip = video_clip.audio

        # Write the audio to a separate file in a choosen location
        audio_clip.write_audiofile(# enter the path of the audio file here)

        # Close the video and audio clips
        audio_clip.close()
        video_clip.close()

        print("Audio extraction successful!")
    except Exception as e:
        print("An error occurred while extracting or writing the audio:", e)