FROM debian:latest

RUN apt-get update && apt-get install -y ffmpeg python3 python3-pip python3-pyaudio python3-numpy libasound2-plugins
RUN apt-get -y install curl && curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
RUN pip3 install --upgrade pip && pip3 install soundbridgefx

CMD /usr/bin/librespot && soundbridgefx
