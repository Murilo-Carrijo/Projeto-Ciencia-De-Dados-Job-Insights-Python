from functools import lru_cache
import csv


@lru_cache
def read(path):
    lines = []
    with open(path, encoding="utf-8") as file:
        csv_data = csv.DictReader(file)
        for line in csv_data:
            lines.append(line)
        return lines
