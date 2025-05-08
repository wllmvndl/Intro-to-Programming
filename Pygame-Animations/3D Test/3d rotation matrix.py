def three_dim_rotator(point, rotation):
    # This function takes in a point in 3D space
    # as well as a rotation about Alpha, Beta, and Gamma (Roll, Pitch, and Yaw)
    # and returns a new point with the rotation applied
    
    x = point[0]
    y = point[1]
    z = point[2]

    alpha = rotation[0]
    beta = rotation[1]
    gamma = rotation[2]

    sinA = math.sin(alpha)
    cosA = math.cos(aplha)
    sinB = math.sin(beta)
    cosB = math.cos(beta)
    sinG = math.sin(gamma)
    cosG = math.cos(gamma)

    # 3D rotation matrix
    # [ cos(B)cos(G)  sin(A)sin(B)cos(G) - cos(A)sin(G)  cos(A)sin(B)cos(G) + sin(A)sin(G) ] [x]
    # [ cos(B)sin(G)  sin(A)sin(B)sin(G) + cos(A)cos(G)  cos(A)sin(B)sin(G) - sin(A)cos(G) ] [y]
    # [ -sin(B)       sin(A)cos(B)                       cos(A)cos(B)                      ] [z]

    new_x = x * (cosB * cosG)  +  y * (sinA * sinB * cosG - cosA * sinG)  +  z * (cosA * sinB * cosG + sinA * sinG)
    new_y = x * (cosB * sinG)  +  y * (sinA * sinB * sinG + cosA * cosG)  +  z * (cosA * sinB * sinG - sinA * cosG)
    new_z = x * (-sinB)        +  y * (sinA * cosB)                       +  z * (cosA * cosB)

    new_point = [new_x, new_y, new_z]
    return new_point

