import math

def project(point):
    FOCUS_POINT = [640, 360, -1280]
    
    t = - FOCUS_POINT[2] / (point[2] - FOCUS_POINT[2])

    x = FOCUS_POINT[0] + t * (point[0] - FOCUS_POINT[0])
    y = FOCUS_POINT[1] + t * (point[1] - FOCUS_POINT[1])

    projected_point = [x, y] 
    return projected_point


def find_surface_normal(point1, point2, point3):

    x1, y1, z1 = point1[0], point1[1], point1[2]
    x2, y2, z2 = point2[0], point2[1], point2[2]
    x3, y3, z3 = point3[0], point3[1], point3[2]

    # Find the surface Normal of the points
    # Define 2 vectors based off the 3 given points
    vector1 = [ [x2 - x1], [y2 - y1], [z2 - z1] ]
    vector1 = [ [x3 - x1], [y3 - y1], [z3 - z1] ]

    # Find the cross product
    product_x = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
    product_y = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
    product_z = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    unnormalized = [ product_x, product_y, product_z]
    magnitude = math.sqrt( product_x**2 + product_y**2 + product_z**2)

    if magnitude > 0:
        surface_normal = [ product_x / magnitude, product_y / magnitude, product_z / magnitude ]
        print(surface_normal)
    else:
        print("Cannot find surface normal on points that are co-linear.")
        surface_normal = [0,0,0]
    
    return surface_normal


triangle = [ [400, 300, 100], [430, 480, 260], [0, 400, 100] ]
print(triangle)
find_surface_normal(triangle[0], triangle[1], triangle[2])
