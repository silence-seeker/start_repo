def insertion_sort(arr: list) -> list:
    """插入排序：将每个元素插入到已排序部分的正确位置。"""
    result = arr.copy()

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key

    return result


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    print("排序后:", insertion_sort(data))
