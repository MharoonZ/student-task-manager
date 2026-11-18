# Student Task Manager

Project status: Ready for release after testing

A Python console app for keeping track of schoolwork. Add a non-blank title, list pending and completed tasks, or complete or delete a task by its numeric ID. Tasks are stored in memory and cleared when the app exits.

## Setup and usage

Use Python 3.12 and Git. No Python packages need to be installed.

```sh
git clone https://github.com/MharoonZ/student-task-manager.git
cd student-task-manager
python app.py
```

Choose `A` to add, `L` to list, `C` to complete, `D` to delete, or `Q` to quit. See the [user guide](docs/user-guide.md) for a walkthrough.

## Tests

```sh
python -m unittest discover -s tests -v
```

GitHub Actions runs the suite for pull requests targeting `main` and for pushes to `main`. See the [lab report](LAB-REPORT.md) for the Git workflow and conflict explanation.
