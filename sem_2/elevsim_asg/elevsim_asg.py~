'''

TASK

Your task is to implement the simple elevator in Python using classes. The
default strategy is the simple "start at the bottom, go to the top, then go to
the bottom". You don't have to use this, you can take an alternative approach
such as random start location for the elevator.


PROJECT DESCRIPTION / SPECIFICATION:

    1. Create three classes: Building, Elevator, and Customer.
    2. Equip the building with an elevator. Ask user to customize the number
       of floors and the number of customers.
    3. Program should have error checking to make sure the user inputs are
       valid. For example, if a user gives non-integer inputs, notify the use
       that the inputs are incorrect and prompt again.
    3. Each customer starts from a random floor, and has a random destination
       floor.
    4. Each customer will use the elevator only once, i.e., when a customer
       moves out of the elevator, he/she will never use it again.
    5. When all customers have reached their destination floor, the simulation
       is finished.
    7. Part of the grade on this assignment will be the appropriateness of
       your classes, methods, and any functions you use. The quality of the
       code will now matter as well as the performance.
    8. All classes’ methods require a docstring for a general description of
       the method.
    9. Don’t use any global variables.

'''


class Building:

    def __init__(self, floors, customers, floor_ls=[], floors_ls=[]):

        self.floors = floors
        self.customers = customers
        self.floor_ls = floor_ls
        self.floors_ls = floors_ls
        for i in range(10):
            floor_ls.append('*')
        for i in range(10):
            floor_ls.append('_')
        for i in range(self.floors):
            self.floors_ls.append(self.floor_ls)

    def __str__(self):

        floor_rep = ''
        for i in (self.floors_ls):
            for j in (self.floor_ls):
                floor_rep += j
            floor_rep += '\n'

        return floor_rep

    def __repr__(self):
        pass


class Elevator:
    pass


class Customer:
    pass


def main():

    floors = int(input('Please input the number of floors in the building: '))
    customers = int(input('Please input the number of customers: '))

    build = Building(floors, customers)
    print(build)

if __name__ == '__main__':
    main()
