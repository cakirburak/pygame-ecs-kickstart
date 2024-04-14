from components import Collision, Transform, Shape

class Entity:
    def __init__(self, e_id, tag):
        self.__id         = e_id
        self.__tag        = tag
        self.__alive      = True
        self.c_transform  = Transform()
        self.c_collision  = Collision()
        self.c_shape      = Shape()

    def get_tag(self):
        return self.__tag

    def is_alive(self):
        return self.__alive

    def destroy(self):
        self.__alive = False
