import jsonlines
import re


def main():
    # py_docstr_re = r'    """[\n]?.*"""[\n]'
    py_docstr_re = r'    [\"\']{3}[\s\S]*?[\"\']{3}[\s]'
    py_com_re = r'[ ]*#.*'
    jsonl_file_path = "D:\\humaneval-dataset\\human-eval-v2-20210705.jsonl"
    with jsonlines.open(jsonl_file_path) as f:
        for item in f:
            str1 = item['prompt'] + item['canonical_solution']
            result = re.findall(py_docstr_re, str1)
            id = item['task_id']
            str2 = re.sub(py_docstr_re, '', str1)
            str3 = re.sub(py_com_re, '', str2)
            print(id)
            print("---------------------------")
            print(str1)
            print("---------------------------")
            print(str3)
            print("---------------------------")


if __name__ == '__main__':
    main()
