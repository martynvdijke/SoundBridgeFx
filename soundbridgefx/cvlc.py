import subprocess
import soundcard as sc
import json
import logging

_LOGGER = logging.getLogger(__name__)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

        """
        A single sonos speaker, lowest level of abstraction.

        Returns:
            _type_: _description_
        """
class CLV:

    def __init__(self) -> None:
        self.speakers = sc.all_speakers()
        self.microphones = sc.all_microphones()
        self.current_speaker = sc.default_speaker()
        self.current_microphone = sc.default_microphone()
        pass

    def get_all_speakers(self):
        self.speakers
    
    def get_all_micrphones(self):
        self.microphones
    
    def get_current_speaker(self):
        self.current_speaker

    def get_current_micrphone(self):
        self.current_microphone
    

    def main(self):
        default_speaker = self.current_speaker
        try:
            p = subprocess.Popen(
                "cvlc -vvvv pulse://alsa_output.pci-0000_0b_00.4.iec958-stereo.monitor --no-sout-video --sout '#transcode{acodec=mp3,ab=128,channels=2}:std{access=http,dst=0.0.0.0:8889/stream.mp3}'",
                stdout=subprocess.PIPE,
                shell=True)
        except:
            _LOGGER.error("Could not start cvlc")