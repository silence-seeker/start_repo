def bubble_sort(arr: list) -> list:
    """冒泡排序：相邻元素两两比较，较大者向后移动。"""
    result = arr.copy()
    n = len(result)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    print("排序后:", bubble_sort(data))
