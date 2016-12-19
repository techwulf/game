from source.abstract.element import element

class Hydrogen(element.Element):
    name            = "Hydrogen"
    symbol          = "H"
    atomic_number   = 1
    group           = 1
    period          = 1
    atomic_weight   = 1.008
    density         = 0.0899
    molar_volume    = 0.01121

    abundance       = {
        "universe"     : 0.75,
        "sun"          : 0.75,
        "meteorite"    : 0.024,
        "crust"        : 0.0015,
        "ocean"        : 0.11,
        "human"        : 0.10
    }

    def __init__(self):
        element.Element.__init__(self)
        pass

"""
Overview
Name    Hydrogen
Symbol  H
Atomic Number   1
Atomic Weight   1.00794
Density 0.0899 g/l[note]
Melting Point   -259.14 C
Boiling Point   -252.87 C

Thermal properties
Phase   Gas
Melting Point   -259.14 C
Boiling Point   -252.87 C
Absolute Melting Point  14.01 K
Absolute Boiling Point  20.28 K
Critical Pressure   1.293 MPa (12.76 Atm)
Critical Temperature    32.97 K
Heat of Fusion  0.558 kJ/mol
Heat of Vaporization    0.452 kJ/mol
Heat of Combustion  N/A
Specific Heat   14300 J/(kg K)[note]
Adiabatic Index 7/5
Neel Point  N/A
Thermal Conductivity    0.1805 W/(m K)
Thermal Expansion   N/A

Bulk physical properties
Density 0.0899 g/l[note]
Density (Liquid)    N/A
Molar Volume    0.01121
Brinell Hardness    N/A
Mohs Hardness   N/A
Vickers Hardness    N/A
Bulk Modulus    N/A
Shear Modulus   N/A
Young Modulus   N/A
Poisson Ratio   N/A
Refractive Index    1.000132
Speed of Sound  1270 m/s
Thermal Conductivity    0.1805 W/(m K)
Thermal Expansion   N/A

Reactivity
Valence 1
Electronegativity   2.2
ElectronAffinity    72.8 kJ/mol
Ionization Energies 
1312 kJ/mol

Health and Safety
Autoignition Point  535.5 C
Flashpoint  -18 C
Heat of Combustion  N/A
DOT Hazard Class    2.1
DOT Numbers 1966
EU Number   N/A
NFPA Fire Rating    4
NFPA Hazards    N/A
NFPA Health Rating  3
NFPA Reactivity Rating  0
RTECS Number    RTECSMW8900000
NFPA Label  NFPA Label
    

Classifications
Alternate Names None
Names of Allotropes Dihydrogen
Block   s
Group   1
Period  1
Electron Configuration  1s1
Color   Colorless
Discovery   
1766 in United Kingdom
Gas phase   Diatomic
CAS Number  CAS1333-74-0
CID Number  CID783
Gmelin Number   N/A
NSC Number  N/A
RTECS Number    RTECSMW8900000

Electrical properties
Electrical Type N/A
Electrical Conductivity N/A
Resistivity N/A
Superconducting Point   N/A

Magnetic properties
Magnetic Type   Diamagnetic
Curie Point N/A
Mass Magnetic Susceptibility    -2.48x10-8
Molar Magnetic Susceptibility   -4.999x10-11
Volume Magnetic Susceptibility  -2.23x10-9

Abundances
% in Universe   75%
% in Sun    75%
% in Meteorites 2.4%
% in Earth's Crust  0.15%
% in Oceans 11%
% in Humans 10%

Atomic dimensions and structure
Atomic Radius   53 pm
Covalent Radius 37 pm
Van der Waals Radius    120 pm
Crystal Structure   Simple Hexagonal
Lattice Angles  
/2, /2, 2 /3
Lattice Constants   
470, 470, 340 pm
Space Group Name    P63/mmc
Space Group Number  194

Nuclear Properties
Half-Life   Stable
Lifetime    Stable
Decay Mode  N/A
Quantum Numbers 2S1/2
Neutron Cross Section   0.332
Neutron Mass Absorption 0.011
Known Isotopes  
1H, 2H, 3H, 4H, 5H, 6H, 7H
Stable Isotopes 
1H, 2H
Isotopic Abundances 
1H  99.9885%
2H  0.0115%


Notes on the properties of Hydrogen:

Density: Density given for H at 0 Celsius. 2

Specific Heat: Value given for gas phase of H . 2
"""
