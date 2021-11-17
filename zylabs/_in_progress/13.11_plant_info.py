# FIXME UNFINISHED
class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)
        print('   Annual:', self.is_annual)
        print('   Color of flowers:', self.color_of_flowers)

    def print_list(self):
        plant = []
        plant.append(Plant)
        for i in plant:
            print(i)

# TODO:  Define the print_list() function that prints a list of plant (or flower) objects

if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input()

    while user_string != '-1':
        user_plant = Plant
        user_split = user_string.split()
        user_plant.plant_name = user_split[1]
        user_plant.plant_cost = user_split[2]
        if user_split[0] == 'flower':
            user_plant.is_annual = user_split[3]
            user_plant.color_of_flowers = user_split[4]

        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        user_string = input()

    # TODO: Call the print_list() function to print my_garden