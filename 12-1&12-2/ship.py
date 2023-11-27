import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # 12-2 Game Character
        """
        Find a bitmap image of a game character you like or
convert an image to a bitmap Make a class that draws the character at the
center of the screen and match the background color of the image to the back-
ground color of the screen, or vice versa
"""
        # Load the ship image, and get its rect.
        # For original image is too big to be used in limited screen applications of the game
        # Here I resize the image, so it would be smaller and suitable to be still used as a ship controller
        self.image = pygame.image.load('Minecraft.bmp').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300,200))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
