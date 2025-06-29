

def get_book_text(path):
    with open(path,encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    """计算文本中的单词数"""
    words = text.split()
    return len(words)

def count_chars(text):
    """统计每个字符出现次数"""
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def sort_char_counts(char_dict):
    """将字符计数字典转换为排序后的词典列表"""
    sorted_list = []
    for char, count in char_dict.items():
        if not char.isalpha():
            continue
        sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list