from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray
import timeit
import time

pathList = ['49.in', '499.in', '4999.in', '9999.in', '17499.in', '49999.in']
path = pathList[0]
text = open(path, 'r')
text = text.read()

start = timeit.default_timer()

freq_lib = defaultdict(int)
for ch in text:
    freq_lib[ch] += 1

# Huffman Tree
heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]
heapify(heap)

while len(heap) > 1:
    right = heappop(heap)
    left = heappop(heap)

    for pair in right[1:]:
        pair[1] = '0' + pair[1]
    for pair in left[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])

huffman_list = right[1:] + left[1:]
huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}

# Huffman encoding
encoded_text = bitarray()
encoded_text.encode(huffman_dict, text)
end = timeit.default_timer()

with open('compressed_file.bin', 'wb') as w:
    encoded_text.tofile(w)

print(f'\narquivo {path}')
print('tempo de processamento: %f' % (end - start))

# Decodificação
padding = 8 - (len(encoded_text) % 8)
decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)

decoded_text = decoded_text[:-padding]

decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)

print(decoded_text)