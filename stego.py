import cv2  # type: ignore
import os
import string

# Ensure the image path is correct and the file exists
img_path = "mypic.jpg"  # Replace with the correct path if needed
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Image file not found: {img_path}")

img = cv2.imread(img_path)
# Check if the image was loaded successfully
if img is None:
    raise IOError(f"Failed to load image from {img_path}. Please check the file path and permissions.")

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")