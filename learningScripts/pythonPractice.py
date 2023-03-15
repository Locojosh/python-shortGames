#def main():
print('YOOOOOO...')

def greet():
    name = input('Your name here:')
    lastName = 'Starllink'
    age = input('Your age please:')
    print('Greetings', name, ' {last}, with age of {}!'.format(age))
    print('Greetings')

#greet()

def show_me_variables():
    num = 3
    print(num)
    print(type(num))
    stri = "somethings"
    print(stri)

#show_me_variables()

def show_operators():
    print(2.1**3)

#show_operators()

def loop_it():
    myList = {1,2,3,4}
    for m in myList:
        print("number: ", m)
    
    for i in range(4):
        print("i is: ", i)
    
    families = [[1,2,3], [22,33], [444,555,888,999]]
    for family in families:
        for member in family:
            print('member of family ', families.index(family)+1 , ' is: ',member)

#loop_it()

def handle_errors():
    #nums = [1,3,5,8]
    nums = ['d', 'e', 'k']
    try:
        avg = sum(nums) / len(nums)
        print("the average is: ", avg)
    except:
        print("Cannot compute average - make sure you enter a list of integers!")
    finally:
        print("jfkdllkdfj")

#handle_errors()

class Obstacle:
    #print("hey you!")
    def __init__(self, height):
        self.height = height

    def __del__(self):
        print("Successfully deleted the obstacle")
    
    def printInfo(self):
        print("New obstacle created. Height:", self.height)

class WaterObstacle(Obstacle):
    def __init__(self, height, wetness):
        self.wetness = wetness
        Obstacle.__init__(self, height)

obsPalestra = Obstacle(7.5)
obsPalestra.printInfo()

obsWaterSlide = WaterObstacle(2.1, "medium")
obsWaterSlide.printInfo()

#print(obsPalestra._height)

#print(obsPalestra)
print("////////")

class TrashCan:
    def printInfo(self):
        print("TrashCan created!")

greenTrashCan = TrashCan()
tallObstacle = Obstacle(9999.3)

for aaa in (greenTrashCan, tallObstacle):
    aaa.printInfo()