#This file is meant to draw a star on the screen.
# it will take in a starting degree, a number of points, and a size.
# it will then draw a star on the screen.

#remember that the cartesian coordinate system on pygame 
#is upside down compared to the traditional cartesian coordinate system

import pygame
import math
import argparse
import sys
import numpy as np
import typing as type

def draw_star(screen: pygame.Surface,                                   #The screen to draw on
            starting_degree: float=90,                                     #The starting degree, default is 90(top of the star)
            num_points: int=5,                                            #The number of points, default is 5
            size: int=100                                                    #The size of the star, default is 100
            ) -> None:
    #create a list of points greater than or equal to 5
    if num_points < 5:
        print("Number of points must be greater than or equal to 5")
        return
    points = []
    #get center of the screen
    center = screen.get_rect().center
    #calculate the step size( 360 divided by the number of points)
    step = math.pi / num_points
    #calculate the starting radians(math programming typically uses radians)
    start_rad = math.radians(starting_degree)
    #calculate the points
    for i in range(num_points):
        #calculate the angle
        angle = start_rad + i * step
        #calculate the x and y coordinates around the screen center
        x = center[0] + size * math.cos(angle)
        y = center[1] + -(size * math.sin(angle))  #the minus is because the y axis is inverted
        #add the point to the list
        points.append((x, y))
    #draw the star
    pygame.draw.polygon(screen, (255, 255, 255), points)
#main function for the program
def main():
    parser = argparse.ArgumentParser(description="Draw a star using Pygame.")
    parser.add_argument(
        "--starting_degree", type=float, default=90,
        help="Starting degree for the first point (default: 90, top of the circle)"
    )
    parser.add_argument(
        "--num_points", type=int, default=5,
        help="Number of points in the star (minimum 5)"
    )
    parser.add_argument(
        "--size", type=int, default=100,
        help="Size (radius) of the star"
    )
    parser.add_argument(
        "--width", type=int, default=600,
        help="Screen width (default 600)"
    )
    parser.add_argument(
        "--height", type=int, default=600,
        help="Screen height (default 600)"
    )
    args = parser.parse_args()

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((args.width, args.height))
    pygame.display.set_caption("Star Drawer")
    screen.fill((0, 0, 0))  # Black background

    #draw the star
    draw_star(
        screen=screen,
        starting_degree=args.starting_degree,
        num_points=args.num_points,
        size=args.size
    )

    print("Star drawn. Close the window to exit.")

    # Keep window open until user closes it
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

