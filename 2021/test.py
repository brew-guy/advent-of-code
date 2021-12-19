template = "NNCB"
# N:2, C:1, B:1

# NN -> NC, CN
# NC -> NB, BC
# CB -> CH, HB
# N:2, C:2, B:2, H:1
# -> NCNBCHB
# N:2, C:2, B:2, H:1


a = {"a": 5, "b": 10}
for i in a.items():
    print(i)
