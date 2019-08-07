import argparse
import sys
from pathlib import Path
import os
import glob
import shutil

from common_tasks import run_check_call

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..'))
dev_setup_script_location = os.path.join(root_dir, 'scripts/dev_setup.py')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'This script is used to execute mypy against a specific folder. Tox does not support ')

    parser.add_argument(
        '-p',
        '--package_dir',
        dest='package_dir',
        help='Specific set of named environments to execute'
    )

    args = parser.parse_args()

    print(args.package_dir)

    # if sys.version_info >= (3, 5):
    #     run_check_call(['mypy', args.package_dir], args.package_dir)
    # else:
    #     print('Mypy is not supported on < Python 3.5')


