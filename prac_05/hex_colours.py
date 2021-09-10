"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_TO_HEX_CODE = {"AliceBlue    ": "#f0f8ff", "AntiqueWhite ": "#faebd7", "AntiqueWhite1": "#ffefdb",
                      "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                      "aquamarine1  ": "#7fffd4", "aquamarine2  ": "#76eec6", "aquamarine4  ": "#458b74"}

# for colour in COLOUR_TO_HEX_CODE:
#     print(f"{colour} is {COLOUR_TO_HEX_CODE[colour]}")

colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    if colour_name in COLOUR_TO_HEX_CODE:
        print(colour_name, "is", COLOUR_TO_HEX_CODE[colour_name])
    else:
        print("Invalid colour name")
    state_code = input("Enter colour name: ").upper()
