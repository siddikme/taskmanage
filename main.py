class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self):
        self.tasks.append(input("New task: "))

    def edit(self):
        i = int(input("Task index to edit: ")) - 1
        self.tasks[i] = input("Updated task: ") if 0 <= i < len(self.tasks) else print("Invalid index")

    def delete(self):
        i = int(input("Task index to delete: ")) - 1
        self.tasks.pop(i) if 0 <= i < len(self.tasks) else print("Invalid index")

    def show(self):
        print("\n".join(f"{i+1}. {t}" for i, t in enumerate(self.tasks)) if self.tasks else "No tasks")

tm = TaskManager()
while True:
    opt = input("\nOptions: 1-Add, 2-Edit, 3-Delete, 4-Show, 5-Exit\nChoose: ")
    if opt == '1': tm.add()
    elif opt == '2': tm.edit()
    elif opt == '3': tm.delete()
    elif opt == '4': tm.show()
    elif opt == '5': break
print("You exited of the program!")

