CREATE TABLE workspaces(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  os_type TEXT, 
  window_manager TEXT
);
CREATE TABLE employees(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  workspace_id INTEGER,
  username TEXT
);

INSERT INTO workspaces (os_type, window_manager)
VALUES
  ('CachyOS', 'dwm'),
  ('Arch', 'hyprland'),
  ('Debian', 'SwayFX'),
  ('CachyOS', 'bspwm');

INSERT INTO employees (workspace_id, username)
VALUES
  (1, 'f;dsdf;'),
  (2, 'bbaabf'),
  (3, 'oofsfs'),
  (4, 'sjalas');
SELECT  employees.username, workspaces.window_manager
FROM workspaces
INNER JOIN employees ON workspaces.id = employees.workspace_id
WHERE workspaces.os_type = 'CachyOS'
ORDER BY employees.username ASC;

