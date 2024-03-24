from colorsys import hls_to_rgb

hue = 120/360
saturation = 80/100
luminosity = 60/100


clr = hls_to_rgb(hue,luminosity,saturation)
print(clr)
