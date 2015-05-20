#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
from pytils.third import six

EXAMPLES = [
    'dt.distance_of_time_in_words.py',
    'dt.ru_strftime.py',
    'numeral.choose_plural.py',
    'numeral.in_words.py',
    'numeral.rubles.py',
    'numeral.sum_string.py',
    'translit.py',
]

name_to_path = lambda x: os.path.join(os.path.normpath(os.path.abspath(os.path.dirname(__file__))), x)
sanitize_output = lambda x: x.replace('#->', '').replace('# ->', '').strip()

def safe_file_iterator(fh, encoding='UTF-8'):
    # Py2.x file iterator returns strings, not unicode
    # Py3 file iterator returns not a bytestrings but string
    # therefore we should decode for Py2.x and leave as is for Py3
    for line in fh:
        if six.PY3:
            yield line
        else:
            yield line.decode(encoding)


def grab_expected_output(name):
    with open(name_to_path(name)) as fh:
        return [sanitize_output(x) for x in safe_file_iterator(fh)
            if x.replace(' ', '').startswith('#->')]


def run_example_and_collect_output(name):
    return [
    x.decode('UTF-8') for x in
    subprocess.check_output(
        ['python', name_to_path(name)], stderr=subprocess.STDOUT).strip().splitlines()]



class ExampleFileTestSuite(object):
    def __init__(self, name):
        self.name = name
        self.expected_output = list(grab_expected_output(name))
        self.real_output = list(run_example_and_collect_output(name))
        assert len(self.real_output) == len(self.expected_output), \
            "Mismatch in number of real (%s) and expected (%s) strings" % (len(self.real_output), len(self.expected_output))
        assert len(self.real_output) > 0
        assert isinstance(self.real_output[0], six.text_type), \
            "%r is not text type (not a unicode for Py2.x, not a str for Py3.x" % self.real_output[0]
        assert isinstance(self.expected_output[0], six.text_type), \
            "%r is not text type (not a unicode for Py2.x, not a str for Py3.x" % self.expected_output[0]
 
    def test_cases(self):
        return range(len(self.real_output))

    def run_test(self, name, i):
        assert name == self.name
        assert isinstance(self.real_output[i], six.text_type)
        assert isinstance(self.expected_output[i], six.text_type)
        # ignore real output if in example line marked with ->>
        if self.expected_output[i].startswith('>'):
            return
        assert self.real_output[i] == self.expected_output[i], \
            "Real output %r doesn't match to expected %r for example #%s" % (self.real_output[i], self.expected_output[i], i)


def test_example():
    for example in EXAMPLES:
        runner = ExampleFileTestSuite(example)
        # we want to have granular test, one test case per line
        # nose show each test as "executable, arg1, arg2", that's
        # why we want pass example name again, even test runner already knows it
        for i in runner.test_cases():
            yield runner.run_test, example, i

def assert_python_version(current_version):
    exec_version = subprocess.check_output(
        ['python', '-c', 'import sys; print(sys.version_info)'], stderr=subprocess.STDOUT).strip()
    assert current_version == exec_version.decode('utf-8')


def test_python_version():
    # check that `python something.py` will run the same version interepreter as it is running
    import sys
    current_version = str(sys.version_info)
    # do a yield to show in the test output the python version
    yield assert_python_version, current_version


if __name__ == '__main__':
    import nose, sys
    if not nose.runmodule():
        sys.exit(1)