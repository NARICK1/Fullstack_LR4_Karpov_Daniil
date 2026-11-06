import os


def create_test_file_KDO():
    if not os.path.exists("1_KDO.dat"):
        data = bytes([10, 20, 30, 40, 50, 60, 70, 80])
        with open("1_KDO.dat", "wb") as output_file:
            output_file.write(data)


def reverse_KDO():
    try:
        with open("1_KDO.dat", "rb") as input_file:
            data = input_file.read()

        reversed_data = data[::-1]

        with open("2_KDO.dat", "wb") as output_file:
            output_file.write(reversed_data)

        with open("1_KDO.dat", "rb") as input_file:
            original_content = input_file.read()

        with open("2_KDO.dat", "rb") as output_file:
            reversed_content = output_file.read()

        print("Содержимое 1_KDO.dat:", list(original_content))
        print("Содержимое 2_KDO.dat:", list(reversed_content))

    except FileNotFoundError:
        print("Файл 1_KDO.dat не найден")
    except OSError as error:
        print("Ошибка при работе с файлом:", error)


if __name__ == "__main__":
    create_test_file_KDO()
    reverse_KDO()
