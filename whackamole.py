import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_width, mole_height = mole_image.get_size()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x, mole_y = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (mole_x <= mouse_x < mole_x + 32 and mole_y <= mouse_y < mole_y + 32):
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32
            screen.fill("light green")
            for x in range(0, 640, 32):
                pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, (200, 200, 200), (0, y), (640, y))
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
