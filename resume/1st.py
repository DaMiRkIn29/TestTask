def process_grades(records: list[str]) -> dict:
    valid_count = 0
    total_sum = 0
    passed_set = set()
    skipped = 0

    for record in records:
        parts = record.split(':', 1)
        surname, grade_str = parts[0].strip(), parts[1].strip()

        if not surname or ':' not in record:
            skipped += 1
            continue
        try:
            grade = int(grade_str)

            if 0 <= grade <= 100:
                valid_count += 1
                total_sum += grade

                if grade >= 60:
                    passed_set.add(surname)
            else:
                skipped += 1
        except ValueError:
            skipped += 1
    if valid_count == 0:
        average = 0.0
    else:
        average = round(total_sum / valid_count, 1)

    return {
        "valid_count": valid_count,
        "average": average,
        "passed": sorted(list(passed_set)),
        "skipped": skipped
    }

data = [
    "Иванов: 85",
    "Петров: 42",
    "Сидоров: abc", # битая
    "Козлов: 90",
    ": 55", # битая
    "Иванов: 70" # повтор (считаем как отдельную запись)
]

print(process_grades(data))