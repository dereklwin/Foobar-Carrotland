import fractions

def countLatticeOnLine(a,b):
    return fractions.gcd(abs(a),abs(b))

def answer(vertices):
    pointAx = vertices[0][0]
    pointAy = vertices[0][1]
    pointBx = vertices[1][0]
    pointBy = vertices[1][1]
    pointCx = vertices[2][0]
    pointCy = vertices[2][1]

    # Calculate all outer lattice points by getting the gcd of the difference between two points and adding 1
    totalOuterLattice = 0
    totalOuterLattice += countLatticeOnLine(pointAx-pointBx, pointAy-pointBy)
    totalOuterLattice += countLatticeOnLine(pointCx-pointBx, pointCy-pointBy)
    totalOuterLattice += countLatticeOnLine(pointAx-pointCx, pointAy-pointCy)
    # The equation to get lattice points between two points also includes the verticies 
    # which results in 3 extra lattice points that need to be subtracted. we remove the 
    # extra subtract by not adding each time we count total lattice points on each line

    # Use coordinates of verticies to get area of the triangle
    area = (pointAx*(pointBy-pointCy)+pointBx*(pointCy-pointAy)+pointCx*(pointAy-pointBy))/2.0

    # Use Pick's theorem to get the count of all lattice points inside the triangle
    return math.fabs(area)-totalOuterLattice/2.0+1

# print answer([[2, 3], [6, 9], [10, 160]])
# print answer([[91207, 89566], [-88690, -83026], [67100, 47194]])
# print answer([[0,0],[1,1],[-1,2]])
# print answer([[1,0],[-3,1],[12,-1]])