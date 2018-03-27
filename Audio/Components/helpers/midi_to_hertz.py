def midi_to_hertz(midi):
    if midi == 0:
        return 0
    f = 2**((midi-69)/12) * 440
    return f
