#! /usr/bin/python2.7

from source.abstract.chemistry.minerals import bauxite
from source.abstract.chemistry.minerals import ice
#from source.entities.electronic.elemental_storage_unit import elemental_storage_unit
#from source.entities.electronic.refinery import refinery
#from source.entities.electronic.replicator import replicator
from source.systems.logistics import logistics

if __name__ == "__main__":
    logistics  = logistics.Logistics()
    #esu        = elemental_storage_unit.ElementalStorageUnit()
    #refinery   = refinery.Refinery(esu) #Create a refinery and attach the ElementalStorageUnit to it.
    #replicator = replicator.Replicator(esu) #Create a Replicator and attach the ElementalStorageUnit to it.

    #Create some minerals
    ice = ice.Ice()
    bauxite = bauxite.Bauxite()

    #Print out the composition of the Minerals
    ice.pretty_print()
    bauxite.pretty_print()

    #Put Minerals in the Refinery
    logistics.refinery.refine_mineral(ice)
    logistics.refinery.refine_mineral(bauxite)
    
    #Print out the status of the ElementalStorageUnit
    logistics.elemental_storage_unit.pretty_print()

    #Replicate a Widget
    widget0 = logistics.replicator.build_widget()
    widget0.pretty_print()

    #Print out the status of the ElementalStorageUnit To see if Elements have been Removed
    logistics.elemental_storage_unit.pretty_print()

    #Replicate Another Widget
    widget1 = logistics.replicator.build_widget()
    widget1.pretty_print()

    #This Widget should fail
    widget2 = logistics.replicator.build_widget()

    #Print out the status of the ElementalStorageUnit To see if Elements have been Removed
    logistics.elemental_storage_unit.pretty_print()
