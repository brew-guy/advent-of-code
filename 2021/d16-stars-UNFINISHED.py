import time
from helpers import *

t = time.time()

input = mypath + "d16-input.txt"
with open(input) as f:
    transmission = f.read()

logging = False
log = lambda line: print(line) if logging else None

# Part 1
hex2bin = lambda hex: "".join([bin(int(n, 16))[2:].zfill(4) for n in hex])
bin2dec = lambda bin: int(bin, 2)

bits = "".join([hex2bin(hex) for hex in transmission])
nibble = lambda bits, len: (bits[:len], bits[len:])  # Bite off len bits, return parts

ver = []


def getPackage(bits, from_op=False):
    version, bits = nibble(bits, 3)
    type_id, bits = nibble(bits, 3)
    ver.append(bin2dec(version))
    log(f"| Ver.: {bin2dec(version)} | Type: {bin2dec(type_id)} |")
    if bin2dec(type_id) == 4:
        return literal(bits, from_op)
    else:
        op_mode, bits = nibble(bits, 1)
        if op_mode == "0":
            return operator15(bits)
        else:
            return operator11(bits)


def literal(bits, from_op, groups=0, literal_value=""):
    group, bits = nibble(bits, 5)
    if group[0] == "0":
        packet_len = 6 + (groups + 1) * 5
        bit_padding = 3 - ((packet_len - 1) % 4) if not from_op else 0
        log(f"| Literal value: {bin2dec(literal_value + group[1:])} |")
        return bin2dec(literal_value + group[1:]), bits[bit_padding:]
    literal_value += group[1:]
    return literal(bits, from_op, groups + 1, literal_value)


def operator15(bits):
    type_bits, bits = nibble(bits, 15)
    type_bits_value = bin2dec(type_bits)
    payload_bits, bits = nibble(bits, type_bits_value)
    log(f"| Op15 | Sub packet bits: {type_bits_value} |")
    while len(payload_bits) > 0:
        result, payload_bits = getPackage(payload_bits, from_op=True)
    return result, bits


def operator11(bits):
    type_bits, bits = nibble(bits, 11)
    packets = bin2dec(type_bits)
    log(f"| Op11 | Sub packets: {packets} |")
    for i in range(packets):
        result, bits = getPackage(bits, from_op=True)
    return result, bits


bn = hex2bin(transmission)
result, bn = getPackage(bn)

dropstar(31, sum(ver), t)

# Part 2

# dropstar(32, , t)
