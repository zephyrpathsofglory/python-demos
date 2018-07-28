class myclass(object):
    def __init__(self):
        self.is_good = True


class childclass(myclass):
    def __init__(self, is_man):
        self.is_man = is_man

    @classmethod
    def can_speak(cls):
        return True

    @property
    def man(self):
        return self.is_man


obj = childclass(True)
print(obj.is_good)