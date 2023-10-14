FROM x11docker/xfce

RUN apt-get update && apt-get install -y \
    avahi-daemon \
    curl \
    ffmpeg \
    gcc \
    libasound-dev \
    libatlas3-base \
    libavformat58 \
    libportaudio2 \
    mkchromecast \
    portaudio19-dev \
    pulseaudio \
    python3 \
    python3-aubio \
    python3-pip \
    python3-pyaudio \
RUN pip install ledfx soco



# ENTRYPOINT [ "mkchromecast" ]