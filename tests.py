class Myclass(object):
    def __init__(self):
        self.is_good = True


class Childclass(Myclass):
    def __init__(self, is_man):
        self.is_man = is_man
        super().__init__() # need if you want is_good as attribute

    @classmethod
    def can_speak(cls):
        return True

    @property
    def man(self):
        return self.is_man


obj = Childclass(True)
print(obj.man)
print(Childclass.can_speak())
print(obj.is_good)