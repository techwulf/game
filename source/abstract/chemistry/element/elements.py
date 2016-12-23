from source.abstract.chemistry.element.element import Element

# more values can be found at
# http://periodictable.com/index.html

"""
Molar Mass (g/mol) is rounded to two decimal points for three reasons.
1. This is > 0.1% precision - plenty for checking the molar mass of compounds.
2. Molar masses are only non-integers because they are the weighted average of the isotopes present on Earth.
The sources of meteorites are determined by noting that their isotope composition is different than Earth's. So these
values are probably not all that accurate for Mars.
3. In many cases, 2 decimal places is all that anyone has bothered to measure.
"""

# 1
class Hydrogen(Element):
    name    = "Hydrogen"
    symbol  = "H"
    mass    = 1.01

    def __init__(self):
        Element.__init__(self)
        pass


# 2
class Helium(Element):
    name    = "Helium"
    symbol  = "He"
    mass    = 4.00

    def __init__(self):
        Element.__init__(self)
        pass


# 3
class Lithium(Element):
    name    = "Lithium"
    symbol  = "Li"
    mass    = 6.94

    def __init__(self):
        Element.__init__(self)
        pass


# 4
class Beryllium(Element):
    name    = "Beryllium"
    symbol  = "Be"
    mass    = 9.01

    def __init__(self):
        Element.__init__(self)
        pass


# 5
class Boron(Element):
    name    = "Boron"
    symbol  = "B"
    mass    = 10.81

    def __init__(self):
        Element.__init__(self)
        pass


# 6
class Carbon(Element):
    name    = "Carbon"
    symbol  = "C"
    mass    = 12.01

    def __init__(self):
        Element.__init__(self)
        pass


# 7
class Nitrogen(Element):
    name    = "Nitrogen"
    symbol  = "N"
    mass    = 14.01

    def __init__(self):
        Element.__init__(self)
        pass


# 8
class Oxygen(Element):
    name    = "Oxygen"
    symbol  = "O"
    mass    = 16.00

    def __init__(self):
        Element.__init__(self)
        pass


# 9
class Fluorine(Element):
    name    = "Fluorine"
    symbol  = "F"
    mass    = 19.00

    def __init__(self):
        Element.__init__(self)
        pass


# 10
class Neon(Element):
    name    = "Neon"
    symbol  = "Ne"
    mass    = 20.18

    def __init__(self):
        Element.__init__(self)
        pass


# 11
class Sodium(Element):
    name    = "Sodium"
    symbol  = "Na"
    mass    = 22.99

    def __init__(self):
        Element.__init__(self)
        pass


# 12
class Magnesium(Element):
    name    = "Magnesium"
    symbol  = "Mg"
    mass    = 24.31

    def __init__(self):
        Element.__init__(self)
        pass


# 13
class Aluminum(Element):
    name    = "Aluminum"
    symbol  = "Al"
    mass    = 26.98

    def __init__(self):
        Element.__init__(self)
        pass


# 14
class Silicon(Element):
    name    = "Silicon"
    symbol  = "Si"
    mass    = 28.09

    def __init__(self):
        Element.__init__(self)
        pass


# 15
class Phosphorus(Element):
    name    = "Phosphorus"
    symbol  = "P"
    mass    = 30.97

    def __init__(self):
        Element.__init__(self)
        pass


# 16
class Sulfur(Element):
    name    = "Sulfur"
    symbol  = "S"
    mass    = 32.07

    def __init__(self):
        Element.__init__(self)
        pass


# 17
class Chlorine(Element):
    name    = "Chlorine"
    symbol  = "Cl"
    mass    = 35.45

    def __init__(self):
        Element.__init__(self)
        pass


# 18
class Argon(Element):
    name    = "Argon"
    symbol  = "Ar"
    mass    = 39.95

    def __init__(self):
        Element.__init__(self)
        pass


# 19
class Potassium(Element):
    name    = "Potassium"
    symbol  = "K"
    mass    = 39.10

    def __init__(self):
        Element.__init__(self)
        pass


# 20
class Calcium(Element):
    name    = "Calcium"
    symbol  = "Ca"
    mass    = 40.08

    def __init__(self):
        Element.__init__(self)
        pass


# 21
class Scandium(Element):
    name    = "Scandium"
    symbol  = "Sc"
    mass    = 44.96

    def __init__(self):
        Element.__init__(self)
        pass


# 22
class Titanium(Element):
    name    = "Titanium"
    symbol  = "Ti"
    mass    = 47.87

    def __init__(self):
        Element.__init__(self)
        pass


# 23
class Vanadium(Element):
    name    = "Vanadium"
    symbol  = "V"
    mass    = 50.94

    def __init__(self):
        Element.__init__(self)
        pass


# 24
class Chromium(Element):
    name    = "Chromium"
    symbol  = "Cr"
    mass    = 52.00

    def __init__(self):
        Element.__init__(self)
        pass


# 25
class Manganese(Element):
    name    = "Manganese"
    symbol  = "Mn"
    mass    = 54.94

    def __init__(self):
        Element.__init__(self)
        pass


# 26
class Iron(Element):
    name    = "Iron"
    symbol  = "Fe"
    mass    = 55.85

    def __init__(self):
        Element.__init__(self)
        pass


# 27
class Cobalt(Element):
    name    = "Cobalt"
    symbol  = "Co"
    mass    = 58.93

    def __init__(self):
        Element.__init__(self)
        pass


# 28
class Nickel(Element):
    name    = "Nickel"
    symbol  = "Ni"
    mass    = 58.69

    def __init__(self):
        Element.__init__(self)
        pass


# 29
class Copper(Element):
    name    = "Copper"
    symbol  = "Cu"
    mass    = 63.55

    def __init__(self):
        Element.__init__(self)
        pass


# 30
class Zinc(Element):
    name    = "Zinc"
    symbol  = "Zn"
    mass    = 65.41

    def __init__(self):
        Element.__init__(self)
        pass


# 31
class Gallium(Element):
    name    = "Gallium"
    symbol  = "Ga"
    mass    = 69.72

    def __init__(self):
        Element.__init__(self)
        pass


# 32
class Germanium(Element):
    name    = "Germanium"
    symbol  = "Ge"
    mass    = 72.64

    def __init__(self):
        Element.__init__(self)
        pass


# 33
class Arsenic(Element):
    name    = "Arsenic"
    symbol  = "As"
    mass    = 74.92

    def __init__(self):
        Element.__init__(self)
        pass


# 34
class Selenium(Element):
    name    = "Selenium"
    symbol  = "Se"
    mass    = 78.96

    def __init__(self):
        Element.__init__(self)
        pass


# 35
class Bromine(Element):
    name    = "Bromine"
    symbol  = "Br"
    mass    = 79.90

    def __init__(self):
        Element.__init__(self)
        pass


# 36
class Krypton(Element):
    name    = "Krypton"
    symbol  = "Kr"
    mass    = 83.80

    def __init__(self):
        Element.__init__(self)
        pass


# 37
class Rubidium(Element):
    name    = "Rubidium"
    symbol  = "Rb"
    mass    = 85.47

    def __init__(self):
        Element.__init__(self)
        pass


# 38
class Strontium(Element):
    name    = "Strontium"
    symbol  = "Sr"
    mass    = 87.62

    def __init__(self):
        Element.__init__(self)
        pass


# 39
class Yttrium(Element):
    name    = "Yttrium"
    symbol  = "Y"
    mass    = 88.91

    def __init__(self):
        Element.__init__(self)
        pass


# 40
class Zirconium(Element):
    name    = "Zirconium"
    symbol  = "Zr"
    mass    = 91.22

    def __init__(self):
        Element.__init__(self)
        pass


#41
class Niobium(Element):
    name    = "Niobium"
    symbol  = "Nb"
    mass    = 92.91

    def __init__(self):
        Element.__init__(self)
        pass


#42
class Molybdenum(Element):
    name    = "Molybdenum"
    symbol  = "Mo"
    mass    = 95.94

    def __init__(self):
        Element.__init__(self)
        pass


#43
class Technetium(Element):
    name    = "Technetium"
    symbol  = "Tc"
    mass    = 98   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 44
class Ruthenium(Element):
    name    = "Ruthenium"
    symbol  = "Ru"
    mass    = 101.07

    def __init__(self):
        Element.__init__(self)
        pass


# 45
class Rhodium(Element):
    name    = "Rhodium"
    symbol  = "Rh"
    mass    = 102.91

    def __init__(self):
        Element.__init__(self)
        pass


# 46
class Palladium(Element):
    name    = "Palladium"
    symbol  = "Pd"
    mass    = 106.42

    def __init__(self):
        Element.__init__(self)
        pass


# 47
class Silver(Element):
    name    = "Silver"
    symbol  = "Ag"
    mass    = 107.87

    def __init__(self):
        Element.__init__(self)
        pass


# 48
class Cadmium(Element):
    name    = "Cadmium"
    symbol  = "Cd"
    mass    = 112.41

    def __init__(self):
        Element.__init__(self)
        pass


# 49
class Indium(Element):
    name    = "Indium"
    symbol  = "In"
    mass    = 114.82

    def __init__(self):
        Element.__init__(self)
        pass


# 50
class Tin(Element):
    name    = "Tin"
    symbol  = "Sn"
    mass    = 118.71

    def __init__(self):
        Element.__init__(self)
        pass


# 51
class Antimony(Element):
    name    = "Antimony"
    symbol  = "Sb"
    mass    = 121.76

    def __init__(self):
        Element.__init__(self)
        pass


# 52
class Tellurium(Element):
    name    = "Tellurium"
    symbol  = "Te"
    mass    = 127.6   # Only 1 decimal place was given.

    def __init__(self):
        Element.__init__(self)
        pass


# 53
class Iodine(Element):
    name    = "Iodine"
    symbol  = "I"
    mass    = 126.90

    def __init__(self):
        Element.__init__(self)
        pass


# 54
class Xenon(Element):
    name    = "Xenon"
    symbol  = "Xe"
    mass    = 131.29

    def __init__(self):
        Element.__init__(self)
        pass


# 55
class Cesium(Element):
    name    = "Cesium"
    symbol  = "Cs"
    mass    = 132.91

    def __init__(self):
        Element.__init__(self)
        pass


# 56
class Barium(Element):
    name    = "Barium"
    symbol  = "Ba"
    mass    = 137.33

    def __init__(self):
        Element.__init__(self)
        pass


# 57
class Lanthanum(Element):
    name    = "Lanthanum"
    symbol  = "La"
    mass    = 138.91

    def __init__(self):
        Element.__init__(self)
        pass


# 58
class Cerium(Element):
    name    = "Cerium"
    symbol  = "Ce"
    mass    = 140.12

    def __init__(self):
        Element.__init__(self)
        pass


# 59
class Praseodymium(Element):
    name    = "Praseodymium"
    symbol  = "Pr"
    mass    = 140.91

    def __init__(self):
        Element.__init__(self)
        pass


# 60
class Neodymium(Element):
    name    = "Neodymium"
    symbol  = "Nd"
    mass    = 144.24

    def __init__(self):
        Element.__init__(self)
        pass


# 61
class Promethium(Element):
    name    = "Promethium"
    symbol  = "Pm"
    mass    = 145   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 62
class Samarium(Element):
    name    = "Samarium"
    symbol  = "Sm"
    mass    = 150.36

    def __init__(self):
        Element.__init__(self)
        pass


# 63
class Europium(Element):
    name    = "Europium"
    symbol  = "Eu"
    mass    = 151.96

    def __init__(self):
        Element.__init__(self)
        pass


# 64
class Gadolinium(Element):
    name    = "Gadolinium"
    symbol  = "Gd"
    mass    = 157.25

    def __init__(self):
        Element.__init__(self)
        pass


# 65
class Terbium(Element):
    name    = "Terbium"
    symbol  = "Tb"
    mass    = 158.93

    def __init__(self):
        Element.__init__(self)
        pass


# 66
class Dysprosium(Element):
    name    = "Dysprosium"
    symbol  = "Dy"
    mass    = 162.5   # Only 1 decimal place was given.

    def __init__(self):
        Element.__init__(self)
        pass


# 67
class Holmium(Element):
    name    = "Holmium"
    symbol  = "Ho"
    mass    = 164.93

    def __init__(self):
        Element.__init__(self)
        pass


# 68
class Erbium(Element):
    name    = "Erbium"
    symbol  = "Er"
    mass    = 167.26

    def __init__(self):
        Element.__init__(self)
        pass


# 69
class Thulium(Element):
    name    = "Thulium"
    symbol  = "Tm"
    mass    = 168.93

    def __init__(self):
        Element.__init__(self)
        pass


# 70
class Ytterbium(Element):
    name    = "Ytterbium"
    symbol  = "Yb"
    mass    = 173.04

    def __init__(self):
        Element.__init__(self)
        pass


# 71
class Lutetium(Element):
    name    = "Lutetium"
    symbol  = "Lu"
    mass    = 174.97

    def __init__(self):
        Element.__init__(self)
        pass


# 72
class Hafnium(Element):
    name    = "Hafnium"
    symbol  = "Hf"
    mass    = 178.49

    def __init__(self):
        Element.__init__(self)
        pass


# 73
class Tantalum(Element):
    name    = "Tantalum"
    symbol  = "Ta"
    mass    = 180.95

    def __init__(self):
        Element.__init__(self)
        pass


# 74
class Tungsten(Element):
    name    = "Tungsten"
    symbol  = "W"
    mass    = 183.84

    def __init__(self):
        Element.__init__(self)
        pass


# 75
class Rhenium(Element):
    name    = "Rhenium"
    symbol  = "Re"
    mass    = 186.21

    def __init__(self):
        Element.__init__(self)
        pass


# 76
class Osmium(Element):
    name    = "Osmium"
    symbol  = "Os"
    mass    = 190.23

    def __init__(self):
        Element.__init__(self)
        pass


# 77
class Iridium(Element):
    name    = "Iridium"
    symbol  = "Ir"
    mass    = 192.22

    def __init__(self):
        Element.__init__(self)
        pass


# 78
class Platinum(Element):
    name    = "Platinum"
    symbol  = "Pt"
    mass    = 195.08

    def __init__(self):
        Element.__init__(self)
        pass


# 79
class Gold(Element):
    name    = "Gold"
    symbol  = "Au"
    mass    = 196.97

    def __init__(self):
        Element.__init__(self)
        pass


# 80
class Mercury(Element):
    name    = "Mercury"
    symbol  = "Hg"
    mass    = 200.59

    def __init__(self):
        Element.__init__(self)
        pass


# 81
class Thallium(Element):
    name    = "Thallium"
    symbol  = "Tl"
    mass    = 204.38

    def __init__(self):
        Element.__init__(self)
        pass


# 82
class Lead(Element):
    name    = "Lead"
    symbol  = "Pb"
    mass    = 207.2   # Only 1 decimal place was given.

    def __init__(self):
        Element.__init__(self)
        pass


# 83
class Bismuth(Element):
    name    = "Bismuth"
    symbol  = "Bi"
    mass    = 208.98

    def __init__(self):
        Element.__init__(self)
        pass


# 84
class Polonium(Element):
    name    = "Polonium"
    symbol  = "Po"
    mass    = 209   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 85
class Astatine(Element):
    name    = "Astatine"
    symbol  = "At"
    mass    = 210   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 86
class Radon(Element):
    name    = "Radon"
    symbol  = "Rn"
    mass    = 222   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 87
class Francium(Element):
    name    = "Francium"
    symbol  = "Fr"
    mass    = 223   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 88
class Radium(Element):
    name    = "Radium"
    symbol  = "Ra"
    mass    = 226   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 89
class Actinium(Element):
    name    = "Actinium"
    symbol  = "Ac"
    mass    = 227   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 90
class Thorium(Element):
    name    = "Thorium"
    symbol  = "Th"
    mass    = 232.04

    def __init__(self):
        Element.__init__(self)
        pass


# 91
class Protactinium(Element):
    name    = "Protactinium"
    symbol  = "Pa"
    mass    = 231.04

    def __init__(self):
        Element.__init__(self)
        pass


# 92 - This is the last naturally occuring element. The rest are man-made.
class Uranium(Element):
    name    = "Uranium"
    symbol  = "U"
    mass    = 238.03

    def __init__(self):
        Element.__init__(self)
        pass


# 93
class Neptunium(Element):
    name    = "Neptunium"
    symbol  = "Np"
    mass    = 237   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 94
class Plutonium(Element):
    name    = "Plutonium"
    symbol  = "Pu"
    mass    = 244   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass


# 95 - This is included because it's common in smoke detectors
class Americium(Element):
    name    = "Americium"
    symbol  = "Am"
    mass    = 243   # Radioactive. Mass is for the longest lived isotope.

    def __init__(self):
        Element.__init__(self)
        pass

