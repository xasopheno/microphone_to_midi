import numpy
import aubio
import shutil
import pyaudio
import math


class StreamToFrequency:
    def __init__(self, show_volume=False, store=None):
        self.terminal_width = self.get_screen_width()
        self.store = store
        self.show_volume=show_volume
        self.pDetection = aubio.pitch("yinfft", 2048, 2048, 44100)
        self.pDetection.set_unit("midi")
        self.pDetection.set_silence(-40)
        self.pDetection.set_tolerance(.4)

        self.volume_threshold = 6
        self.acceptable_confidence = 1

    def get_screen_width(self):
        width = shutil.get_terminal_size((80, 20)).columns
        return width

    def callback(self, in_data, frame_count, time_info, status):
        samples = numpy.fromstring(in_data,
                                   dtype=aubio.float_type)

        prediction = int(self.pDetection(samples)[0])

        volume = numpy.sum(samples ** 2) / len(samples)

        self.store.note = prediction
        self.store.volume = volume

        if self.show_volume:
            self.__display_volume(volume)

        return in_data, pyaudio.paContinue

    def __display_volume(self, volume):
        width = self.terminal_width
        bar = ' ' + "-" * (int(volume * 100))
        if len(bar) > width - 20:
            bar = ' ' + "-" * (width - 20)
        print(str(volume) + bar)

    @staticmethod
    def scale_velocity(volume):
        volume = round(volume, 6) * 10 ** 3
        volume = math.log(volume)
        volume *= 15
        if volume > 127:
            volume = 127
        if volume < 0:
            volume = 0

        return volume
