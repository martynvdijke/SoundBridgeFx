import logging
import subprocess
import soundcard as sc

_LOGGER = logging.getLogger(__name__)


def get_audio_device():
    default_speaker = sc.default_speaker()


def main():
    default_speaker = get_audio_device()
    try:
        p = subprocess.Popen(
            "systemctl start raspotify",
            stdout=subprocess.PIPE,
            shell=True)
    except:
        _LOGGER.error("Could not start cvlc")
