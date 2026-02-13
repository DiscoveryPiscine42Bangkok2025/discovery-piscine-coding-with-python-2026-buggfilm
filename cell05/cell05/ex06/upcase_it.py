import sys

# ต้องมี 2 ค่า (ชื่อไฟล์ + parameter 1 ตัว)
if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())
