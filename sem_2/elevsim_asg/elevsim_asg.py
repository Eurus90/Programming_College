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

import random


class Building:

    def __init__(self, floors, customers, customers_ls=[], floor_ls=[], floors_ls=[]):

        self.floors = floors
        self.customers = customers
        self.customers_ls = customers_ls
        self.floor_ls = floor_ls
        self.floors_ls = floors_ls

    def run(self):

        Elev = Elevator(self.floors)
        cnt = 0
        customer_cnt = 0
        self.customers_ls = []
        customer_obj_ls = []
        flr_sz = 0
        flr_sz_cnt = {}
        cus_on_des_flr = []

        for i in range(self.customers):

            x = str('C' + str(i))
            self.customers_ls.append(x)

        for i in range(self.customers):

            i = Customer(i, self.floors)
            customer_obj_ls.append(i)

        for i in customer_obj_ls:

            if i.des_floor in flr_sz_cnt:
                flr_sz_cnt[i.des_floor] += 1
            else:
                flr_sz_cnt[i.des_floor] = 1
            if i.current_floor in flr_sz_cnt:
                flr_sz_cnt[i.current_floor] += 1
            else:
                flr_sz_cnt[i.current_floor] = 1

        for i in flr_sz_cnt:

            if flr_sz < flr_sz_cnt[i]:
                flr_sz = flr_sz_cnt[i]

        while len(cus_on_des_flr) < (self.customers):

            cnt += 1
            self.floors_ls = []

            if cnt <= 1:

                for i in range(self.floors):

                    if i == Elev.current_floor:
                        self.floor_ls = ['[E] ']*(flr_sz*2) + ['___ ']*(flr_sz*2)
                    else:
                        self.floor_ls = ['[ ] ']*(flr_sz*2) + ['___ ']*(flr_sz*2)

                    for j in customer_obj_ls:

                        if j.current_floor == i:

                            self.floor_ls.remove('___ ')
                            self.floor_ls.insert((flr_sz*2), j.name)

                    self.floors_ls.append(self.floor_ls)

            else:

                for i in range(self.floors):

                    if i == Elev.current_floor:
                        self.floor_ls = ['[E] ']*(flr_sz*2) + ['___ ']*(flr_sz*2)
                    else:
                        self.floor_ls = ['[ ] ']*(flr_sz*2) + ['___ ']*(flr_sz*2)

                    for j in customer_obj_ls:

                        if (j.current_floor == i) and (i != Elev.current_floor) and (j.on_elev == 0):

                            try:

                                self.floor_ls.remove('___ ')
                                self.floor_ls.insert((flr_sz*2), j.name)

                            except ValueError:

                                self.floor_ls.append(j.name)

                        elif (j.current_floor == i) and (i == Elev.current_floor) and (j.on_elev == 0) and (j.des_floor == i):

                            try:

                                self.floor_ls.remove('___ ')
                                self.floor_ls.insert((flr_sz*2), j.name)

                            except ValueError:

                                self.floor_ls.append(j.name)

                        elif (j.current_floor == i) and (j.des_floor != i) and (i == Elev.current_floor):

                            try:

                                j.on_elev = 1
                                j.move_cus()

                                self.floor_ls.remove('[E] ')
                                self.floor_ls.insert(0, j.name)

                            except ValueError:

                                try:

                                    self.floor_ls.remove('___ ')
                                    self.floor_ls.insert((flr_sz*2), j.name)

                                except ValueError:

                                    self.floor_ls.append(j.name)

                        elif (j.current_floor == i) and (j.des_floor == i) and (i == Elev.current_floor) and (j.on_elev == 1):

                            try:

                                j.on_des_floor = 1
                                cus_on_des_flr.append(1)
                                j.on_elev = 0
                                self.floor_ls.remove('___ ')
                                self.floor_ls.insert((flr_sz*2), j.name)

                            except ValueError:

                                self.floor_ls.append(j.name)

                    self.floors_ls.append(self.floor_ls)

                Elev.move()

            print(self)

    def __str__(self):

        floor_rep = '\n\n'
        for i in (self.floors_ls):
            for j in i:
                floor_rep += j
            floor_rep += '\n\n'

        return floor_rep

    def __repr__(self):
        pass


class Elevator:

    def __init__(self, floors, current_floor=0, up=1):

        self.current_floor = current_floor
        self.floors = floors
        self.up = up

    def move(self):

        if self.current_floor == (self.floors - 1):
            self.up = 0
        elif self.current_floor == 0:
            self.up = 1

        if self.up == 1:
            self.current_floor += 1
        if self.up == 0:
            self.current_floor -= 1


class Customer:

    def __init__(self, i, floors, name='', current_floor=0, des_floor=0, on_elev=0, on_des_floor=0, up=1):

        self.i = i
        self.name = name
        self.floors = floors
        self.current_floor = random.randint(0, (floors - 1))
        self.des_floor = random.randint(0, (floors - 1))
        self.on_elev = on_elev
        self.on_des_floor = on_des_floor
        self.up = up

        while self.current_floor == self.des_floor:
            self.des_floor = random.randint(0, (floors - 1))

        if self.i < 10:
            self.name = str('c' + '0' + str(i) + ' ')
        else:
            self.name = str('c' + str(i) + ' ')

    def move_cus(self):

        if self.current_floor == (self.floors - 1):
            self.up = 0
        elif self.current_floor == 0:
            self.up = 1

        if self.up == 1:
            self.current_floor += 1
        if self.up == 0:
            self.current_floor -= 1

    def __str__(self):

        return self.name


def main():

    floors = int(input('Please input the number of floors in the building: '))
    customers = int(input('Please input the number of customers: '))

    build = Building(floors, customers)
    build.run()

if __name__ == '__main__':
    main()
