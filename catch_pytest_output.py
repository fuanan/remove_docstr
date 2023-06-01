import pytest

program = '''
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
'''

test_case = '''
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
'''

with open(".\\temp_dir\\program.py", "w") as p:
    p.write(program)

with open(".\\temp_dir\\test_program.py", "w") as tc:
    tc.write(test_case)

pytest_args = ['--rootdir', 'temp_dir/', '--json-report', '--json-report-file=temp_dir/report.json',
                   '--json-report-summary', '--cov', 'temp_dir', '--cov-report', 'term', '--no-cov-on-fail', '-q',
               '--show-capture=no', '--no-summary', 'temp_dir/test_program.py']

pytest.main(pytest_args)



code = '''
print("这是一条输出")
x = 42
print("变量x的值是:", x)
'''

import sys, os

original_stdout = sys.stdout

sys.stdout = open('exec_output.txt', 'w')

exec(code)

file = sys.stdout

sys.stdout = original_stdout

file.close()

os.remove("exec_output.txt")




