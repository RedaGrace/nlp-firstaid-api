

SAVED_MODEL_PATH = ''

class _nlp_model:
    def predict(self, file_path):
      pass
     
    def preprocess(self, file_path):
      pass
    
    


def nlp_model():
    """Factory function for _nlp_model class.
    :return _nlp_model._instance (_nlp_model):
    """

    # ensure an instance is created only the first time the factory function is called
    if _nlp_model._instance is None:
        _nlp_model._instance = _nlp_model()
        _nlp_model.model = tf.keras.models.load_model(SAVED_MODEL_PATH)
    return _nlp_model._instance


if __name__ == "__main__":

    # create 2 instances of the model service
    model = nlp_model()
    model_1 = nlp_model()

    # check that different instances of the model service point back to the same object (singleton)
    assert model is model_1

    # make a prediction
    first_aid_instructions = model.predict(file_path)
    print(first_aid_instructions)    
