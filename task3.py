import sys

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


def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parsed_line = parse_log_line(line)
            logs.append(parsed_line)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(
        filter(
            lambda log: log["level"] == level.upper(),
            logs
        )
    )


def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]

        if level not in counts:
            counts[level] = 0

        counts[level] += 1

    return counts


def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17}| {'Кількість'}")
    print(f"{'-' * 17}|{'-' * 10}")

    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python task3.py <log_file> [logging_level]")
        return

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)

        counts = count_logs_by_level(logs)

        display_log_counts(counts)

        if len(sys.argv) == 3:
            level = sys.argv[2].upper()

            if level not in counts:
                print(f"\nUnknown logging level: {level}")
                return

            filtered_logs = filter_logs_by_level(logs, level)

            print(f"\nДеталі логів для рівня '{level}':")

            for log in filtered_logs:
                print(
                    f"{log['date']} {log['time']} - {log['message']}"
                )

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    except PermissionError:
        print(f"Error: No permission to read '{file_path}'.")

    except ValueError as error:
        print(f"Error: {error}")

    except OSError as error:
        print(f"Error reading file: {error}")


if __name__ == "__main__":
    main()