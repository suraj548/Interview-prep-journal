import math

#1
def rev(str_value):  # str_valueing slicing returns new str_valueing
    return str_value[::-1]

#2
def rev_words_in_sentence(str_value: str):
    words = str_value.split()
    rev_words_list = [word[::-1] for word in words]
    rev_words_in_sentence = ' '.join(rev_words_list)
    return  rev_words_in_sentence

#3
def rev_sentence(str_value: str):
    words = str_value.split()
    rev_list = []
    for i in reversed(words):
        if i == " ":
            continue
        else:
            rev_list.append(i)
    rev_sentence = ' '.join(rev_list)
    return rev_sentence

#4
def count_chars_in_word(str_value):
    char_dict = {}
    char_str_list = []
    for i in str_value:
        char_dict.setdefault(i, 0)
    
    for j in str_value:
        char_dict[j] += 1
        
    for key, value in char_dict.items():
        char_str_list.append(key)
        char_str_list.append(value)
        
    str_value_list = [str(c) for c in char_str_list]
    return ''.join(str_value_list)

#5
def count_highest_char(str_value):
    char_dict = {}
    m = 0
    n = ""

    for i in str_value:
        char_dict.setdefault(i, 0)
    
    for j in str_value:
        char_dict[j] += 1
        if char_dict[j] > m:
            m = char_dict[j]
            n = j

    return n, m

#6
def find_missing_numbers(arr_list):
    arr_list_set = set(arr_list) 
    missing_list = []
    for i in range(0, max(arr_list)):
        if i not in arr_list_set:
            missing_list.append(i)
    return missing_list

#7
def simple_swap(a, b):
    a, b = b, a
    return a, b

#8
def temp_swap(a, b):
    temp = a
    a = b
    b = temp    
    # a = a+b #5
    # b = a-b #5-3
    # a = a-temp
    return a, b

#9
def palindrome(str):
    if len(str) == 1:
        return True
    else:
        if str == str[::-1]:
            return True
        else:
            return False

#10
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

#11
def fib(limit):
    a, b = 0, 1
    fib_list = []
    while a < limit:
        fib_list.append(a)
        a, b = b, a+b
    return fib_list

#12
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    
#13
def print_prime(n):
    prime_list = []
    for i in range(n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

#14
def remove_dupicate_words(str_value: str):
    str_list = str_value.split()
    str_list_set = set(str_list)
    return ' '.join(sorted(str_list_set, key=str_list.index))

#15
def reverse_num(num: int):
    reversed = 0
    while num > 0:
        remainder = int(num%10)
        reversed = reversed*10 + remainder
        num = int(num/10)
    return reversed

#16 
def max_word_count(str_value: str):
    str_list = str_value.split()
    str_dict = {}
    for i in set(str_list):
        str_dict.setdefault(i, 0)
    for j in str_list:
        str_dict[j] = str_dict[j]+1
    sorted_list = sorted(str_dict.values(), reverse=True)
    if len(sorted_list) > 1:
        return sorted_list[1]
    else:
        return sorted_list[0]

#17
# def merge(list1, list2):

def check_anagram(word1: str, word2: str):
    if len(word1) != len(word2):
        return False
    list1 = sorted(list(word1))
    list2 = sorted(list(word2))
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
    
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)

print(rev_words_in_sentence("mohan"))
print(rev_sentence("sky is blue"))
print(count_chars_in_word("total"))
print(count_highest_char("Total"))
print(find_missing_numbers([1,2,4,6,3,9]))
print(simple_swap(2,3))
print(temp_swap(2,3))
print(palindrome("RADAR"))
print(fact(5))
print(fib(5))
print(is_prime(27))
print(print_prime(-3))
print(remove_dupicate_words("mohan said mohan is good boy and mohan bad boy"))
print(reverse_num(21))
print(max_word_count("mohan said mohan is good boy and mohan bad boy"))
z = 3,12,14,56,1,89,2
print(merge_sort(z))
print(check_anagram("mohan", "nahom"))
