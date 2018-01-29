import sys
import binascii

init_byte = 0x0f

def step(current_byte, in_bit):
    out_bit = in_bit ^ ((current_byte & 0x20) >> 5)
    next_byte = (current_byte & 0x01) << 7
    next_byte |= (current_byte & 0x18) << 2
    next_byte |= (current_byte & 0x80) >> 3
    next_byte |= (current_byte & 0x06) << 1
    next_byte |= (current_byte & 0x40) >> 5
    next_byte |= ((current_byte & 0x40) >> 6) ^ ((current_byte & 0x20) >> 5) ^ ((current_byte & 0x08) >> 3) ^ ((current_byte & 0x02) >> 1) ^ 0x01
    return next_byte, out_bit

def run(data, state=init_byte):
    ret = []
    for d in data:
        state, r = step(state, d)
        ret.append(r)
    return ret

def n2ba(n, bit_length=None):
    assert(n >= 0)
    if bit_length is None:
        bit_length = n.bit_length() if n > 0 else 1
    return [(n >> i) & 1 for i in range(bit_length)]

def ba2n(ba):
    n = 0
    for i in range(len(ba)):
        n |= ba[i] << i
    return n

def ba2s(ba):
    assert(len(ba) % 8 == 0)
    r = []
    c = 0
    for i in range(0, len(ba), 8):
        for j, e in zip(range(8), ba[i:i+8]):
            c |= e << j
        r.insert(0, chr(c))
        c = 0
    return ''.join(r)

if __name__=='__main__':
    code = '2FED5B7FEB81D3C44E39E4AEA346010240E0CBBB'
    ba = n2ba(int(code, 16), len(code) * 4)
    for i in range(256):
        ret = ba2s(run(ba, i))
        if (ret[:5] == '34C3_'):
            print ret
