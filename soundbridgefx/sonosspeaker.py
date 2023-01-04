import logging

_LOGGER = logging.getLogger(__name__)


class SonosSpeaker:

    def __init__(self, speaker):
        self.speaker = speaker
        self.player_name = self.speaker.player_name
        self.ip_addres = self.speaker.ip_address
        self.speaker_info = self.speaker.get_speaker_info()

        self.current_track_info = self.speaker.get_current_track_info()
        self.current_transport_info = self.speaker.get_current_transport_info()
        self.current_media_info = self.speaker.get_current_media_info()
        _LOGGER.debug(self.player_name, self.ip_addres)

    def __str__(self):
        return str(self.player_name)

    @property
    def update(self):
        self.current_track_info = self.speaker.get_current_track_info()
        self.current_transport_info = self.speaker.get_current_transport_info()
        self.current_media_info = self.speaker.get_current_media_info()

    def play_stream(self):
        _LOGGER.debug("going to play stream")
        self.speaker.play_uri(uri="http://192.168.1.21:8889/stream.mp3",
                              title="SoundBridgeFx stream",
                              force_radio=True)

    def stop(self):
        self.speaker.stop()

    def pause(self):
        self.speaker.pause()

    def set_volume(self):
        vol = 50
        self.speaker.ramp_to_volume(vol)

    def reprJSON(self):
        return dict(player_name=self.player_name,
                    ip_addres=self.ip_addres,
                    current_track_info=self.current_track_info,
                    current_transport_info=self.current_transport_info,
                    current_media_info=self.current_media_info,
                    speaker_info=self.speaker_info,
                    type="sonos")
