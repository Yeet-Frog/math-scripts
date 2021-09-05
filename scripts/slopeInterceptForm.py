slope = input("Slope: ")
x = input("X: ")
y = input("Y: ")
slope = float(slope)
x = float(x)
y = float(y)

def yIntercept(slope, xCoord):
    xCoord = -(xCoord)
    return (slope * xCoord) + y

print('\033[4m',"y = ",slope,"x + ",yIntercept(slope, x))
