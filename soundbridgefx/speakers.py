import soco
import json

class Speakers:

    def __init__(self):
        self.speakers = []
        print(self.speakers)
        self.populate()

    def populate(self):
        speakers = soco.discover()
        for speaker in speakers:
            self.speakers.append(Speaker(speaker))
        print(self.speakers)

    def get_all_speakers(self):
        return self.speakers

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Speaker:
    def __init__(self, speaker):
        self.speaker = speaker
        self.player_name = self.speaker.player_name
        self.ip_addres = self.speaker.ip_address
        print(self.player_name, self.ip_addres)

    def play_stream(self):
        self.speaker.play_uri(uri="http://192.168.1.21:8889/stream.mp3")
