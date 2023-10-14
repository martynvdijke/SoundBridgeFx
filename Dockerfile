FROM kasmweb/core-debian-bullseye:1.14.0-rolling

USER root

ENV HOME /home/kasm-default-profile
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

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
    python3-pyaudio 
RUN pip install ledfx soco

RUN chown 1000:0 $HOME
RUN $STARTUPDIR/set_user_permission.sh $HOME

ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000


# ENTRYPOINT [ "mkchromecast" ]