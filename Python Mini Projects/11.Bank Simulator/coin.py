#Singapore Coins

import random

class Coin:

    def __init__(self, rare=False, clean=True, on_heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean

        self.value = self.original_value*1.25 if self.is_rare else self.original_value
        self.color = self.clean_color if self.is_clean else self.rusty_color
        self.on_heads = on_heads
        
    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def flip(self):
        options = [True, False]
        choice = random.choice(options)
        self.on_heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "c{} Coin".format(int(self.original_value *100))

    def __del__(self):
        print("Coin Spent! for {}".format(self.original_value))


class One_Dollar(Coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_color" : "gold",
            "rusty_color": "greenish",
            "num_of_edges": 1,
            "diameter": 24.65,
            "thickness": 2.50,
            "mass": 7.62,
        }

        super().__init__(**data)

class Five_Cent(Coin):
    def __init__(self):
        data = {
                "original_value" : 0.05,
                "clean_color" : "bronze",
                "rusty_color": "brownish",
                "num_of_edges": 1,
                "diameter": 16.75,
                "thickness": 1.22,
                "mass": 1.70,
            }

        super().__init__(**data)

class Ten_Cent(Coin):
    def __init__(self):
        data = {
                "original_value" : 0.10,
                "clean_color" : "silver",
                "rusty_color": "reddish brown",
                "num_of_edges": 1,
                "diameter": 18.50,
                "thickness": 1.38,
                "mass": 2.36,
            }
        super().__init__(**data)


class Twenty_Cent(Coin):
    def __init__(self):
        data = {
                "original_value" : 0.20,
                "clean_color" : "silver",
                "rusty_color": "reddish brown",
                "num_of_edges": 1,
                "diameter": 21.00,
                "thickness": 1.72,
                "mass": 3.85,
            }
        super().__init__(**data)

class Fifty_Cent(Coin):
    def __init__(self):
        data = {
                "original_value" : 0.50,
                "clean_color" : "silver",
                "rusty_color": "reddish brown",
                "num_of_edges": 1,
                "diameter": 23.00,
                "thickness": 2.50,
                "mass": 7.62,
            }
        super().__init__(**data)


def main():
    coins = [One_Dollar(), Five_Cent(), Twenty_Cent(), Ten_Cent(), Five_Cent()]

    for coin in coins:
        arguments = [
                coin, coin.color, coin.value, coin.diameter, 
                coin.thickness,coin.mass,coin.num_of_edges
            ]

        string = "{} - Color: {}, Value: {}, Diameter(mm): {}, Thickness(mm): {}, Mass(mm): {}, Num Of Edges:{}".format(*arguments)

        print(string)

if __name__ == "__main__":
    main()