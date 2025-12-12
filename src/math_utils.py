"""数学工具函数。

提供简单的加法与平均值计算。
"""
from typing import Iterable


def add(a: float, b: float) -> float:
    """返回两个数的和。"""
    return a + b


def mean(numbers: Iterable[float]) -> float:
    """返回一组数字的平均值，空序列会抛出 ValueError。"""
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers 不能为空")
    return sum(nums) / len(nums)
