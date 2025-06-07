#!/usr/bin/python3

file_path = input("Enter the file path:")

try:
    with open(file_path, 'r') as f:
        hex_string = f.read().replace("0x", "").replace("byte[] rsrc = new byte[464] {", "").replace("};", "").replace(",", "")
        hex_encode = hex_string.encode()

    with open("out.bin", "wb") as out:
        out.write(hex_encode)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}") 
