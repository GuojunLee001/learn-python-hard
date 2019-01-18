# coding: utf-8

# 句子中每个单词分为单独词语
def break_words(stuff):
    """This function will break up words for us.""" 
    words = stuff.split(' ')
    return words

# 混乱排序
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
	
# 句子第一个单词,0,-1表示列表内容
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print word

# 句子最后一个单词
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print word

# 与第二个函数输出结果一样
def sort_sentense(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
	
# 打印分离的第一个和最后一个
def print_first_and_last(sentense):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)
	
# 打印第一个和最后一个
def print_first_and_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentense(sentence)
    print_first_word(words)
    print_last_word(words)