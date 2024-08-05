import pygame
import sys

def main():
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((800, 600))  # Create a screen with width 800 and height 600
    pygame.display.set_caption("Simple Ball Animation")  # Set window title

    ball_pos = [400, 300]  # Ball starts in the center
    ball_speed = [2, 2]  # Ball speed in x and y directions
    ball_radius = 20  # Radius of the ball
    screen_width, screen_height = 800, 600  # Screen dimensions
    clock = pygame.time.Clock()  # Create a clock to manage frame rate

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the program

        # Update ball position
        ball_pos[0] += ball_speed[0]  # Move ball horizontally
        ball_pos[1] += ball_speed[1]  # Move ball vertically

        # Bounce off edges
        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > screen_width:
            ball_speed[0] = -ball_speed[0]  # Reverse horizontal speed

        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > screen_height:
            ball_speed[1] = -ball_speed[1]  # Reverse vertical speed

        # Draw everything
        screen.fill((255, 255, 255))  # White background
        pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)  # Draw the red ball
        pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
