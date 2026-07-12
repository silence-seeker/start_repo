def selection_sort(arr: list) -> list:
    """选择排序：每轮从未排序部分选出最小元素，放到已排序部分末尾。"""
    result = arr.copy()
    n = len(result)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]

    return result


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    print("排序后:", selection_sort(data))
