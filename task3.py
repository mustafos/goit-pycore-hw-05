
def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)

    if len(parts) != 4:
        raise ValueError("Invalid log line format")

    date, time, level, message = parts

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }

line = "2024-01-22 08:30:01 INFO User logged in successfully."

parsed_line = parse_log_line(line)

print(parsed_line)

def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parsed_line = parse_log_line(line.strip())
            logs.append(parsed_line)

    return logs

logs = load_logs("log.txt")

for log in logs:
    print(log)

def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]

        if level not in counts:
            counts[level] = 0

        counts[level] += 1

    return counts

logs = load_logs("log.txt")

counts = count_logs_by_level(logs)

print(counts)

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<20} | Кількість")
    print("-" * 35)

    for level, count in counts.items():
        print(f"{level:<20} | {count}")

logs = load_logs("log.txt")
counts = count_logs_by_level(logs)

display_log_counts(counts)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(
        filter(
            lambda log: log["level"] == level.upper(),
            logs
        )
    )

logs = load_logs("log.txt")

error_logs = filter_logs_by_level(logs, "error")

for log in error_logs:
    print(
        f"{log['date']} {log['time']} - {log['message']}"
    )