def generate_phrases(category_index, n_time_steps, semi_redundancy_step):
    category_xs = []
    category_ys = []
    for i in range(0, len(category_index) - n_time_steps, semi_redundancy_step):
        category_xs.append(category_index[i: i + n_time_steps])
        category_ys.append(category_index[i + n_time_steps])

    return category_xs, category_ys
