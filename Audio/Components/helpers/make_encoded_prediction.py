import numpy as np


def encode_phrase_for_prediction(unencoded_phrase, category_index, n_categories, n_time_steps):
    encoded_prediction = np.zeros((1, n_time_steps, n_categories))
    for t, event in enumerate(unencoded_phrase):
        encoded_prediction[0, t, category_index[event]] = 1

    return encoded_prediction


def make_encoded_prediction(model, phrases, categorized_variables, lookup_indicies, n_time_steps):
    encoded_note_prediction = \
        encode_phrase_for_prediction(unencoded_phrase=phrases['note_phrase'],
                                     category_index=lookup_indicies['note_index'],
                                     n_categories=len(categorized_variables['note_categories']),
                                     n_time_steps=n_time_steps)

    encoded_length_prediction = \
        encode_phrase_for_prediction(unencoded_phrase=phrases['length_phrase'],
                                     category_index=lookup_indicies['lengths_index'],
                                     n_categories=len(categorized_variables['length_categories']),
                                     n_time_steps=n_time_steps)

    prediction = model.predict([encoded_note_prediction, encoded_length_prediction], verbose=0)

    return prediction
