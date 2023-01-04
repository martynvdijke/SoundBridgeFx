import subprocess
import soundcard as sc
import logging

_LOGGER = logging.getLogger(__name__)


def get_audio_device():
    default_speaker = sc.default_speaker()


def main():
    default_speaker = get_audio_device()
    try:
        p = subprocess.Popen(
            "cvlc -vvvv pulse://alsa_output.pci-0000_0b_00.4.iec958-stereo.monitor --no-sout-video --sout '#transcode{acodec=mp3,ab=128,channels=2}:std{access=http,dst=0.0.0.0:8889/stream.mp3}'",
            stdout=subprocess.PIPE,
            shell=True)
    except:
        _LOGGER.error("Could not start cvlc")


main()
