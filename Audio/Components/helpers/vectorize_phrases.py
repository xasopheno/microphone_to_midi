import numpy as np


def vectorize_phrases(phrases, n_categories, n_time_steps, lookup_index, next_lookup_index):
    vectorized_x = np.zeros((len(phrases), n_time_steps, n_categories), dtype=np.bool)
    vectorized_y = np.zeros((len(phrases), n_categories), dtype=np.bool)

    for i, phrase in enumerate(phrases):
        for t, event in enumerate(phrase):
            vectorized_x[i, t, lookup_index[event]] = 1
        vectorized_y[i, lookup_index[next_lookup_index[i]]] = 1

    return vectorized_x, vectorized_y
