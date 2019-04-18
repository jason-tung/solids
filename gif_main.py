from display import *
from draw import *
from nooby import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'gifbase', edges, polygons, csystems, screen, zbuffer, color )


