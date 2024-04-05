def filter_file(input_file, output_file, keyword):
    with open(input_file, 'r') as f_input:
        lines = f_input.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    with open(output_file, 'w') as f_output:
        f_output.writelines(filtered_lines)

def main():
    input_file_name = "input.txt"
    output_file_name = "filtered.txt"
    keyword = input("Введіть ключове слово для фільтрації: ")

    filter_file(input_file_name, output_file_name, keyword)
    print("Результати фільтрації збережено у файлі filtered.txt")

if __name__ == "__main__":
    main()