


class ListaDellaSpesa:
    def __init__(self):
        self._list = []
    def add(self, item):
        self._list.append(item)
    def get(self):
        return self._list