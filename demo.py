#! /usr/bin/python2.7

import pygame
from source.game import game

if __name__ == "__main__":
    game = game.Game()
    game.on_loop()
