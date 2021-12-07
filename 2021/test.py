a = (306, 537)
b = (38, 805)  # (39, 804) ... (306, 537)

x1, y1, x2, y2 = a[0], a[1], b[0], b[1]

x_range = range(min(x1, x2), max(x1, x2) + 1)
y_range = range(min(y1, y2), max(y1, y2) + 1)
if y1 < y2:
    y_range = reversed(y_range)

c = zip(x_range, y_range)
