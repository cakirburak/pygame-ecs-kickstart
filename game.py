import pygame as pg
from entity_manager import EntityManager

class Game:
    def __init__(self, base_res_w, base_res_h):
        self.screen = pg.Surface
        self.render_window = pg.Rect
        self.render_scale = 1
        self.game_res = 16/9

        self.e_manager = EntityManager()

        self.is_running = True
        self.is_paused = False

        self.game_init(base_res_w, base_res_h)

    def game_init(self, base_res_w, base_res_h):
        # init pygame
        pg.init()

        # get user display info
        display_info = pg.display.Info()
        display_res = display_info.current_w / display_info.current_h

        # set render window and render scale
        if display_res == self.game_res:
            print("FullScreen")
            self.render_window = pg.Rect(0,0, display_info.current_w, display_info.current_h) 
            self.render_scale = display_info.current_w / base_res_w
        elif display_res < self.game_res:
            self.render_window = pg.Rect( 0, int((display_info.current_h - display_info.current_w*(9/16))/2 ), display_info.current_w, display_info.current_w*(9/16),) 
            self.render_scale = display_info.current_w / base_res_w
            print("User Display is Higher")
        else:
            self.render_window = pg.Rect(int((display_info.current_w - display_info.current_h*(16/9))/2), 0, display_info.current_h*(16/9), display_info.current_h) 
            self.render_scale = display_info.current_h / base_res_h
            print("User Display is Wider")

        # set screen
        self.screen = pg.display.set_mode((display_info.current_w, display_info.current_h), flags=pg.FULLSCREEN | pg.NOFRAME)

        # testing entity manager
        entity = self.e_manager.add_entity("background")
        entity.c_transform(pg.Vector2(0+self.render_window.x, 0+self.render_window.y))
        entity.c_shape(pg.Vector2(640*self.render_scale, 360*self.render_scale), pg.Color(0, 0, 255))
        entity2 = self.e_manager.add_entity("player")
        entity2.c_transform(pg.Vector2(0+self.render_window.x, 0+self.render_window.y), pg.Vector2(2, 1), 1)
        entity2.c_shape(pg.Vector2(32*self.render_scale, 32*self.render_scale), pg.Color(255, 0, 0))

    def run(self):
        clock = pg.time.Clock()
        while self.is_running:
            self.e_manager.update()
            self.s_collision()
            self.s_movement()
            self.s_render()
            self.s_user_input()
            clock.tick(60)  # limits FPS to 60
        pg.quit()

    def s_collision(self):
        pass

    def s_movement(self):
        for e in self.e_manager.get_entities("player"):
            e.c_transform.pos += e.c_transform.velocity

    def s_render(self):
        pg.Surface.fill(self.screen, "black")
        for e in self.e_manager.get_entities("background"):
            pg.draw.rect(self.screen, e.c_shape.fill_color, pg.Rect(e.c_transform.pos.x, e.c_transform.pos.y, e.c_shape.size.x, e.c_shape.size.y))
        
        for e in self.e_manager.get_entities("player"):
            pg.draw.rect(self.screen, e.c_shape.fill_color, pg.Rect(e.c_transform.pos.x, e.c_transform.pos.y, e.c_shape.size.x, e.c_shape.size.y))

        pg.display.flip()

    def s_user_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())

