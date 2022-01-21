def online_count(status):
    count = 0
    for key in status:
        if status[key] == "online":
            count += 1
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))