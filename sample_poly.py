#Created by mmnair
class Shapes:
    shape = ""
    def __int__(self):
        Shapes.shape = input('enter the shapes[sqr,rec,tri]:'"")

    def add(*args):
        answer = 1
        if len(args) == 1:
            for i in args:
                answer = i * i
        else:
            for i in args:
                answer *= i
        return answer

obj = Shapes()
'''
if Shapes.shape == 'sqr':
    side = int(input("side of square:"))
    print("area of square=" + str(Shapes.add(side)))
if Shapes.shape == 'tri':
    leng = int(input('length of triangle'))
    brdth = int(input('breadth of triangle'))
    hght = int(input('height of triangle'))
    print("area of rectangle=" + str(Shapes.add(leng, brdth, hght)))
if Shapes.shape == 'rec':
    leng = int(input('length of recangle'))
    brdth = int(input('breadth of rectangle'))
    print("area of rectangle=" + str(Shapes.add(leng, brdth)))
'''