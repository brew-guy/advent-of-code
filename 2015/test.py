import re
from time import process_time_ns

a = "Orangutang"

regexp = r"an"
match = re.finditer(regexp, a)

replace = "*"
for m in match:
    print(a[: m.start()] + replace + a[m.end() :])

