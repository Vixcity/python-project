import pygame
from pygame import *
from sys import exit

WIDTH, HEIGHT = 600, 480
FPS = 60


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵基类"""

    def __init__(self, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 加载图像 一个30*30的绿色小方块
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = GameSprite()
    # 事件队列
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        clock.tick(30)

        pressed_keys = pygame.key.get_pressed()
        # 屏幕背景色
        screen.fill((0, 0, 0))
        # 将我们的小方框绘制到屏幕中
        screen.blit(game.image, game.rect)
        # 调用update方法来触发事件
        game.update(pressed_keys)

        pygame.display.flip()


if __name__ == '__main__':
    main()