from typing import Any


class Insect:
    number_of_insects = 0

    @staticmethod
    def get_number_of_insects():
        return Insect.number_of_insects

    def __init__(self, name="mosquito", speed_meters_per_seconds=10, weight_gram=3, body_temperature_Celsius=15,
                 number_of_legs=4, color="grey"):
        self.name = name
        self.speed_meters_per_seconds = speed_meters_per_seconds
        self.weight_gram = weight_gram
        self.body_temperature_Celsius = body_temperature_Celsius
        self.number_of_legs = number_of_legs
        self.color = color

    def __del__(self):
        print("{} is deleted".format(self.name))

    def __str__(self):
        return "name of insect is {}, his attribute: speed - {} m/s ," \
               " weight - {} gram, body temperature - {} degrees Celsius," \
               " number of legs - {}, color - {} ".format(self.name,
                                                          self.speed_meters_per_seconds,
                                                          self.weight_gram,
                                                          self.body_temperature_Celsius,
                                                          self.number_of_legs,
                                                          self.color)

    def __repr__(self):
        return "Insect [ name = {},  speed_meters_per_seconds = {},  weight_gram = {},  body_temperature_Celsius = " \
               "{}, number_of_legs = {},  color = {} ] ".format(self.name, self.speed_meters_per_seconds,
                                                                self.weight_gram, self.body_temperature_Celsius,
                                                                self.number_of_legs, self.color)


def main():
    first_insect = Insect()
    second_insect = Insect("dragonfly", 8, 9, color="green")
    third_insect = Insect(speed_meters_per_seconds=15, weight_gram=2)

    print(first_insect)
    print(second_insect, "\n", third_insect)
    insects = []
    insects.append(Insect())
    insects.append(Insect())
    print(insects)


if __name__ == "__main__":
    main()
