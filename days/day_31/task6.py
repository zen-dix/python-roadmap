def admin_required(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user_role") ==  "admin":
            del kwargs["user_role"]
            return func(*kwargs)
        else:
            return {'status': 403, 'error': 'Access Denied'}
    return wrapper
@admin_required
def get_database_record(db_id):
    return {"status": 200, "data": f"Secret info from db {db_id}"}

print(get_database_record(db_id=42, user_role='admin'))
print(get_database_record(db_id=42, user_role='guest'))
print(get_database_record(db_id=42))