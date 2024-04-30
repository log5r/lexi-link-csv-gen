import os
import re
import csv
import toml
import sys


def read_toml_files(directory) -> dict[str, dict[str, str]]:
    results: dict[str, dict] = dict()
    pattern = re.compile(r'^\d+\.toml$')

    for filename in os.listdir(directory):
        if pattern.match(filename):
            filepath = os.path.join(directory, filename)
            nonextname = os.path.splitext(filename)[0]
            with open(filepath, 'r', encoding='utf-8') as file:
                results[nonextname] = toml.load(file)

    return results


def create_convertable_combination(cards: dict[str, dict[str, str]], proc_lang_list: list[str]) -> list[list[str]]:
    convertable_contents = []
    for _, texts in cards.items():
        for lang_front in proc_lang_list:
            for lang_back in proc_lang_list:
                buf = []
                if lang_front == lang_back:
                    continue
                buf.append(f"[{lang_front.split('-')[1]} > {lang_back.split('-')[1]}]: {texts[lang_front]}")
                buf.append(texts[lang_back])
                comment_section = []
                for lang_other in proc_lang_list:
                    if lang_other == lang_front or lang_other == lang_back:
                        continue
                    comment_section.append(texts[lang_other])
                buf.append(" / ".join(comment_section))
                buf.append(lang_front)
                buf.append(lang_back)

                convertable_contents.append(buf)
    return convertable_contents


def write_to_csv(data, file_path):
    # CSVファイルを開き、データを書き込む
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def output_convertable_wordholic_cards_csv(input_dir, output_path):
    lang_list = ["ja-JP", "en-US", "fr-FR", "zh-CN", "ko-KR"]
    ccr = create_convertable_combination(read_toml_files(input_dir), lang_list)
    write_to_csv(ccr, output_path)


def main():
    if len(sys.argv) != 3:
        print(f"Please provide 2 paths! (You specified {sys.argv})\nHow to use: main.py <path_to_toml_dir> <path_to_csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    out_path = sys.argv[2]
    try:
        output_convertable_wordholic_cards_csv(file_path, out_path)
    except Exception as e:
        print(f"ファイルの読み込みに失敗しました: {e}")


if __name__ == '__main__':
    main()
