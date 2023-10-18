import math
def distance(x1,y1,x2,y2):
    lat = pow((x2-x1),2) + pow((y2-y1),2)
    dist =math.sqrt(lat)
    return (dist)


X1 = 17.735020
X2 = 8.213120   
Y1 = 83.287376
Y2 = 83.213120
print(distance(X1,Y1,X2,Y2))
