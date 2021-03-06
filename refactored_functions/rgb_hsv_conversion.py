# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

"""
The RGB color model is an additive color model in which red, green, and blue light
are added together in various ways to reproduce a broad array of colors. The name
of the model comes from the initials of the three additive primary colors, red,
green, and blue. Meanwhile, the HSV representation models how colors appear under
light. In it, colors are represented using three components: hue, saturation and
(brightness-)value. This file provides functions for converting colors from one
representation to the other.

(description adapted from https://en.wikipedia.org/wiki/RGB_color_model and
https://en.wikipedia.org/wiki/HSL_and_HSV).
"""


def hsv_to_rgb(hue: float, saturation: float, value: float) -> list:
    """
    Conversion from the HSV-representation to the RGB-representation.
    Expected RGB-values taken from
    https://www.rapidtables.com/convert/color/hsv-to-rgb.html

    >>> hsv_to_rgb(0, 0, 0)
    [0, 0, 0]
    >>> hsv_to_rgb(0, 0, 1)
    [255, 255, 255]
    >>> hsv_to_rgb(0, 1, 1)
    [255, 0, 0]
    >>> hsv_to_rgb(60, 1, 1)
    [255, 255, 0]
    >>> hsv_to_rgb(120, 1, 1)
    [0, 255, 0]
    >>> hsv_to_rgb(240, 1, 1)
    [0, 0, 255]
    >>> hsv_to_rgb(300, 1, 1)
    [255, 0, 255]
    >>> hsv_to_rgb(180, 0.5, 0.5)
    [64, 128, 128]
    >>> hsv_to_rgb(234, 0.14, 0.88)
    [193, 196, 224]
    >>> hsv_to_rgb(330, 0.75, 0.5)
    [128, 32, 80]
    """
    if hue < 0 or hue > 360:
        raise Exception("hue should be between 0 and 360")

    if saturation < 0 or saturation > 1:
        raise Exception("saturation should be between 0 and 1")

    if value < 0 or value > 1:
        raise Exception("value should be between 0 and 1")

    chroma = value * saturation
    hue_section = hue / 60
    second_largest_component = chroma * (1 - abs(hue_section % 2 - 1))
    match_value = value - chroma

    # Colour types.
    
    # --------------------------------------------------------------------
    # REFACTORED: Here the three main calculations are made instead of being part a larger 
    # if-statement. The values have also been placed into an indexable list which can 
    # be accessed by the hue_section.
    # --------------------------------------------------------------------
    ct1 = round(255 * (chroma + match_value))
    ct2 = round(255 * (second_largest_component + match_value))
    ct3 = round(255 * (match_value))
    
    # Colour type combos.
    comb_one = [ct1, ct2, ct3]
    comb_two = [ct2, ct1, ct3]
    comb_three = [ct3, ct1, ct2]
    comb_four = [ct3, ct2, ct1]
    comb_five = [ct2, ct3, ct1]
    comb_six = [ct1, ct3, ct2]
    hue_section_list = [comb_one, comb_one, comb_two, comb_three, comb_four, comb_five]

    if hue_section <= 5:
        return hue_section_list[round(hue_section)]
    # --------------------------------------------------------------------

    return comb_six


def rgb_to_hsv(red: int, green: int, blue: int) -> list:
    """
    Conversion from the RGB-representation to the HSV-representation.
    The tested values are the reverse values from the hsv_to_rgb-doctests.
    Function "approximately_equal_hsv" is needed because of small deviations due to
    rounding for the RGB-values.

    >>> approximately_equal_hsv(rgb_to_hsv(0, 0, 0), [0, 0, 0])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 255, 255), [0, 0, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 0, 0), [0, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 255, 0), [60, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(0, 255, 0), [120, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(0, 0, 255), [240, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 0, 255), [300, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(64, 128, 128), [180, 0.5, 0.5])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(193, 196, 224), [234, 0.14, 0.88])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(128, 32, 80), [330, 0.75, 0.5])
    True
    """
    if red < 0 or red > 255:
        raise Exception("red should be between 0 and 255")

    if green < 0 or green > 255:
        raise Exception("green should be between 0 and 255")

    if blue < 0 or blue > 255:
        raise Exception("blue should be between 0 and 255")

    float_red = red / 255
    float_green = green / 255
    float_blue = blue / 255
    value = max(max(float_red, float_green), float_blue)
    chroma = value - min(min(float_red, float_green), float_blue)
    saturation = 0 if value == 0 else chroma / value

    if chroma == 0:
        hue = 0.0
    elif value == float_red:
        hue = 60 * (0 + (float_green - float_blue) / chroma)
    elif value == float_green:
        hue = 60 * (2 + (float_blue - float_red) / chroma)
    else:
        hue = 60 * (4 + (float_red - float_green) / chroma)

    hue = (hue + 360) % 360

    return [hue, saturation, value]


def approximately_equal_hsv(hsv_1: list, hsv_2: list) -> bool:
    """
    Utility-function to check that two hsv-colors are approximately equal

    >>> approximately_equal_hsv([0, 0, 0], [0, 0, 0])
    True
    >>> approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.500001, 0.30001])
    True
    >>> approximately_equal_hsv([0, 0, 0], [1, 0, 0])
    False
    >>> approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.6, 0.30001])
    False
    """
    check_hue = abs(hsv_1[0] - hsv_2[0]) < 0.2
    check_saturation = abs(hsv_1[1] - hsv_2[1]) < 0.002
    check_value = abs(hsv_1[2] - hsv_2[2]) < 0.002

    return check_hue and check_saturation and check_value
