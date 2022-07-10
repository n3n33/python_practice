# 선택 정렬 
array1 = [7,5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array1)):
    min_index = i
    for j in range(i+1, len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
    array1[i], array1[min_index] = array1[min_index], array1[i] # 스와프


print(array1)

# 삽입 정렬
array2 = [7,5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array2)):
    for j in range(i, 0, -1): # 인덱스 i분터 1까지 감소
        if array2[j] < array2[j - 1] : # 왼쪽으로 이동
            array2[j], array2[j-1] = array2[j-1], array2[j]
        else:
            break

print(array2)