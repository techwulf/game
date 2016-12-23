#! /usr/bin/python2.7

from source.abstract.chemistry.minerals import bauxite
from source.abstract.chemistry.minerals import ice
from source.entities.elemental_storage_unit import elemental_storage_unit
from source.entities.refinery import refinery
from source.entities.replicator import replicator

if __name__ == "__main__":
    esu        = elemental_storage_unit.ElementalStorageUnit()
    refinery   = refinery.Refinery(esu) #Create a refinery and attach the ElementalStorageUnit to it.
    replicator = replicator.Replicator(esu) #Create a Replicator and attach the ElementalStorageUnit to it.

    #Create some minerals
    ice = ice.Ice()
    bauxite = bauxite.Bauxite()

    #Print out the composition of the Minerals
    ice.pretty_print()
    bauxite.pretty_print()

    #Put Minerals in the Refinery
    refinery.refine_mineral(ice)
    refinery.refine_mineral(bauxite)
    
    #Print out the status of the ElementalStorageUnit
    esu.pretty_print()

    #Replicate a Widget
    widget0 = replicator.build_widget()
    widget0.pretty_print()

    #Print out the status of the ElementalStorageUnit To see if Elements have been Removed
    esu.pretty_print()

    #Replicate Another Widget
    widget1 = replicator.build_widget()
    widget1.pretty_print()

    #This Widget should fail
    widget2 = replicator.build_widget()

    #Print out the status of the ElementalStorageUnit To see if Elements have been Removed
    esu.pretty_print()
