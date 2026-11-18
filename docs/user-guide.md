# User guide

From the repository root, run `python app.py`.

1. Enter `A`, then type `Finish DevOps lab`. Blank input is rejected; spaces around a valid title are trimmed.
2. Enter `L`. Note the number shown before `[pending]`.
3. Enter `C`, then that number. Enter `L` again to check that the task is now `[done]`.
4. Enter `D`, then the same number to remove the task. Enter `L` to confirm it is gone.
5. Enter `Q` to exit. Start a new session with `python app.py`; previous tasks are not saved.

Complete and delete require a positive whole-number ID from the list. An invalid or unknown ID does not change any task.
