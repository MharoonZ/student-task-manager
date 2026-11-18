from task_manager import TaskManager


def main():
    manager = TaskManager()
    while True:
        command = input('[A]dd [L]ist [Q]uit: ').strip().lower()
        if command == 'q':
            return
        if command == 'a':
            try:
                task = manager.add(input('Title: '))
            except ValueError as error:
                print(error)
            else:
                print(f'Added task {task.identifier}.')
        elif command == 'l':
            tasks = manager.display()
            if not tasks:
                print('No tasks yet.')
            for task in tasks:
                status = 'done' if task.completed else 'pending'
                print(f'{task.identifier}. [{status}] {task.title}')
        else:
            print('Choose an option from the menu.')


if __name__ == '__main__':
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print('\nGoodbye.')
