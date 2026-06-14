import sys
import os

repo_root = os.path.dirname(__file__)
lib_dir = os.path.join(repo_root, 'lib')
# ensure lib is on sys.path so `from cash_register import CashRegister` works
sys.path.insert(0, lib_dir)

from testing import cash_register_test

failed = False

# instantiate test class
# run all methods that start with test_
test_file = os.path.join(lib_dir, 'testing', 'cash_register_test.py')
method_names = []
with open(test_file, 'r') as fh:
    for line in fh:
        line = line.strip()
        if line.startswith('def test_'):
            # extract method name
            name = line.split('def ')[1].split('(')[0]
            method_names.append(name)

for name in method_names:
    T = cash_register_test.TestCashRegister()
    method = getattr(T, name)
    try:
        method()
        print(f"{name}: OK")
    except AssertionError as e:
        print(f"{name}: FAIL - AssertionError: {e}")
        failed = True
    except Exception as e:
        print(f"{name}: ERROR - {e}")
        failed = True

if failed:
    sys.exit(1)
else:
    print('All tests passed')
