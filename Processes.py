

# Imports
from vpython import * # Imports vpython library
import subprocess

# Canvas scene (width, height, background color, range)
star_light = local_light(pos=vector(0,0,0), color=color.white, visible = True)
scene.width = 1280
scene.height = 720
scene.background = color.black

# Orbital Periods (Days to complete one orbit):
exoplanetperiod = 170
mercuryperiod = 88
venusperiod = 224.7
earthperiod = 365.2
marsperiod = 687
jupiterperiod = 4332.6
saturnperiod = 10759.2

# Radius of Planets (m) (Scaled down by 1e6):
starrad = 696.34e6
mercuryrad = 2.44e6
venusrad = 6.05e6
earthrad = 6.38e6
marsrad = 3.4e6
jupiterrad = 7.14e7
saturnrad = 6.03e7

# Position of Planet (m) (Scaled down by 1e6):
mercurypos = vector((5.79e9+starrad), 0, 0)
venuspos = vector((1.082e10+starrad), 0, 0)
earthpos = vector((1.496e10+starrad), 0, 0)
marspos = vector((2.279e10+starrad), 0, 0)
jupiterpos = vector((7.785e11+starrad), 0, 0)
saturnpos = vector((1.433e12+starrad), 0, 0)

# CHZ(Circumstellar Habitable Zone):
chz_inner = ((0.75*mag(earthpos)) + starrad)
chz_outer = ((1.7*mag(earthpos)) + starrad)
chz_thickness = (0.009*mag(earthpos))


# Time
t = 0
deltat = 0.1


##  Objects

star=sphere(color=color.orange,pos=vec(0,0,0),radius=starrad, emissive=True, texture = "http://i.imgur.com/yoEzbtg.jpg")
mercury=sphere(color=color.gray(0.75),pos=mercurypos,radius=mercuryrad, shininess=10, make_trail=True, opacity = 0.5)
venus=sphere(color=color.gray(0.75),pos=venuspos,radius=venusrad, shininess=10, make_trail=True, opacity = 0.5)
earth=sphere(color=color.gray(0.75),pos=earthpos,radius=earthrad, shininess=10, make_trail=True, opacity = 0.5)
mars=sphere(color=color.gray(0.75),pos=marspos,radius=marsrad, shininess=10, make_trail=True, opacity = 0.5)
ring1 = ring(pos= vec(0,0,0), axis = vec(0,1,0), radius = chz_inner, thickness = chz_thickness, color = color.green, opacity = 0.75)
ring2 = ring(pos= vec(0,0,0), axis = vec(0,1,0), radius = chz_outer, thickness = chz_thickness, color = color.red, opacity = 0.75)
jupiter=sphere(color=color.gray(0.75),pos=jupiterpos,radius= jupiterrad, shininess=10, make_trail=True, opacity = 0.5)
saturn=sphere(color=color.gray(0.75),pos=saturnpos,radius= saturnrad, shininess=10, make_trail=True, opacity = 0.5)


 ##  Labels
star_label = label(pos=star.pos,
    text='Star', xoffset=10,
    line = False, yoffset=10, height=12, 
    border=3, font='sans')

mercury_label = label(pos=mercury.pos,
    text='Mercury', xoffset=10,
    line = False, yoffset=10, height=12, 
    border=3, font='sans')

venus_label = label(pos=venus.pos,
    text='Venus', xoffset=10,
    line = False, yoffset=10, height=12, 
    border=3, font='sans')

earth_label = label(pos=earth.pos,
    text='Earth', xoffset=10,
    line = False, yoffset=10, height=12, 
    border=3, font='sans')

ring_label = label(pos=(ring1.pos+vector(0, 0, ring1.radius)),
    text='CHZ Inner', xoffset=2,
    line = False, yoffset=10, height=12, 
    border=3, font='sans')

ring_label2 = label(pos=(ring2.pos+vector(0, 0, ring2.radius)),
    text='CHZ Outer', xoffset=2,
    line = False, yoffset=10, height=12, 
    border=3, font='sans')

mars_label = label(pos=mars.pos,
    text='Mars', xoffset=10,
    line = False, yoffset=10, height=12,
    border=3, font='sans')

jupiter_label = label(pos=jupiter.pos,
    text='Jupiter', xoffset=10,
    line = False, yoffset=10, height=12,
    border=3, font='sans')

saturn_label = label(pos=saturn.pos,
    text='Saturn', xoffset=10,
    line = False, yoffset=10, height=12,
    border=3, font='sans')



sleep(1)
while True:
  rate(100)
  t = t + deltat
  star.rotate(angle=(2*3.14159/365), axis=vector(0,1,0), origin=vector(0,0,0))
  mercury.rotate(angle=(2*3.14159/mercuryperiod), axis=vector(0,1,0), origin=vector(0,0,0))
  venus.rotate(angle=(2*3.14159/venusperiod), axis=vector(0,1,0), origin=vector(0,0,0))
  earth.rotate(angle=(2*3.14159/earthperiod), axis=vector(0,1,0), origin=vector(0,0,0))
  mars.rotate(angle=(2*3.14159/marsperiod), axis=vector(0,1,0), origin=vector(0,0,0))
  jupiter.rotate(angle=(2*3.14159/jupiterperiod), axis=vector(0,1,0), origin=vector(0,0,0))
  saturn.rotate(angle=(2*3.14159/saturnperiod), axis=vector(0,1,0), origin=vector(0,0,0))

 
