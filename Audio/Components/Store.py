import os
import sys
import math
import time
from collections import deque
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Audio.Components.helpers.prepare_ring_buffer import prepare_ring_buffer
import constants

class Store:
    def __init__(self):
        self.__note = 0
        self.__volume = 0
        self.length = 0
        self.past_prediction = self.base_values()
        self.new_note = True
        self.volume_array = []
        self.start_time = time.time()
        self.past_notes_array = deque([0], maxlen=10)
        self.past_length = 0
        self.note_ring_buffer = prepare_ring_buffer(size=constants.n_time_steps)
        self.length_ring_buffer = prepare_ring_buffer(size=constants.n_time_steps)


    @staticmethod
    def base_values():
        return {
            "note": 0,
            "volume": 0,
            "length": 0,
        }

    @property
    def note(self):
        return self.__note

    @property
    def volume(self):
        return self.__volume

    @note.setter
    def note(self, note):
        note = int(note)
        self.past_notes_array.appendleft(note)
        self.__note = note
        self.is_new_note()

    @volume.setter
    def volume(self, volume):
        volume = self.scale_volume(volume)
        volume = int(volume)
        self.volume_array.append(volume)
        self.__volume = volume

    @property
    def values(self):
        return {
            "note": self.most_common(),
            "volume": self.__volume,
            "length": self.length,
        }

    @staticmethod
    def scale_volume(volume):
        volume = round(volume, 6) * 10 ** 3
        if volume == 0:
            volume = 0.001
        volume = math.log(volume)
        volume *= 15
        if volume > 127:
            volume = 127
        if volume < 0:
            volume = 0

        return volume

    def avg_volume(self):
        length = len(self.volume_array)
        total = sum(self.volume_array)
        avg = total/length if length else 0
        return int(avg)

    def most_common(self):
        return max(set(self.past_notes_array), key=self.past_notes_array.count)

    def rounded_length(self):
        raw = time.time() - self.start_time
        if raw < 1:
            return round(raw, 2)
        elif 1 <= raw < 5:
            return round(raw, 1)
        else:
            return 5.0

    def is_new_note(self):
        self.past_prediction = self.values
