# CSC418 — Lab Assignment 4

## Git and GitHub

Git tracks changes locally. GitHub hosts the repository and adds collaboration tools. `git add` stages the edits for the next snapshot, `git commit` records that snapshot in the local history, and `git push` sends the new commits to the remote.

## Branches, pull requests, and the README conflict

A branch lets a feature develop without changing `main` until it is ready. A pull request shows the differences between branches and gives reviewers a place to discuss them before merging. The add, complete, and delete PRs each separate the data-layer change from the console change.

The two documentation branches started from `Project status: Planning`. One replaced it with `Testing`; the other replaced it with `Ready for release`. After the testing PR merged, Git could not choose between edits to the same line. The resolution kept one status, `Ready for release after testing`, and preserved the rest of the file. [PR #9](https://github.com/MharoonZ/student-task-manager/pull/9) records the merge.

## Fetch versus pull; merge versus rebase

`git fetch` downloads remote commits and updates remote-tracking refs without changing the current branch. `git pull` fetches and then integrates the remote branch; this lab uses `git pull --ff-only` to avoid accidental merge commits while syncing. Merging combines histories and may create a two-parent commit. Rebasing replays commits on a new base and changes their IDs, so avoid rebasing shared work without coordination.

## Issues and Actions

Issues turn planned work and defects into trackable items; labels identify the kind of work and PR links show where it was fixed. Actions runs the same tests for each PR and each update to `main`, making failures visible before release.

## Difficulty and resolution

The CI demonstration used an intentionally inverted assertion: it expected the selected task to stay incomplete after calling `complete`. The [failed run](https://github.com/MharoonZ/student-task-manager/actions/runs/44259549606) showed the assertion mismatch. Changing the expectation to `True` fixed the test without weakening its separate check that the other task stayed incomplete.

To inspect the branch history locally, run `git log --graph --oneline --all`. The [evidence folder](lab-evidence/) records the GitHub pages for branches, issues, merges, the conflict, and CI.
