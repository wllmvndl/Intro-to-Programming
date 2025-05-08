import math

def find_real_value():
    pass

def parameterize(square_point, focus_point):
    #f(t) = focus_point + t(square_real)   
    t = - focus_point[2] / (square_point[2] - focus_point[2])

    x = focus_point[0] + t * (square_point[0] - focus_point[0])
    y = focus_point[1] + t * (square_point[1] - focus_point[1])
    z = focus_point[2] + t * (square_point[2] - focus_point[2])

    projected_point = [x, y, z] 
    return projected_point

def draw_square(x, y, z, side, theta):
    # 4 points for a square defined by its center and side length

    # s is equal to the given side length over 2
    s = side/2
    real_quadrant1 = [x + s * math.cos(theta), y + side/2, z - s * math.sin(theta)]
    real_quadrant2 = [x - s * math.cos(theta), y + side/2, z + s * math.sin(theta)]
    real_quadrant3 = [x - s * math.cos(theta), y - side/2, z + s * math.sin(theta)]
    real_quadrant4 = [x + s * math.cos(theta), y - side/2, z - s * math.sin(theta)]
    
    real_square = [real_quadrant1, real_quadrant2, real_quadrant3, real_quadrant4]

    # Defines the field of View, Farther Away = Narrower
    focus_point = [640, 360, -1280]

    # Finds the Parameterized "Equation" for a line in 3D Space
    projected_quadrant1 = parameterize(real_quadrant1, focus_point)
    projected_quadrant2 = parameterize(real_quadrant2, focus_point)
    projected_quadrant3 = parameterize(real_quadrant3, focus_point)
    projected_quadrant4 = parameterize(real_quadrant4, focus_point)

    projected_square = [projected_quadrant1, projected_quadrant2, projected_quadrant3, projected_quadrant4]

    print(real_square)
    print(projected_square)

draw_square(1000, 300, 1000, 300, math.pi/4)
draw_square(100, -200, 200, 100, 0)
