import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")])

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")

opinions_count = len(opinions.index)
pros_count = 0
cons_count = 0
avg_score = 0

print(opinions_count)