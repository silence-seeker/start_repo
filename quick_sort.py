def quick_sort(arr: list) -> list:
    """快速排序：选基准值，小于的放左边，大于的放右边，再递归排序。"""
    if len(arr) <= 1:
        return arr.copy()

    result = arr.copy()
    _quick_sort_inplace(result, 0, len(result) - 1)
    return result


def _quick_sort_inplace(arr: list, left: int, right: int) -> None:
    if left >= right:
        return

    pivot_index = _partition(arr, left, right)
    _quick_sort_inplace(arr, left, pivot_index - 1)
    _quick_sort_inplace(arr, pivot_index + 1, right)


def _partition(arr: list, left: int, right: int) -> int:
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    print("排序后:", quick_sort(data))
