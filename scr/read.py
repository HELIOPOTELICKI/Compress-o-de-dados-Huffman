padding = 8 - (len(encoded_text) % 8)
decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)

decoded_text = decoded_text[:-padding]  # remove padding

decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)

print(decoded_text)