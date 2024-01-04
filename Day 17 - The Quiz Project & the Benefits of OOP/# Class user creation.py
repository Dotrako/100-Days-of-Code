# Class user creation

class User():
    def __init__(self, id, username):    
        self.id_test = id
        self.username = username


# user1 = User("001", "Amine")
# print(user1.username)
# print(user1.id_test)

class Car():
    def __init__(self, seats):
        self.seats = seats

class SportsCar():
    def __init__(self,seats):
        self.seats = 2

model1 = Car(4)
print(model1.seats)

model2 = SportsCar(2)
print(model2.seats)