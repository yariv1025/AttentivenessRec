class ModelCreator:
    """
    :param model - The model used for system training.
    """
    def __init__(self, model):
        self.model = model

    """
    :param database - the database we will train.
    """
    def trainModel(self, database):
        pass

    """
    :param database - .
    """
    def getModel(self, database):
        return self.trainModel(database)