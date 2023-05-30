import pytest
import json


def invoke_pytest(program: str, test_case: str, time_out: str):
    # pytest_args = ['-ra', '--cov', 'temp_dir', '--cov-report', 'term', '--no-cov-on-fail', 'temp_dir/test_program.py']
    pytest_args = ['--rootdir', 'temp_dir/', '--json-report', '--json-report-file=temp_dir/report.json',
                   '--json-report-summary', '--cov', 'temp_dir', '--cov-report', 'annotate', '--no-cov-on-fail',
                   'temp_dir/test_program.py']
    pytest.main(pytest_args)
    with open("temp_dir/report.json", "r") as reader:
        report = json.load(reader)
        exitcode = report['exitcode']
        print("exitcode:" + f'{exitcode}')
        summary = report['summary']
        failed = summary['failed']
        print("failed:" + f'{failed}')
        total = summary['total']
        print("total:" + f'{total}')
        if total > 0:
            pass_rate = (total - failed)/total
        else:
            pass_rate = 0.0


if __name__ == "__main__":
    invoke_pytest("", "", "")
