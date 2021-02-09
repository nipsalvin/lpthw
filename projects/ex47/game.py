class Room(object):

    def __init__(self, name, description):
        self.name = name
        sself.description = description
        self.path = []

    def go(self, direction):
        return self.path.get(direction, None)

    def add_path(self, path):
        self.paths.update(paths)
        
