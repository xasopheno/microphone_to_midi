from Audio.Components.helpers.sample import sample


def decode_prediction(encoded_prediction, lookup_index, temperature):
    encoded_index_from_sample = sample(encoded_prediction, temperature)
    decoded_prediction = lookup_index[encoded_index_from_sample]
    return decoded_prediction


def decode_predictions(encoded_prediction, lookup_indicies, temperature=1.0):
    encoded_note_prediction = encoded_prediction[0][0]
    encoded_length_prediction = encoded_prediction[1][0]

    note_prediction = decode_prediction(
        encoded_prediction=encoded_note_prediction,
        lookup_index=lookup_indicies['index_note'],
        temperature=temperature
    )

    length_prediction = decode_prediction(
        encoded_prediction=encoded_length_prediction,
        lookup_index=lookup_indicies['index_lengths'],
        temperature=temperature
    )

    predictions = {
        'note_prediction': note_prediction,
        'length_prediction': length_prediction,
    }

    return predictions
