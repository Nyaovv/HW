CREATE TABLE IF NOT EXISTS diary (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_name TEXT NOT NULL,
  task_description TEXT NOT NULL DEFAULT '',
  task_ready TEXT DEFAULT 'undone',
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)