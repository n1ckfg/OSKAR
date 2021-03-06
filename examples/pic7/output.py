"""

Python Generated by the OSKAR Compiler v2.3 at
2017-06-11 16:38:32.6212351 Eastern Daylight Time

Compiler written by Bryce Summers
Please see https://github.com/Bryce-Summers/OSKAR

"""

from pythonGenerator import *

# Global Variables

scene = Scene()

p = scene.newFunction("myTY1")
p.addArgument("x")
p.addArgument("time")
p.addExpression("cos((x*360)+(time*360))")
p.scalar_type()

# 1 functions parsed.

# Picture definition for floor
scene.newPicture("floor")
scene.iterations("i", "0", "1")
scene.scaling("2", "2", ".02")
scene.translation("-.5", "-.5", "-.05")
scene.basis("cube")

# Picture definition for funplot
scene.newPicture("funplot")
scene.addArgument("TYfunction")
scene.iterations("i", "0", "20")
scene.scaling(".125", ".04", ".01")
scene.scaling(".5", "4", "5")
scene.translation("i", "TYfunction ( i , Global_t )", ".05")
scene.scaling("1", ".5", "1")
scene.translation("0", ".5", "0")
scene.basis("cube")

# Picture via reduction for cosine
scene.newDirectPicture("cosine")
scene.expression("funplot(myTY1)")

# Picture definition for funplot
scene.newPicture("funplot")
scene.addArgument("TYfunction")
scene.addArgument("numpix")
scene.iterations("i", "0", "numpix")
scene.scaling(".125", ".04", ".01")
scene.scaling(".5", "4", "5")
scene.translation("i", "TYfunction ( i , Global_t )", ".05")
scene.scaling("1", ".5", "1")
scene.translation("0", ".5", "0")
scene.basis("cube")

# Picture via reduction for cosine
scene.newDirectPicture("cosine")
scene.expression("funplot(myTY1,100)")

# Picture definition for MakeArray
scene.newPicture("MakeArray")
scene.addArgument("base=cube")
scene.addArgument("rows=4")
scene.addArgument("cols=2")
scene.addArgument("numpix=rows*cols")
scene.iterations("i", "0", "numpix")
scene.scaling("1 / cols", "1 / rows", "1")
scene.translation("modulo ( i * steps , cols ) / cols", "step ( i * steps , cols ) / cols / cols", "0")
scene.basis("base")

# Picture via reduction for wallpaper
scene.newDirectPicture("wallpaper")
scene.expression("MakeArray(cosine,4,4,16)")


# Top level picture definition.
scene.newDrawCommand("draw")
scene.iterations("i", "0", "400")
scene.basis("wallpaper")
scene.basis("floor")


# Generate Code in a Render Language
scene.generateCode()
