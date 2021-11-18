from gl import Raytracer, V3
from obj import *
from figures import *

# Dimensio pix
width = 1024
height = 512

# Materiales
grass = Material(diffuse = (0,0.9,0), spec = 64)
Pink = Material(diffuse = (1,0.75,0.79), spec = 64)
piedra = Material(diffuse = (0.5,0.5,0.5), spec = 64)
agua = Material(diffuse = (0.2, 0.2 , 0.7), spec = 128, matType = REFLECTIVE)
sol = Material(spec = 64, ior = 1.1, matType = TRANSPARENT)

#texturas
arbol = Material(texture = Texture('wood.bmp'))
leaves = Material(texture = Texture('Leaves.bmp'))
workbench = Material(texture = Texture('workbench.bmp'))


# ENVMAP Sky
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('sky.bmp')

#Luces
rtx.ambLight = AmbientLight(strength = 0.08)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.3)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 0.2))


# #cerdito
rtx.scene.append(Sphere(V3(-1.5,-2,-6), 0.6, Pink) )
rtx.scene.append(AABB(V3(0,-2,-6), V3(2,1,1),Pink))#torso
rtx.scene.append(AABB(V3(0.4,-2.5,-5.5), V3(0.4,0.7,0.5),Pink))#pierna
rtx.scene.append(AABB(V3(-0.4,-2.5,-5.5), V3(0.4,0.7,0.5),Pink))#pierna
rtx.scene.append(AABB(V3(-2,-2,-6), V3(0.3,0.3,0.4),Pink))#nariz

# Sol
rtx.scene.append(Sphere(V3(-15,4.5,-24), 3, sol) )


# #Plataforma
rtx.scene.append(AABB(V3(7,-3.5,-8), V3(16,1.8,7),grass))

# #agua
rtx.scene.append(AABB(V3(-7,-3.5,-8), V3(13,1,7),agua))

# Pared
rtx.scene.append(AABB(V3(6,-4,-11), V3(15,7,1),piedra))
rtx.scene.append(AABB(V3(-7,-4,-11), V3(13,3,1),piedra))

# #arbol
rtx.scene.append(AABB(V3(0,-2,-10), V3(1,1,1),arbol))
rtx.scene.append(AABB(V3(0,-1,-10), V3(1,1,1),arbol))

# #leaves
rtx.scene.append(AABB(V3(0,0,-9), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(1,0,-10), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(-1,0,-10), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(0,1,-10), V3(1,1,1),leaves))

# #arbol2
rtx.scene.append(AABB(V3(5,-2,-7), V3(1,1,1),arbol))
rtx.scene.append(AABB(V3(5,-1,-7), V3(1,1,1),arbol))


#leaves
rtx.scene.append(AABB(V3(5,0,-6), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(6,0,-7), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(4,0,-7), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(5,1,-7), V3(1,1,1),leaves))

#arbol3
rtx.scene.append(AABB(V3(2,-2,-8), V3(1,1,1),arbol))

#leaves
rtx.scene.append(AABB(V3(2,-1,-7), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(3,-1,-8), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(1,-1,-8), V3(1,1,1),leaves))
rtx.scene.append(AABB(V3(2,0,-8), V3(1,1,1),leaves))

#workbench
rtx.scene.append(AABB(V3(4,-2,-6), V3(1,1,1),workbench))

# Outbmp
rtx.glRender()
rtx.glFinish('Out.bmp')



