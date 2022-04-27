from controllers.game_move import GameMove
from .exit import Exit
from .key import Key
from .play import Play
from .wall import Wall

import pygame
import pygame.locals
import datetime

def create_text_surface(text):
    arial = pygame.font.SysFont('arial', 24)
    text_surface = arial.render(text, True, (0, 0, 0))

    return text_surface

class MazeView:
    """
    Creates a view of the maze in pygame
    """

    def __init__(self, maze, name):
        """
        Creates an instance of the maze view

        :param maze: An attribute of the maze class that is the nested lists for the maze
        :type maze: nested lists
        """
        self.maze = maze
        self._name = name
        start_time = datetime.datetime.now()
        self.start_time = (60 * start_time.minute) + start_time.second
        self.timer = 0

    def display_maze(self):
        """
        Starts pygame display, activates movement, and displays maze
        """
        pygame.init()
        clock = pygame.time.Clock()
        running = True

        while running:
            player = Play()
            key = Key()
            exit = Exit()
            wall = Wall()
            #-- A loop that updates the maze with new information after moving and loops movement

            clock.tick(60)

            window = pygame.display.set_mode(((len(self.maze.content[0])*50), (len(self.maze.content*50) + 50)))
            window.set_colorkey((255, 255, 255))
            window.fill((211, 211, 211))

            for idx, value in enumerate(self.maze.content):
            # =============================================================
            # loops through the outer list of the nested lists for the maze

            # :param valueinenumerate: an inner list
            # :type valueinenumerate: list
            # =============================================================
                for jdx, jvalue in enumerate(value):
                # ============================================================
                # loops through the inner list of the nested lists for the maze

                # :param valueinenumerate: an inner list
                # :type valueinenumerate: list
                # :param jvalueinenumerate: One of the folowing strings "key, X,  , E"
                # :type jvalueinenumerate: string
                # =============================================================
                    if jvalue == "X":
                    #-- Checks if a spot is an X and creates a black square to represent a wall for it in pygame
                        window.blit(wall.image, ((jdx * 50), (idx * 50)))
                
                    if jvalue == "P":
                    #-- Checks if a spot is the player or P and creates a blue square to represent it in pygame

                        window.blit(player.image, ((jdx * 50), (idx * 50)))
                
                    if jvalue == "E":
                    #-- Checks if a spot is the exit or E and creates a green square to represent it in pygame
        
                        window.blit(exit.image, ((jdx * 50), (idx * 50)))
                
                    if jvalue == "key":
                    #-- Checks if a spot is a key and creates a red square to represent it in pygame
                        window.blit(key.image, ((jdx * 50), (idx * 50)))

            #-- Creates a timer and backpack in pygame
            self.timer = 100 - (pygame.time.get_ticks() // 600)
            show_fps = create_text_surface(str(self.timer))
            timer = create_text_surface("Timer:")
            backpack = create_text_surface("Backpack:")
            window.blit(timer, (5, (len(self.maze.content*50) + 13)))
            window.blit(show_fps, (62, (len(self.maze.content*50) + 13)))

            window.blit(backpack, (100, (len(self.maze.content*50) + 13)))

            #-- Adds keys to appear in the backpack depending on how many keys are collected in pygame
            if len(self.maze.player.backpack) == 1:
                window.blit(key.image, ((190, (len(self.maze.content*50) + 8))))

            if len(self.maze.player.backpack) == 2:
                window.blit(key.image, ((190, (len(self.maze.content*50) + 8))))
                window.blit(key.image, ((220, (len(self.maze.content*50) + 8))))

            if len(self.maze.player.backpack) == 3:
                window.blit(key.image, ((190, (len(self.maze.content*50) + 8))))
                window.blit(key.image, ((220, (len(self.maze.content*50) + 8))))
                window.blit(key.image, ((250, (len(self.maze.content*50) + 8))))

            if len(self.maze.player.backpack) == 4:
                window.blit(key.image, ((190, (len(self.maze.content*50) + 8))))
                window.blit(key.image, ((220, (len(self.maze.content*50) + 8))))
                window.blit(key.image, ((250, (len(self.maze.content*50) + 8))))
                window.blit(key.image, ((280, (len(self.maze.content*50) + 8))))

            pygame.display.update()

            moving = GameMove(self.maze, self._name, self.timer)
            moving.move()

    def display(self, content):
        """
        A simple way to display the layout of the maze in a terminal
        """
        for i in content:
            print(i)