import time
import rtmidi
import os.path
current_path = os.getcwd()


class MidiPlayer:
    def __init__(self, synth=None):
        self.synth = synth
        self.midi_out = self.setupMidi()

    def setupMidi(self):
        midi_out = rtmidi.MidiOut()
        available_ports = midi_out.get_ports()
        print(available_ports)
        midi_out.open_port(1)
        return midi_out

    def play(self, num, length, velocity=100):
        if num == 0:
            time.sleep(length)
        else:
            if self.synth == 'Volca':
                self.play_volca(num, length, velocity)
            else:
                self.play_synth(num, length, velocity)

    def play_synth(self, num, length, velocity=100):
        note_on = [0x90, num, velocity]
        note_off = [0x80, num, 0]
        self.midi_out.send_message(note_on)
        time.sleep(length)
        self.midi_out.send_message(note_off)

    def play_volca(self, num, length, velocity=100):
        velocity = [0xb0, 0x29, velocity]
        note_on = [0x90, num, 1]
        note_off = [0x80, num, 0]
        self.midi_out.send_message(velocity)
        self.midi_out.send_message(note_on)
        time.sleep(length)
        self.midi_out.send_message(note_off)

    def del_midiout(self):
        del self.midi_out


if __name__ == '__main__':
    player = MidiPlayer()
