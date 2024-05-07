from twisted.internet.protocol import Protocol

clients = []


class Spreader(Protocol):
    def __init__(self, factory):
        self.factory = factory
