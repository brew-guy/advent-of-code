import time
import pathlib

mypath = str(pathlib.Path(__file__).parent.resolve()) + "\\"


def dropstar(star_number, answer, startTime):
    laptime = time.time() - startTime
    print(f"Star {star_number}: {answer} | Calc time: {laptime}")
