import soco
import logging
from soundbridgefx.sonos.speaker import SonosSpeaker
from soundbridgefx.metaclasses.singleton import Singleton

_LOGGER = logging.getLogger(__name__)


"""
A class to hold all information about Sonos Speakers.
Please not the plural version of this, this class will scan for all sonos speakers on the network and manage them using this class.

Returns:
_type_: _description_
"""


class SonosController(metaclass=Singleton):
    
    def __init__(self):
        self.speakers_dict = []
        self.speakers = []
        self.N_speakers = None
        #self.populate()

    """
    Populate the class with all sonos speakers on the network.
    """
    # def populate(self):
    #     soco_speakers = soco.discover()
    #     for speaker in soco_speakers:
    #         speaker = SonosSpeaker(speaker)

    #         self.speakers_dict.append({
    #             "player_name": speaker.player_name,
    #             "object": speaker,
    #         })

    #         self.speakers.append(speaker)

    #     self.N_speakers = len(self.speakers_dict)

    # @property
    # def update(self):
    #     for speaker in self.speakers:
    #         speaker.update()

    # ##TODO refactor

    # """Gets the requested speaker index of all speakers.
    # """

    # def get_speaker_index(self, speakers):
    #     stream_speakers_object = []

    #     for index, sonos_speaker in enumerate(self.speakers_dict):
    #         speaker_name = sonos_speaker["player_name"]
    #         if speaker_name == speakers[0]:
    #             stream_speakers_object.append(index)

    #     return stream_speakers_object

    # def play_stream(self, sonos_speakers_stream):
    #     for i in self.get_speaker_index(sonos_speakers_stream):
    #         self.speakers[i].play_stream()

    # def play_party(self, sonos_speakers_stream):
    #     _LOGGER.debug("Requested party play")

    # def pause(self, sonos_speakers_stream):
    #     for i in self.get_speaker_index(sonos_speakers_stream):
    #         self.speakers[i].play()

    # def stop(self, sonos_speakers_stream):
    #     for i in self.get_speaker_index(sonos_speakers_stream):
    #         self.speakers[i].stop()

    # def set_volume(self, sonos_speakers_stream):
    #     for i in self.get_speaker_index(sonos_speakers_stream):
    #         self.speakers[i].set_volume()

    # def reprJSON(self):
    #     return dict(sonos_speakers=self.speakers_dict)
