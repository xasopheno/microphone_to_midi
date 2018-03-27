def play_generated_phrase(generated_notes, generated_lengths, player):
    for event in range(len(generated_notes)):
        note = generated_notes[event]
        length = generated_lengths[event]
        print(note, '|', length)
        player.play(note, length, 100)
