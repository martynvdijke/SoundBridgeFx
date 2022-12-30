import subprocess


def main():
    try:
        p = subprocess.Popen(
            "cvlc -vvvv pulse://alsa_output.pci-0000_0b_00.4.iec958-stereo.monitor --no-sout-video --sout '#transcode{acodec=mp3,ab=128,channels=2}:std{access=http,dst=0.0.0.0:8889/stream.mp3}'", stdout=subprocess.PIPE, shell=True)
    except:
        _LOGGER.error("Could not start cvlc")


main()
