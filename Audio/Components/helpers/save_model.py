def save_model(trained_model, name):
    """serialize model to JSON"""
    model_json = trained_model.to_json()
    with open(name + ".json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    trained_model.save_weights(name + ".h5")
    print("Saved " + name + ".json and " + name + ".h5 to disk")
