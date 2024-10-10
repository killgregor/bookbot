def word_processor(file_path):
    with open(file_path) as f:
        return f.read().lower()

def char_counter(content):
    counter_dict = {}
    for character in content:
        if character not in counter_dict:
            counter_dict[character] = 1
        else:
            counter_dict[character] += 1
    return counter_dict 

def word_counter(content):
    return len(content.split())


def report_generator(word_count, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n")
    for item in sorted(char_dict, key=char_dict.get, reverse=True):
        if item.isalpha():
            print(f"The '{item}' character was found {char_dict[item]} times")

def main():
    file_content = word_processor("books/frankenstein.txt")
    word_cnt = word_counter(file_content)
    char_cnt = char_counter(file_content)
    report_generator(word_cnt, char_cnt)

main()