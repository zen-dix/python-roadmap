def server_log(level, prefix, *messages):
    ans = f"[{level}] <{prefix}>: "
    for message in messages:
        ans+= message+" "
    return ans
print(server_log("ERROR", "DB_CONN", "Connection refused.", "Retrying in 5 seconds..."))