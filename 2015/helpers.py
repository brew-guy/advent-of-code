import time


def dropstar(star_number, answer, startTime):
    laptime = time.time() - startTime
    print(f"Execution time in seconds: {laptime}")
    print(f"Star {star_number}: {answer}")


# class Starclass(object):
#     def __init__(self, star_number, answer):
#         self.startTime = time.time()
#         self.star_number = star_number
#         self.answer = answer

#     def dropstar(self):
#         laptime = time.time() - self.startTime
#         print(f"Execution time in seconds: {laptime}")
#         print(f"Star {star_number}: {answer}")
