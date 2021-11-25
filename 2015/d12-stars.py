import time, re, json
from helpers import *

t = time.time()

input = "d12-input.txt"
with open(input) as f:
    document = f.read()

# Part 1
numbers = re.findall("-?[0-9]+", document)
numbers = list(map(int, numbers))

dropstar(23, sum(numbers), t)

# Part 2
def redact(data, match):
    if isinstance(data, dict):  # Find dicts
        if match in data.values():
            pass  # Leave out whole dict if matched value found
        else:
            return {k: redact(v, match) for k, v in data.items()}
    elif isinstance(data, list):  # Find lists
        return [redact(i, match) for i in data]
    else:  # Find everything else
        return data


json_document = json.loads(document)
redacted = redact(json_document, "red")
redact_document = json.dumps(redacted)

numbers = re.findall("-?[0-9]+", redact_document)
numbers = list(map(int, numbers))

dropstar(24, sum(numbers), t)
