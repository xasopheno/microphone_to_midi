import pyaudio
import time
import random

from Audio.Components.MidiPlayer import MidiPlayer
from Audio.Components.StreamToFrequency import StreamToFrequency
from Audio.Components.Store import Store

from Audio.Components.helpers.logger import logger
import constants


class Generator:
    def __init__(self, args=None):
        self.arguments = args
        self.play_midi = args.play_midi
        self.show_prediction = args.display_prediction
        self.display_volume = args.display_volume
        self.filtered = args.filtered

        self.store = Store()
        self.detector = StreamToFrequency(
            store=self.store,
            show_volume=self.display_volume
        )

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=constants.sample_rate,
                                  frames_per_buffer=constants.chunk_size,
                                  input=True,
                                  output=False,
                                  stream_callback=self.detector.callback)


        """Players"""
        self.player = self.setup_midi_player()

    def setup_midi_player(self):
        player = None
        if self.play_midi:
            try:
                player = MidiPlayer(synth='other')
                logger('Connected')
            except:
                print('No midi destinations!')
        return player

    def generate(self):
        while True:
            self.play()
            time.sleep(0.01)

    def beyond_threshold(self):
        threshold = True
        if self.filtered:
            threshold = self.store.new_note
        return threshold

    def play(self):
        note = self.store.note
        volume = self.store.volume
        length = 0.01

        if volume > 10:
            volume += 30

        print(note, length, volume)
        self.player.play(note, length, volume)
        
        self.store.past_prediction = self.store.values
