from display import *
from draw import *
from parser import *
from matrix import *
import copy
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = []
ident_mat = new_matrix()
ident(ident_mat)
transform.append(ident_mat)

parse_file( 'myscript', edges, polygons, transform, screen, color )
