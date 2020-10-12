from base64 import b64encode
print(str(b64encode(input().encode()))[2:-1])