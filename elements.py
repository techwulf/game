#! /usr/bin/python

from source.minerals import bauxite

if __name__ == "__main__":
    b = bauxite.Bauxite()
    print(b.name)

    for chemical in b.chemicals:
        print(chemical.name)

        for element in chemical.elements:
            print(element.name)
