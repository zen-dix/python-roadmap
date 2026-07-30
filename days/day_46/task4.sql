CREATE TABLE ServerLogs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    error_message TEXT,
    is_critical BLOB
)
