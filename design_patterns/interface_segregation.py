class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def play_video(self, video_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def stop_video(self):
            raise NotImplementedError

# Better interfaces as they segregate the audio and video so we can no have mp3 inheriting Audio and AviVideoPlayer inherit VideoPlayer
# and MultiMediaPlayer inheriting both of them
class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError

class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError