import sys
from pathlib import Path

import pytest

# 确保可以从 src 导入模块
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import math_utils  # noqa: E402


def test_add_basic_cases():
    assert math_utils.add(1, 2) == 3
    assert math_utils.add(-1.5, 2.5) == 1.0


def test_mean_normal_list():
    assert math_utils.mean([1, 2, 3, 4]) == 2.5
    assert math_utils.mean([2.5, 3.5]) == 3.0


def test_mean_empty_list_raises():
    with pytest.raises(ValueError):
        math_utils.mean([])
