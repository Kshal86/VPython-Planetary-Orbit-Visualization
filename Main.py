import pygame
import sys
from pygame.locals import *
import subprocess

# Initialize Pygame
pygame.init()

BLACK=  (0, 0, 0)

# Set up the screen
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Start Screen") # Set the window title

# Load the background image
background_img = pygame.image.load("Images/background.png").convert()

# Set up colors
WHITE = (255, 255, 255)

# Create the font
title_font = pygame.font.Font("Fonts/Lato-Regular.ttf", 72)
button_font = pygame.font.Font("Fonts/Lato-Regular.ttf", 22)
name_font = pygame.font.Font("Fonts/Lato-Regular.ttf", 24)

# Define button dimensions
button_width = 200
button_height = 50
button_margin = 20
button_radius = 10

# Create the buttons
start_button = pygame.Rect((width - button_width) // 2, height // 2, button_width, button_height)
quit_button = pygame.Rect((width - button_width) // 2, height // 2 + button_height + button_margin, button_width, button_height)

# Main start screen loop
def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                     subprocess.run(["python3", "Processes.py"]) 
                     sys.exit()
                     pygame.quit()
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Draw the background image
        screen.blit(background_img, (0, 0))

        # Render and display the title text
        title_text = title_font.render("Space Visualizer", True, WHITE)
        title_rect = title_text.get_rect()
        title_rect.center = (width // 2, height // 3)
        screen.blit(title_text, title_rect)

        # Render and display the "by Kushal Parajapati" text
        author_text = name_font.render("By: Kushal Prajapati", True, WHITE)
        author_rect = author_text.get_rect()
        author_rect.center = (width // 2, title_rect.bottom + 20)
        screen.blit(author_text, author_rect)

        # Draw the buttons with curved edges
        pygame.draw.rect(screen, WHITE, start_button, border_radius=button_radius)
        pygame.draw.rect(screen, WHITE, quit_button, border_radius=button_radius)

        # Render and display the button text
        start_text = button_font.render("Start", True, BLACK)
        start_text_rect = start_text.get_rect()
        start_text_rect.center = start_button.center
        screen.blit(start_text, start_text_rect)

        quit_text = button_font.render("Quit", True, BLACK)
        quit_text_rect = quit_text.get_rect()
        quit_text_rect.center = quit_button.center
        screen.blit(quit_text, quit_text_rect)

        # Update the display
        pygame.display.update()


if __name__ == '__main__':
    start_screen()
