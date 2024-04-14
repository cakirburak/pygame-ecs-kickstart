class Transform:
    def __init__(self):
        pass

    def __call__(self, *args):
        if len(args) == 3:
            self.pos        = args[0]
            self.velocity   = args[1]
            self.speed      = args[2]
        elif len(args) == 1:
            self.pos        = args[0]

class Collision:
    def __init__(self):
        pass

    def __call__(self, *args):
        if len(args) == 1:
            self.hit_box = args[0]
        else:
            pass

class Shape():
    def __init__(self):
            pass

    def __call__(self, *args):
        if len(args) == 2:
            self.size       = args[0]
            self.fill_color = args[1]
        else:
            pass

