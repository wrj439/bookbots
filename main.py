import sys
from stats import get_book_text, count_words, count_chars, sort_char_counts

def main():
    # 命令行参数检查
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>\n")
        print("Example: python main.py books/frankenstein.txt")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    # 输出报表头部
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # 读取内容
    text = get_book_text(book_path)
    
    # 单词统计
    word_count = count_words(text)
    print("\n----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # 字符统计
    char_counts = count_chars(text)
    sorted_char_list = sort_char_counts(char_counts)
    
    # 字符频率报告
    print("\n--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    
    print("\n============= END ===============")

if __name__ == "__main__":
    main()
