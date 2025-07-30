# GAP Example Test for The Carpentries GAP Lesson

This repository provides a testing framework and code generation pipeline for validating GAP code examples used in The Carpentries' [GAP course](https://carpentries-incubator.github.io/gap-lesson/). It extracts code from lesson Markdown files and automatically generates `.tst` files, which are run and compared using GAP’s testing tools.

## Project Structure

```
.
├── episodes/            # Original Markdown lesson files (input)
├── code/              # Source files referenced by Read("...")
└── tst/                 # All test-related content lives here
    ├── defs/            # GAP files containing shared function definitions
    ├── log/             # Test output logs (auto-generated)
    ├── generate_tst.py  # Script to extract GAP/output blocks from Markdown
    ├── testall.g        # GAP entry script to run all .tst tests
    └── run_tests.sh     # Shell script to generate and run tests
```

## How to Use

### 1. Generate `.tst` Files and Run Tests

Run the following in your terminal:

```bash
./run_tests.sh
```

This script will:

1. Run `generate_tst.py` to extract ` ```gap`, ` ```output`, and ` ```error` blocks from `episodes/*.md`.
2. Automatically generate `.tst` files in the current directory.
3. Insert `Read("defs/functions.g")` if any GAP code block uses functions like `AvgOrdOfGroup`.
4. Detect and copy files referenced via `Read("...")` from the `code/` directory into the test directory.
5. Use GAP to execute the tests via `testall.g`.
6. Save a full timestamped log in the `log/` directory and display results in the terminal.

### 2. GAP Entry Script: `testall.g`

```gap
TestDirectory(DirectoryCurrent(),
  rec(
    exitGAP     := true,
    testOptions := rec(compareFunction := "uptowhitespace")
  )
);
FORCE_QUIT_GAP(1);  # failsafe fallback if tests don't exit properly
```

This script runs all `.tst` files in the current directory and compares output using GAP’s `uptowhitespace` comparison, ignoring formatting differences.

## Notes

* Any code block containing `return` will be skipped to avoid execution issues in `.tst` format.
* Files referenced with `Read("filename.g")` must exist in the `code/` directory; they will be copied before test execution.
* The special file `04-testing.md` is ignored by the generator and is used only for manual testing.

## Useful references

1. How GAP tests work: https://carpentries-incubator.github.io/gap-lesson/04-testing.html 
2. GAP documentation: https://docs.gap-system.org/doc/ref/chap7_mj.html#X87712F9D8732193C
3. How to install GAP: https://www.gap-system.org/install/
