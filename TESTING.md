# Testing

The test harness uses a [declarative framework](https://pre-commit.com)
with pluggable checks for static tests.

Run:

```bash
sdlc/bootstrap
sdlc/build
sdlc/test
```

Some of the tests update files when necessary.<br/>
If a test updates a file from your commit:

1. Inspect the update to ensure it makes sense.
1. Amend your commit with the update (assuming it makes sense).
1. Run `sdlc/test` again.

For example, the "Update markdown table-of-contents" test detects if a new
header has been added to a markdown file and updates the table-of-contents.

Output resembles:

```conf
[INFO] Check data against schema file schema/acronyms.yaml
data/finance.yaml:  INFO - validation.valid
data/global.yaml:  INFO - validation.valid
data/technology.yaml:  INFO - validation.valid

[INFO] Run declarative checks
Update markdown table-of-contents..........................................Passed
Detect if an email address needs to be added to mailmap....................Passed
Forbid binaries........................................(no files to check)Skipped
Check for conflict markers and core.whitespace errors......................Passed
Check if the git tree is dirty.............................................Passed
Check markdown files.......................................................Passed
Check file encoding........................................................Passed
Non-executable shell script filename ends in .sh...........................Passed
Executable shell script omits the filename extension.......................Passed
Test shell scripts with shellcheck.........................................Passed
Check shell style with shfmt...............................................Passed
codespell..................................................................Passed
yamllint...................................................................Passed
Format YAML files..........................................................Passed
Check for added large files................................................Passed
Check builtin type constructor use.........................................Passed
Check for byte-order marker................................................Passed
Check for case conflicts...................................................Passed
Check docstring is first...................................................Passed
Check that executables have shebangs.......................................Passed
Check JSON.............................................(no files to check)Skipped
Check for merge conflicts..................................................Passed
Check for broken symlinks..............................(no files to check)Skipped
Check vcs permalinks.......................................................Passed
Check Toml.............................................(no files to check)Skipped
Check Xml..............................................(no files to check)Skipped
Check Yaml.................................................................Passed
Detect Private Key.........................................................Passed
Fix End of Files...........................................................Passed
Fix python encoding pragma.................................................Passed
Forbid new submodules......................................................Passed
Mixed line ending..........................................................Passed
Don't commit to branch.....................................................Passed
Pretty format JSON.....................................(no files to check)Skipped
Fix requirements.txt.......................................................Passed
Sort simple YAML files.................................(no files to check)Skipped
Trim Trailing Whitespace...................................................Passed
mypy.......................................................................Passed
check blanket noqa.........................................................Passed
check for not-real mock methods............................................Passed
check for eval()...........................................................Passed
use logger.warning(........................................................Passed
type annotations not comments..............................................Passed
no unicode replacement chars...............................................Passed
pep257.....................................................................Passed
pyupgrade..................................................................Passed
Reorder python imports.....................................................Passed
Add trailing commas........................................................Passed
Strip unnecessary `# noqa`s................................................Passed
CRLF end-lines checker.....................................................Passed
No-tabs checker............................................................Passed
Detect secrets.............................................................Passed
talisman...................................................................Passed
bandit.....................................................................Passed
pydocstyle.................................................................Passed
pylint.....................................................................Passed
autopep8...................................................................Passed
flake8.....................................................................Passed

[PASS] sdlc/test OK
```
