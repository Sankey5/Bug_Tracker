


class Bug:
    """
    This is the parent bug class that will contain the base information for
    each bug given to the application
    """

    def __init__(self, name, description, priority):
        self.id
        self.name = name
        self.description = description
        self.priority = priority

    # Getters
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority

    # Setters

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setPriority(self, priority):
        self.priority = priority