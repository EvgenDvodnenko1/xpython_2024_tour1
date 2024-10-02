import time


cloth_type = [
    {
        "name": "Бавовна",
        "temperature": "40-90ºC",
        "spin_power": "сильний віджим"
    },
    {
        "name": "Синтетика",
        "temperature": "30-40ºC",
        "spin_power": "середній віджим"
    },
    {
        "name": "Делікатний",
        "temperature": "30ºC",
        "spin_power": "слабкий віджим"
    }
]


class Modes:
    def mode(self, mode, sleep_time):
        print(f"\nЗараз ваша пральна машинка в режимі {mode}...")
        time.sleep(sleep_time)

    def finish(self, mode):
        print(f"\n{mode} закінчено :) Можете забирати речі")


class WashingMachine(Modes):
    def __init__(self, make, color):
        self.make = make
        self.color = color
