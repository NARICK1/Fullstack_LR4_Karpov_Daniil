import re


def process_file_KDO():
    try:
        with open("first_KDO.txt", "r", encoding="utf-8") as input_file:
            lines = input_file.readlines()
    except FileNotFoundError:
        print("Файл first_KDO.txt не найден")
        return

    result_lines = []

    for start in range(0, len(lines), 4):
        group = lines[start:start + 4]
        counts = {}
        last_positions = {}

        for line_number, line in enumerate(group):
            words = re.findall(r"[^\W\d_]+", line.lower(), flags=re.UNICODE)

            for word in dict.fromkeys(words):
                counts[word] = counts.get(word, 0) + 1
                last_positions[word] = (line_number, words.index(word))

        common_words = [word for word in counts if counts[word] >= 2]
        common_words.sort(key=lambda word: last_positions[word])
        result_lines.append(" ".join(common_words))

    with open("second.txt", "w", encoding="utf-8") as output_file:
        if result_lines:
            output_file.write("\n".join(result_lines) + "\n")

    print("Обработка завершена. Результат сохранён в second.txt")

if __name__ == "__main__":
    process_file_KDO()
