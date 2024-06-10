from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = YsortCameraGroup()
        self.create_map()

    def create_map(self):
        # for row_index, row in enumerate(WORLD_MAP):
        #     for col_index, col in enumerate(row):
        #         x = col_index * TILESIZE
        #         y = row_index * TILESIZE
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
        #         elif col == 'p':
        #             self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
        self.player = Player((2000,1430),[self.visible_sprites],self.obstacle_sprites)
    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        #self.obstacle_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        #debug(self.player.direction)


class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2(100,200)
        self.floor_surface = pygame.image.load('assets/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0,0))

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height


        #floor drawing
        floor_offset = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset)

        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
        #for sprite in self.sprites():
            rect_offset = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, rect_offset) # blit = block image transfer