# Question: Use Python to calculate the distance in kilometers between Jupiter and Sun 
# on January 1, 1230. 
# Hint 1: Use the ephem  Python third party library.
# Hint 2: Note that the units of ephem  are in Astronomical Units (AU). 
# You need to convert them to kilometers.

# Expected output: 
# 758085657.5026425

# Answer:
import ephem

date = '1230/1/1'
jupiter = ephem.Jupiter()
jupiter.compute(date)

distance_AU = jupiter.sun_distance
distance_km = distance_AU * 149597870.691
print(f"distance in kilometers between Jupiter and Sun on January 1, 1230: {distance_km}")


# Explanation:
# This solution required some internet research to find out about the ephem  library which is used for astronomy computations. The library can be installed with pip install ephem, but if that doesn't work on Windows then download a precompiled version from here and install it again with pip like pip install ephem‑3.7.6.0‑cp36‑cp36m‑win_amd64.whl 
# In the ephem webpage you can find an example to start off. The above solution was developed based on that example. 
