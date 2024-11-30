class Shapes:
    shapes = ''
    def __init__(self):
        Shapes.shapes=input("Enter shape [sqr, rec, tri,cir] : ")

    def add(*args):
        answer = 1
        if Shapes.shapes == "cir":
            if len(args) == 1:
                answer = 3.14 * (args[0] * args[0])
        else:
            if len(args) == 1:
                answer = args[0] * args[0]
            else:
                for i in args:
                    answer *= i
        return answer


obj = Shapes()

# Square
if Shapes.shapes == "sqr":
    side = int(input("Side of Square: "))
    print( "Area of Square = " + str(Shapes.add(side)))

# Rectangle
if Shapes.shapes == "rec":
    leng = int(input("Length of Rectangle: "))
    brdt = int(input("Breadth of Rectangle: "))
    print( "Area of Rectangle = " + str(Shapes.add(leng,brdt)))

# Triangle
if Shapes.shapes == "tri":
    leng = int(input("Length of Triangle: "))
    brdt = int(input("Breadth of Triangle: "))
    hght = int(input("Height of Triangle: "))
    print( "Area of Triangle = " + str(Shapes.add(leng,brdt,hght)))

# Circle
if Shapes.shapes == "cir":
    radius = int(input("Radius of Circle: "))
    print( "Area of Circle = " + str(Shapes.add(radius)))