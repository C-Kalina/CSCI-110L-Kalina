import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sx = 1000   # Desired physical surface size, in pixels.
    surface_sy = 800

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sx, surface_sy))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        some_color = (0, 255, 100)        # A color is a mix of (Red, Green, Blue)
        
        for i in range(100):
            main_surface.set_at((100+i, 100+i), some_color)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

if __name__ == "__main__":
    main()