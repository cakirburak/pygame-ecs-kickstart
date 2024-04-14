from typing import Dict, List
from entity import Entity

class EntityManager:
    def __init__(self):
        # all of the entities
        self.__entities: List[Entity]                 = []
        # to be able access specific type of entities { "player", "enemy", "tree", "floor", .....}
        # sacriface some memory to gain development efficiency
        self.__entities_dict: Dict[str, List[Entity]] = {}
        self.__to_add: List[Entity]                   = []
        self.__total_entites                          = 0

    def update(self) -> None:
        # add newly created entites
        for e in self.__to_add:
            # add them to entities list
            self.__entities.append(e)
            
            # add them to dict list
            if e.get_tag() in self.__entities_dict:
                self.__entities_dict[e.get_tag()].append(e)
            else:
                entity_list = self.__entities_dict.get(e.get_tag(), [])
                entity_list.append(e)
                self.__entities_dict[e.get_tag()] = entity_list

        self.__to_add.clear()

        # remove dead entites from entities
        for e in self.__entities:
            if not e.is_alive():
                self.__entities.remove(e)

        # remove dead entites from entity dict
        for tag in self.__entities_dict:
            for e in self.__entities_dict[tag]:
                if not e.is_alive():
                    self.__entities_dict[tag].remove(e)

    def add_entity(self, tag:str) -> Entity:
        entity = Entity(++self.__total_entites, tag)
        self.__to_add.append(entity)
        return entity

    def get_entities(self, *args) -> List[Entity]:
        if len(args) == 0:
            return self.__entities
        else:
            return self.__entities_dict[args[0]]

