import soco
import logging
from soundbridgefx import (sonosspeaker)


_LOGGER = logging.getLogger(__name__)


"""
A class to hold all information about Sonos Speakers.
Please not the plural version of this, this class will scan for all sonos speakers on the network and manage them using this class.

Returns:
_type_: _description_
"""
class SonosSpeakers:

    def __init__(self):
        self.sonos_speakers_dict = []
        self.sonos_speakers = []
        self.N_speakers = None
        self.populate()

    """
    Populate the class with all sonos speakers on the network.
    """
    def populate(self):
        speakers = soco.discover()
        for speaker in speakers:
            sonos_speaker = sonosspeaker.SonosSpeaker(speaker)
            my_dict = {
                "player_name": sonos_speaker.player_name,
                "object": sonos_speaker
            }
            self.sonos_speakers_dict.append(my_dict)
            self.sonos_speakers.append(sonos_speaker)

        self.N_speakers = self.sonos_speakers_dict.__len__

    @property
    def update(self):
        for speaker in self.sonos_speakers:
            speaker.update()

    ##TODO refactor

    """Gets the requested speaker index of all speakers.
    """

    def get_speaker_index(self, speakers):
        stream_speakers_object = []

        for index, sonos_speaker in enumerate(self.sonos_speakers_dict):
            speaker_name = sonos_speaker['player_name']
            if speaker_name == speakers[0]:
                _LOGGER.debug(index, sonos_speaker)
                stream_speakers_object.append(index)

        return stream_speakers_object

    def play_stream(self, sonos_speakers_stream):
        for i in self.get_speaker_index(sonos_speakers_stream):
            self.sonos_speakers[i].play_stream()

    def play_party(self, sonos_speakers_stream):                
        _LOGGER.debug("Requested party play")

    def pause(self, sonos_speakers_stream):
        for i in self.get_speaker_index(sonos_speakers_stream):
            self.sonos_speakers[i].play()

    def stop(self, sonos_speakers_stream):
        for i in self.get_speaker_index(sonos_speakers_stream):
            self.sonos_speakers[i].stop()

    def stop(self, sonos_speakers_stream):
        for i in self.get_speaker_index(sonos_speakers_stream):
            self.sonos_speakers[i].stop()

    def set_volume(self, sonos_speakers_stream):
        for i in self.get_speaker_index(sonos_speakers_stream):
            self.sonos_speakers[i].set_volume()

    def reprJSON(self):
        return dict(sonos_speakers=self.sonos_speakers_dict)
