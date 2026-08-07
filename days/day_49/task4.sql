/*
Задача 4 (Средняя, 10 мин)
Работа с тремя таблицами. Часто связи идут по цепочке.

    projects (id, project_name)

    repositories (id, project_id, repo_url)

    commits (id, repository_id, commit_hash, message)
    Напиши запрос, который выводит project_name, repo_url и commit_hash. Тебе потребуется использовать JOIN дважды в одном запросе.
*/
CREATE TABLE projects(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  project_name TEXT
);
CREATE TABLE repositories(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  project_id INTEGER,
  repo_url TEXT
);
CREATE TABLE commits(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  repository_id INTEGER,
  commit_hash TEXT,
  message TEXT
);

INSERT INTO projects (project_name)
VALUES
  ('Pomodoro'),
  ('Linux'),
  ('dotfiles');
INSERT INTO repositories (project_id, repo_url)
VALUES 
  (1, 'github.com/fjasdlf;a'),
  (2, 'gitlab.com/hhhohohoo'),
  (3, 'web.com/djfasj');
INSERT INTO commits (repository_id, commit_hash, message)
VALUES
  (1, 'fsdjaklfjo34738', 'Daily update'),
  (2, 'f328y4y8fijlk', 'Fix bug'),
  (3, '4ifsldkn38', 'Bebebe');
SELECT t1.project_name, t2.repo_url, t3.commit_hash
FROM projects t1
JOIN repositories t2 ON t1.id = t2.project_id
JOIN commits t3 ON t2.id = t3.repository_id;

