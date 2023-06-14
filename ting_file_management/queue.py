from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicializa a fila"""
        self._queue = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self._queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self._queue) == 0:
            return None
        return self._queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]
