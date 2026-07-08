class Workspace:
    def __init__(self, workspace_id: int, windows: list = None):
        self.workspace_id = workspace_id
        self.windows = windows if windows is not None else []

    def open_window(self, window_name: str):
        self.windows.append(window_name)

    def __len__(self):
        return len(self.windows)

    def __eq__(self, other):
        if not isinstance(other, Workspace):
            return NotImplemented
        return len(self.windows) == len(other.windows)


ws1 = Workspace(1)
ws1.open_window("kitty")
ws1.open_window("lazyvim")

ws2 = Workspace(2)
ws2.open_window("firefox")

print(len(ws1))
print(ws1 == ws2)

ws2.open_window("obsidian")
print(ws1 == ws2)
