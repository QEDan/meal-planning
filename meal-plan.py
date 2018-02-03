import pandas as pd
import argparse
import logging as log

DEFAULT_DATABASE = "meal-database.csv"
NUM_MEALS = 3

class MealDatabase:
    def __init__(self, database=DEFAULT_DATABASE):
        self.database = database
        self.loadDatabase()

    def loadDatabase(self):
        try:
            self.df = pd.read_csv(self.database)
        except IOError as e:
            log.error("Error reading meal database: " + e)
        except Exception as e:
            log.error("Error: " + e)

    def sampleMeals(self, num_meals=3):
        return self.df.sample(n=num_meals,
                              weights=self.df['weight'])

    def printPlan(self, num_meals=3):
        print("This week's meals")
        sample = self.sampleMeals(num_meals=num_meals)
        print(sample[['name', 'details']].to_string(index=False))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--database",
                        dest="database",
                        default=DEFAULT_DATABASE,
                        help="Data base of meals (csv)"
                        )
    parser.add_argument("-n", "--num_meals",
                        dest="num_meals",
                        nargs="?",
                        default=NUM_MEALS,
                        type=int,
                        help="Number of meals to generate"
                        )
    args = parser.parse_args()
    meal_database = MealDatabase(database=args.database)
    meal_database.printPlan()
