import subprocess
import xml.etree.ElementTree as ET


def run_junit_tests(test_class):
    # 调用命令行运行JUnit测试
    command = ["java", "-cp", "path/to/junit.jar:path/to/your/test/classes", "org.junit.runner.JUnitCore", test_class]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # 解析JUnit XML测试报告
    test_results = []
    xml_root = ET.fromstring(stdout)
    testcases = xml_root.findall(".//testcase")
    for testcase in testcases:
        test_name = testcase.attrib["name"]
        test_result = testcase.attrib["result"]
        test_results.append((test_name, test_result))

    return test_results


# 运行JUnit测试并打印结果
results = run_junit_tests("com.example.MyTestClass")
for test_name, test_result in results:
    print(f"Test: {test_name}, Result: {test_result}")
