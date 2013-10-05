#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys

def test_python_version():
    """Verify that /usr/bin/env python is pointing out to the current python"""
    python_version = subprocess.check_output(['python', '--version'], stderr=subprocess.STDOUT).strip()
    python, version = python_version.split()
    assert sys.version.split()[0] == version.decode('utf-8')



if __name__ == '__main__':
    import nose, sys
    if not nose.runmodule():
        sys.exit(1)