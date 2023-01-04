import json
import logging
from soundbridgefx import (
    sonosspeakers
)

_LOGGER = logging.getLogger(__name__)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

        """
        A single sonos speaker, lowest level of abstraction.

        Returns:
            _type_: _description_
        """
class Speakers:
    def __init__(self):
        self.speakers = []
        self.sonos_speakers = sonosspeakers.SonosSpeakers()
        self.speakers.append(self.sonos_speakers)
        self.populate()

    def populate(self):
        json.dumps(self.sonos_speakers.reprJSON(), cls=ComplexEncoder)

    def reprJSON(self):
        return dict(all_speakers=self.speakers)

    def get_all_speakers(self):
        return json.dumps(self.reprJSON(), cls=ComplexEncoder)

    def play_stream(self, speakers):
        response = self.sonos_speakers.play_stream(speakers)
        return response

    def play_party(self, speakers):
        response = self.sonos_speakers.play_party(speakers)
        return response

    def pause(self, speakers):
        response = self.sonos_speakers.pause(speakers)
        return response

    def stop(self, speakers):
        response = self.sonos_speakers.stop(speakers)
        return response

    def set_volume(self, speakers):
        response = self.sonos_speakers.set_volume(speakers)
        return response
