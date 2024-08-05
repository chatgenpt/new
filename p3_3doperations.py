import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define cube vertices, edges, and colors
vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
]

surfaces = [
    (0, 1, 2, 3), (3, 2, 6, 7), (7, 6, 5, 4),
    (4, 5, 1, 0), (1, 5, 6, 2), (4, 0, 3, 7)
]

colors = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (1, 1, 0), (1, 0, 1), (0, 1, 1)
]

def draw_cube():
    """Draw the cube with colored faces."""
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    # Initialize Pygame and set up OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1, 1, 1, 1)  # Set background color to white
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Set perspective
    glTranslatef(0.0, 0.0, -5)  # Move the camera back

    clock = pygame.time.Clock()

    translate, rotate, scale = [0, 0, 0], [0, 0, 0], 1  # Initial transformations

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        # Handle translation
        if keys[K_LEFT]: translate[0] -= 0.05
        if keys[K_RIGHT]: translate[0] += 0.05
        if keys[K_UP]: translate[1] += 0.05
        if keys[K_DOWN]: translate[1] -= 0.05
        # Handle rotation
        if keys[K_x]: rotate[0] += 3
        if keys[K_y]: rotate[1] += 3
        if keys[K_z]: rotate[2] += 3
        # Handle scaling
        if keys[K_w]: scale += 0.05
        if keys[K_s]: scale = max(scale - 0.05, 0.05)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen
        glPushMatrix()
        glTranslatef(*translate)  # Apply translation
        glScalef(scale, scale, scale)  # Apply scaling
        glRotatef(rotate[0], 1, 0, 0)  # Rotate around x-axis
        glRotatef(rotate[1], 0, 1, 0)  # Rotate around y-axis
        glRotatef(rotate[2], 0, 0, 1)  # Rotate around z-axis
        draw_cube()  # Draw the cube
        glPopMatrix()
        pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    main()
