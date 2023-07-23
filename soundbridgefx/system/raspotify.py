import logging
import subprocess
import soundcard as sc

_LOGGER = logging.getLogger(__name__)

def main():
    try:
        p = subprocess.Popen(
            "librespot",
            stdout=subprocess.PIPE,
            shell=True)
    except:
        _LOGGER.error("Could not start cvlc")
