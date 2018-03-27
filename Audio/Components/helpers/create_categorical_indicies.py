def create_category_indicies(category):
    category_index = dict((c, i) for i, c in enumerate(category))
    index_category = dict((i, c) for i, c in enumerate(category))

    return category_index, index_category
