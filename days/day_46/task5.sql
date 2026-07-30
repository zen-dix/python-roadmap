CREATE TABLE employee_records (
  log_id INTEGER PRIMARY KEY,
  department TEXT NOT NULL, 
  salary REAL NOT NULL,
  has_access_card INTEGER,
  metadata TEXT NOT NULL
);
