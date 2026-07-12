from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar("T")


@dataclass
class SortStats:
    """记录归并排序过程中的统计信息。"""

    comparisons: int = 0
    merges: int = 0

    def reset(self) -> None:
        self.comparisons = 0
        self.merges = 0


def merge_sort(
    arr: list[T],
    *,
    reverse: bool = False,
    key: Callable[[T], object] | None = None,
    stats: SortStats | None = None,
) -> list[T]:
    """自顶向下归并排序：递归二分，再合并有序子数组。"""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], reverse=reverse, key=key, stats=stats)
    right = merge_sort(arr[mid:], reverse=reverse, key=key, stats=stats)
    return _merge(left, right, reverse=reverse, key=key, stats=stats)


def merge_sort_iterative(
    arr: list[T],
    *,
    reverse: bool = False,
    key: Callable[[T], object] | None = None,
    stats: SortStats | None = None,
) -> list[T]:
    """自底向上归并排序：按 1、2、4… 的宽度逐层合并，避免递归栈开销。"""
    if len(arr) <= 1:
        return arr.copy()

    segments: list[list[T]] = [[item] for item in arr]

    while len(segments) > 1:
        merged_segments: list[list[T]] = []
        for i in range(0, len(segments), 2):
            if i + 1 < len(segments):
                merged_segments.append(
                    _merge(
                        segments[i],
                        segments[i + 1],
                        reverse=reverse,
                        key=key,
                        stats=stats,
                    )
                )
            else:
                merged_segments.append(segments[i])
        segments = merged_segments

    return segments[0]


def _merge(
    left: list[T],
    right: list[T],
    *,
    reverse: bool = False,
    key: Callable[[T], object] | None = None,
    stats: SortStats | None = None,
) -> list[T]:
    if stats is not None:
        stats.merges += 1

    result: list[T] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if stats is not None:
            stats.comparisons += 1

        left_value = key(left[i]) if key else left[i]
        right_value = key(right[j]) if key else right[j]

        if (left_value > right_value) if reverse else (left_value <= right_value):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def _run_demo(title: str, arr: list, **kwargs) -> None:
    stats = SortStats()
    sorted_arr = merge_sort(arr, stats=stats, **kwargs)
    print(f"\n{title}")
    print(f"  排序前: {arr}")
    print(f"  排序后: {sorted_arr}")
    print(f"  比较次数: {stats.comparisons}, 合并次数: {stats.merges}")


if __name__ == "__main__":
    print("=" * 50)
    print("归并排序演示")
    print("=" * 50)

    _run_demo("1. 基础整数排序", [64, 34, 25, 12, 22, 11, 90])

    _run_demo("2. 降序排序", [64, 34, 25, 12, 22, 11, 90], reverse=True)

    _run_demo("3. 按字符串长度排序", ["pear", "fig", "watermelon", "kiwi"], key=len)

    _run_demo("4. 边界情况", [])
    _run_demo("5. 单元素", [42])
    _run_demo("6. 已有序", [1, 2, 3, 4, 5])

    print("\n7. 稳定性验证（相等键保持原有相对顺序）")
    items = [("b", 2), ("a", 1), ("b", 3), ("a", 4)]
    stable_sorted = merge_sort(items, key=lambda x: x[0])
    print(f"  排序前: {items}")
    print(f"  排序后: {stable_sorted}")
    print("  说明: 两个 'a' 和两个 'b' 的先后关系与输入一致")

    print("\n8. 递归版 vs 迭代版")
    data = [38, 27, 43, 3, 9, 82, 10]
    recursive_stats = SortStats()
    iterative_stats = SortStats()
    recursive_result = merge_sort(data, stats=recursive_stats)
    iterative_result = merge_sort_iterative(data, stats=iterative_stats)
    print(f"  原始数据:   {data}")
    print(f"  递归结果:   {recursive_result}")
    print(f"  迭代结果:   {iterative_result}")
    print(f"  结果一致:   {recursive_result == iterative_result}")
    print(
        f"  递归统计:   比较 {recursive_stats.comparisons} 次, "
        f"合并 {recursive_stats.merges} 次"
    )
    print(
        f"  迭代统计:   比较 {iterative_stats.comparisons} 次, "
        f"合并 {iterative_stats.merges} 次"
    )
