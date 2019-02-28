class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.engine_status = True
        print("You can turn the key and the car turns on")

    def move_forward(self):
        self.fuel -= 1
        print("The car moves forward")

    def turn_left(self):
        self.fuel -= 1
        print("The car turns left")

    def turn_off(self):
        self.engine_status = False
        print("You turn the car off.")

    def reverse(self):
        self.fuel -= 1
        print("The car moves backward")

    def turn_right(self):
        self.fuel -= 1
        print("The car turns right")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)


class KeylessCar(Car):
    def __init__(self, name, milage):
        super(KeylessCar, self).__init__(name, milage)

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the car turns on.")
        

wiebe_car = KeylessCar("Tesla", 125)
jacob_car = Impala()
jacob_car.start_engine()
jacob_car.move_forward()
jacob_car.turn_left()
jacob_car.move_forward()
jacob_car.turn_off()


def cake():
    print("""Reluctantly crouched at the starting line
Engines pumping and thumping in time
The green light flashes, the flags go up
Churning and burning, they yearn for the cup
They deftly maneuver and muscle for rank
Fuel burning fast on an empty tank
Reckless and wild, they pour through the turns
Their prowess is potent and secretly stern
As they speed through the finish, the flags go down
The fans get up and they get out of town
The arena is empty except for one man
Still driving and striving as fast as he can
The sun has gone down and the moon has come up
And long ago somebody left with the cup
But he's driving and striving and hugging the turns
And thinking of someone for whom he still burns
He's going the distance
He's going for speed
She's all alone (all alone)
All alone in her time of need
Because he's racing and pacing and plotting the course
He's fighting and biting and riding on his horse
He's going the distance
No trophy, no flowers, no flashbulbs, no wine
He's haunted by something he cannot define
Bowel-shaking earthquakes of doubt and remorse
Assail him, impale him with monster-truck force
In his mind, he's still driving, still making the grade
She's hoping in time that her memories will fade
'Cause he's racing and pacing and plotting the course
He's fighting and biting and riding on his horse
The sun has gone down and the moon has come up
And long ago somebody left with the cup
But he's striving and driving and hugging the turns
And thinking of someone for whom he still burns
'Cause he's going the distance
He's going for speed
She's all alone (all alone)
All alone in her time of need
Because he's racing and pacing and plotting the course
He's fighting and biting and riding on his horse
He's racing and pacing and plotting the course
He's fighting and biting and riding on his horse
He's going the distance
He's going for speed
He's going the distance
Ah no, so sad, alright 
Oh no, oh no, no, no""")


cake()
