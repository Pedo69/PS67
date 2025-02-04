def quicksort(arr):
    if len(arr) <= 1:  # กรณีฐาน: ถ้าอาร์เรย์มี 1 หรือน้อยกว่าตัวเลข ไม่ต้องจัดเรียง
        return arr

    pivot = arr[len(arr) // 2]  # เลือกจุดหมุนเป็นค่าตรงกลาง
    left = [x for x in arr if x < pivot]  # ตัวเลขที่น้อยกว่า pivot
    middle = [x for x in arr if x == pivot]  # ตัวเลขที่เท่ากับ pivot
    right = [x for x in arr if x > pivot]  # ตัวเลขที่มากกว่า pivot

    return quicksort(left) + middle + quicksort(right)  # เรียกใช้งานแบบเรียกซ้ำ (recursion)

arr = [4, 3, 1, 2, 5, 9, 7, 10, 6]
sorted_arr = quicksort(arr)
print(sorted_arr)