
import pytest
from typing import List

from program import *

def test_has_close_elements():
    # 测试用例1: 具有相近元素，小于阈值
    numbers1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold1 = 1.5
    assert has_close_elements(numbers1, threshold1) == True

    # 测试用例2: 具有相近元素，大于阈值
    numbers2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold2 = 0.5
    assert has_close_elements(numbers2, threshold2) == False

    # 测试用例3: 仅有一个元素
    numbers3 = [1.0]
    threshold3 = 0.1
    assert has_close_elements(numbers3, threshold3) == False

    # 测试用例4: 空列表
    numbers4 = []
    threshold4 = 1.0
    assert has_close_elements(numbers4, threshold4) == False

    # 测试用例5: 具有相近元素，阈值为负数
    numbers5 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold5 = -1.0
    assert has_close_elements(numbers5, threshold5) == False

    # 测试用例6: 具有相近元素，阈值为0
    numbers6 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold6 = 0
    assert has_close_elements(numbers6, threshold6) == False
