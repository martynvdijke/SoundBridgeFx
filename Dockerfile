FROM debian:latest

RUN apt-get update
RUN apt-get install -y libc6 systemd libasound2 alsa-utils libpulse0 init-system-helpers python3 python3-pip python3-pyaudio python3-numpy
RUN apt-get -y install curl && curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
RUN pip3 install --upgrade pip
RUN pip install ledfx