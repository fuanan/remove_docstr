
import pytest
from typing import List

from program import *

def test_has_close_elements():
    # ��������1: �������Ԫ�أ�С����ֵ
    numbers1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold1 = 1.5
    assert has_close_elements(numbers1, threshold1) == True

    # ��������2: �������Ԫ�أ�������ֵ
    numbers2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold2 = 0.5
    assert has_close_elements(numbers2, threshold2) == False

    # ��������3: ����һ��Ԫ��
    numbers3 = [1.0]
    threshold3 = 0.1
    assert has_close_elements(numbers3, threshold3) == False

    # ��������4: ���б�
    numbers4 = []
    threshold4 = 1.0
    assert has_close_elements(numbers4, threshold4) == False

    # ��������5: �������Ԫ�أ���ֵΪ����
    numbers5 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold5 = -1.0
    assert has_close_elements(numbers5, threshold5) == False

    # ��������6: �������Ԫ�أ���ֵΪ0
    numbers6 = [1.0, 2.0, 3.0, 4.0, 5.0]
    threshold6 = 0
    assert has_close_elements(numbers6, threshold6) == False
