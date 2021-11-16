# Day 6 - Part 1
import re
import time
startTime = time.time()

# Read merged group responses to array
input = "d6-input.txt"
with open(input) as f:
	forms = f.read()
forms = re.sub(r'(\w)\n', r'\1 ', forms).replace(' ','').split('\n')

print("Received {0} group forms.".format(len(forms)))

any_yes_responders = map(lambda form: len({letter: True for letter in form}), forms)

print("Sum of all the unique group form responses were {0}.".format(sum(list(any_yes_responders))))
print('Execution time in seconds: {0}'.format(time.time() - startTime))