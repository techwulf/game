#! /usr/bin/python

from source.minerals import bauxite, ice

if __name__ == "__main__":
    b = bauxite.Bauxite()
    i = ice.Ice()

    b.pretty_print()
    i.pretty_print()
