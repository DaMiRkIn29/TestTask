def longest_increasing_streak(nums: list[int]) -> dict:
    n = len(nums)
    if n < 2:
        return {"length": 0, "streak": []}

    cur_start = 0
    cur_len   = 1

    best_start = 0
    best_len   = 0

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            cur_len += 1
        else:
            if cur_len > best_len:
                best_len   = cur_len
                best_start = cur_start

            cur_start = i
            cur_len   = 1

    if cur_len > best_len:
        best_len   = cur_len
        best_start = cur_start

    if best_len < 2:
        return {"length": 0, "streak": []}

    return {
        "length": best_len,
        "streak": nums[best_start: best_start + best_len]
    }

# Тут попросил ИИ сделать несколько тест кейсов
if __name__ == "__main__":
    examples = [
        [],
        [42],
        [5, 5, 5, 5],
        [9, 8, 7, 6],
        [1, 2, 3, 4, 5],
        [1, 3, 2, 5, 8, 4, 7],
        [1, 2, 4, 1, 2, 3],
        [5, 1, 2, 3, 4],
        [-3, -2, -1, 0, 5]
    ]

    for idx, arr in enumerate(examples, 1):
        rez = longest_increasing_streak(arr)
        print(f"Пример #{idx}:  вход = {arr}")
        print(f"            → длина = {rez['length']}, серия = {rez['streak']}\n")
