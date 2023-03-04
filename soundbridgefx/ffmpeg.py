import subprocess
import soundcard as sc
import logging

_LOGGER = logging.getLogger(__name__)


# class FFMPEG:

#     def __init__(self) -> None:
#         print("test")
#         self.speakers = sc.all_speakers()
#         self.microphones = sc.all_microphones()
#         self.current_speaker = sc.default_speaker()
#         self.current_microphone = sc.default_microphone()
#         pass

#     def get_all_speakers(self):
#         self.speakers
    
#     def get_all_micrphones(self):
#         self.microphones
    
#     def get_current_speaker(self):
#         self.current_speaker

#     def get_current_micrphone(self):
#         self.current_microphone
    

def main():

    # default_speaker = self.current_speaker
    try:
        p = subprocess.Popen(
            "ffmpeg -f alsa -ac 2 -i default -acodec libmp3lame -ab 256k -f mp3 stream.mp3",
            stdout=subprocess.PIPE,
            shell=True)
    except:
        _LOGGER.error("Could not start ffmpeg")