import os
from pathlib import Path
import unittest
import shutil
import argparse


def get_file_name(module_name) -> str:
    return f"{module_name}.py"


def get_solution_name(module_name) -> str:
    return f"{module_name}_solution.py"

def get_starter_name(module_name) -> str:
    return f"{module_name}.py"

def run_tests(file_location: str, test_location: str, verbosity: int):
    loader = unittest.TestLoader()
    tests = loader.discover(test_location, top_level_dir=file_location)
    runner = unittest.TextTestRunner(verbosity=verbosity)
    res = runner.run(tests)
    return res


def test_module(test_type:str, module_name: str, module_dir: Path, verbosity=1):
    assert module_dir.is_dir(), "Module specified is not valid"
    test_dir = module_dir / "staff/gradescope/tests"
    assert test_dir.is_dir(), "Test directory is not set up correctly"
    if test_type=="starter":
        sol_file = module_dir / "student" / get_starter_name(module_name)
    else:
        sol_file = module_dir / "staff" / get_solution_name(module_name)

    if sol_file.exists():
        tmp_file = test_dir / get_file_name(module_name)
        shutil.copyfile(sol_file, tmp_file)
        res = run_tests(test_dir, test_dir, verbosity)
        os.remove(tmp_file)
        print(res)
    else:
        if test_type=="starter":
            raise Exception(
                f"ERROR: Starter file not found: {get_starter_name(module_name)}"
            )
        else:
            raise Exception(
                f"ERROR: Solution file not found: {get_solution_name(module_name)}"
            )


def main():
    current_dir = Path(os.path.dirname(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument("module_name", type=str)
    parser.add_argument('type', choices=['starter', 'solution'])
    parser.add_argument("-v", "--verbosity", type=int, default=1)
    args = parser.parse_args()
    test_module(args.type, args.module_name, current_dir / args.module_name, args.verbosity)


if __name__ == "__main__":
    main()
