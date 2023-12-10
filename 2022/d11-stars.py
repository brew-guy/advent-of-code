import re
import time
from helpers import *

t = time.time()

input = mypath + "d11-input-sample.txt"
with open(input) as f:
    monkeys = [m.split("\n") for m in f.read().split("\n\n")]

# Part 1
# Read input to list split at double linebreaks
# Further split blocks to lines at single linebreak
# Process each monkey block with regex to extract dicts of
#   monkey number, items, operation, test and recipient monkeys
#   operation should be a lambda expression -> eval later
# Create a Monkey class
#   all above attributes
#   attribute to count item inspections
#   function to pass items to other monkey
#   function to inspect item -> recalculate worry level + increase inspection counter
#   function to take a turn -> continue until all items are gone
# Create monkey instances
# Loop through 20 rounds
#   let all monkeys take turns


class Monkey:
    def __init__(self, id, items, oper, test, t_true, t_false, low_worry=True) -> None:
        self.id = id
        self.items = items
        self.oper = eval(oper)
        self.test = test
        self.t_true = t_true
        self.t_false = t_false
        self.low_worry = low_worry
        self.counter = 0

    def throw(self, monkey, item):
        monkey.items.append(item)
        # print(f"Monkey {self.id} throws item {item} to monkey {monkey.id}")

    def inspect(self, item):
        self.counter += 1
        new = self.oper(item)
        worry = new // 3 if self.low_worry else new
        return worry

    def turn(self):
        while len(self.items) > 0:
            old = self.items.pop(0)
            new = self.inspect(old)
            recipient = self.t_true if new % self.test == 0 else self.t_false
            self.throw(monkey_list[recipient], new)


monkey_list = []
for monkey in monkeys:
    m_num = int(re.search("Monkey (\d+)", monkey[0]).group(1))
    m_items = re.search("items: (.*)", monkey[1]).group(1)
    m_items = [int(i) for i in m_items.split(", ")]
    m_oper = "lambda old: " + re.search("Operation: new = (\w.*)", monkey[2]).group(1)
    m_test = int(re.search("Test: divisible by (\d+)", monkey[3]).group(1))
    m_true = int(re.search("If true: throw to monkey (\d+)", monkey[4]).group(1))
    m_false = int(re.search("If false: throw to monkey (\d+)", monkey[5]).group(1))
    monkey_list.append(Monkey(m_num, m_items, m_oper, m_test, m_true, m_false))

for turn in range(20):
    for monkey in monkey_list:
        monkey.turn()

monkey_activity = [m.counter for m in monkey_list]
m1, m2 = sorted(monkey_activity, reverse=True)[:2]
monkey_business = m1 * m2

dropstar(21, monkey_business, t)

# Part 2
t = time.time()

monkey_list = []
for monkey in monkeys:
    m_num = int(re.search("Monkey (\d+)", monkey[0]).group(1))
    m_items = re.search("items: (.*)", monkey[1]).group(1)
    m_items = [int(i) for i in m_items.split(", ")]
    m_oper = "lambda old: " + re.search("Operation: new = (\w.*)", monkey[2]).group(1)
    m_test = int(re.search("Test: divisible by (\d+)", monkey[3]).group(1))
    m_true = int(re.search("If true: throw to monkey (\d+)", monkey[4]).group(1))
    m_false = int(re.search("If false: throw to monkey (\d+)", monkey[5]).group(1))
    monkey_list.append(Monkey(m_num, m_items, m_oper, m_test, m_true, m_false, False))

for turn in range(700):
    for monkey in monkey_list:
        # if turn % 10 == 0:
        #     print(monkey.id, monkey.items)
        monkey.turn()

monkey_activity = [m.counter for m in monkey_list]
m1, m2 = sorted(monkey_activity, reverse=True)[:2]
monkey_business = m1 * m2

dropstar(22, monkey_business, t)
