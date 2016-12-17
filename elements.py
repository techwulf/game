#! /usr/bin/python

from source.minerals import bauxite, ice

def print_info(mineral):
    print(mineral.name)

    for chemical in mineral.chemicals:
        print("  "+chemical.name)

        for element in chemical.elements:
            print("    "+element.name)
    print(" ")

if __name__ == "__main__":
    b = bauxite.Bauxite()
    i = ice.Ice()

    print_info(b)
    print_info(i)
