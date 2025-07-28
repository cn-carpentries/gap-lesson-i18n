# GAP Example Test for The Carpentries GAP Curriculum

This repository provides a testing framework and code generation pipeline for validating GAP code examples used in The Carpentries' [GAP course](https://carpentries-incubator.github.io/gap-lesson/). It extracts code from lesson Markdown files and automatically generates `.tst` files, which are run and compared using GAP’s testing tools.

## Project Structure

.
├── episodes/          # Original Markdown lesson files (input)
├── tst/               # Generated .tst test files (output)
├── log/               # Test output logs (auto-generated)
├── generate\_tst.py    # Script to extract GAP/output blocks from Markdown
├── testall.g          # GAP entry script to run all tests
└── run\_tests.sh       # Bash script to generate .tst files and run tests


## How to Use

### 1. Generate `.tst` Files and Run Tests

Run the following in your terminal:

```bash
./run_tests.sh
```

This script will:

1. Run `generate_tst.py` to convert ` ```gap` and ` ```output` blocks from `episodes/*.md` into `.tst` files.
2. Use GAP to run the tests via `testall.g`.
3. Save a full log (with timestamp) in the `log/` directory and stream output to your terminal.

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

This runs all `.tst` files in the current directory and compares output using GAP’s `uptowhitespace` comparison.

## Useful references
1. How GAP tests work: https://carpentries-incubator.github.io/gap-lesson/04-testing.html 
2. GAP documentation: https://docs.gap-system.org/doc/ref/chap7_mj.html#X87712F9D8732193C
3. How to install GAP: https://www.gap-system.org/install/


