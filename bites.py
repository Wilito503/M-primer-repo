import hashlib

# Coordenada x del punto compartido (1562)
x = int(input("Ingrese la clave compartida: "))
x_bytes = x.to_bytes((x.bit_length() + 7) // 8, byteorder='big')

# Derivar la clave AES de 256 bits (32 bytes) utilizando SHA-256
aes_key = hashlib.sha256(x_bytes).digest()

print("Clave 256 bits:", aes_key.hex())
