"""数学工具函数。"""
from __future__ import annotations

from typing import Iterable


def add(a: float, b: float) -> float:
    """返回两个数的和。"""
    return a + b


def mean(numbers: Iterable[float]) -> float:
    """计算数值序列的算术平均值。"""
    nums = list(numbers)
    if not nums:
        raise ValueError("numbers 不能为空")
    return sum(nums) / len(nums)
