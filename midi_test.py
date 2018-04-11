import rtmidi

midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
print(available_ports)
