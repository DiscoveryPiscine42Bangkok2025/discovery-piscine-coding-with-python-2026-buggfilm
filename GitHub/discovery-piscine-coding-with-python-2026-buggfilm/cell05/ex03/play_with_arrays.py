#!/usr/bin/env python3

def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]

    # สมมติ logic เดิม: +2 ทุกตัว
    result = []
    for n in arr:
        result.append(n + 2)

    # ลบค่าซ้ำ โดยไม่ไปยุ่ง arr เดิม
    result = list(set(result))

    # ถ้าอยากเรียงค่า
    result.sort()

    print(arr)
    print(result)

if __name__ == "__main__":
    main()
