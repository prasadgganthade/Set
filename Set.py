s1 = {1,2,3}
print(s1)
s2 = {2,3,4,5}
print(s2)
name = s1.union(s2)
print(name)
print(s1 - s2)
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
# frozenset
f = frozenset({10,20,30})
print(f)
print(dir(f))
d = 'Prasad Ganthade'
# reverse the string
print(d[::-1])
# without slicing
print(reversed(d))
print(list(reversed(d)))
print(''.join(list(reversed(d))))
# for above case reverse the words
new = d.split()
print(new[::-1])
print(' '.join(new[::-1]))
# create a dict
t = (10,20,30)
print(t)
print(type(t))
# now from tuple to dict
print({}.fromkeys(t))
print(dict.fromkeys(t))
t2 = (100,200,300)
# create dict of t and t2
t3 = dict(zip(t,t2))
print(t3)
print(len(d))
print(len(t))
print(sum(t2))
# min : find minimum value from sequence
print(min(t2))
# max : find maximum value froma sequence
print(max(t2))
# round = rounding the floting number
f = 12.56861463
print(round(f,2)) # rounding upto 2 places
# eval : evaling a mathematical expressions
name = eval('10+20+30')
print(name)
print(type(name))
# enumarate : it gives value + index
h = [1,2,3,4,5,6]
print(list(enumerate(h)))
# each tuple gives index and value
e = ['sham','ram','govind','krishana','madhusdan']
print(list(enumerate(e)))
print(t3)
t3[2] = 250
print(t3)
t3[20] = 400
print(t3)
# exercise
# Find the size of a Set in Python
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

import sys
print('Size of set1',Set1.__sizeof__(),'bytes')
print('Size of set2',Set2.__sizeof__(),'bytes')
print('Size of set3',Set3.__sizeof__(),'bytes')
# Iterate over a set in Python
test_set = set('geEks')
for i in test_set:
    print(i)

for i, val in enumerate(test_set):
    print(i, val)
#2. Python | Maximum and Minimum in a Set
sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
def MAX(sets):
    return max(sets)
print(MAX(sets))
def MIN(sets):
    return min(sets)
print('Minimum value is',MIN(sets))
# 3. Python | Remove items from Set
initial_set = set([12, 10, 13, 15, 8, 9])
def Remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)
Remove(initial_set)
# 4. Python | Check if two lists have at-least one element common
def comman_data(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(comman_data(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(comman_data(a, b))
# method 2 - using set member
def common_member(a,b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))
# 5. Python program to find common elements in three lists using sets
arr1 = [1, 5, 10, 20, 40, 80, 100]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

def intersecofsets(arr1,arr2,arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)

    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)
    print(final_list)

intersecofsets(arr1,arr2,arr3)

# 6. Python | Find missing and additional values in two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
print('Missing value in first list',set(list2).difference(list1))
print('Additional value in first list',set(list1).difference(list2))
print('Missing value in second list',set(list1).difference(list2))
print('Additional value in second list',set(list2).difference(list1))
# 7. Python Set difference to find lost element from a duplicated array
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]
def lost_element(a,b):
    a = set(A)
    b = set(B)

    if len(a) > len(b):
        print(list(a-b))
    else:
        print(list(b-a))

if __name__ == '__main__':
    lost_element(A,B)

# 8. Python program to count number of vowels using sets in given string
def vowel_counter(str1):
    count = 0
    vowel = "aeiouAEIOU"
    for alphabet in str1:
        if alphabet in vowel:
            count = count + 1
    print('Number of vowels is',count)
str1 = "GeeksforGeeks"
vowel_counter(str1)

# 9. Concatenated string with uncommon characters in Python
def uncommon_concat(str1,str2):
    set1 = set(str1)
    set2 = set(str2)
    uncommon = list(set1 ^ set2)
    print(" ".join(uncommon))
str1 = 'aacdb'
str2 = 'gafd'
if __name__ == "__main__":
    uncommon_concat(str1,str2)

# 10. Python | Program to accept the strings which contains all vowels
def check(string):
    if len(set(string.lower()).intersection('aeiou')) >= 5:
        return 'Accepted'
    else:
        return 'Not accepted'

if __name__ == "__main__":
    string = "geeksforgeeks"
    string1 = "SEEquoiaL"
    print(check(string))
    print(check(string1))

# 10. Python | Check if a given string is binary string or not
def check_binary(string):
    p = set(string)
    s = {'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        return 'Yes'
    else:
        return 'No'
string = '0101011110001'
string1 = '0101200'
string2 = '01010jk'
print(check_binary(string))
print(check_binary(string1))
print(check_binary(string2))
# 11. Python set to check if string is pangram
# method 1 using asci
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
string ="The quick brown fox jumps over the lazy dog"
if check(string) == True:
    print('The string is panagram')
else:
    print('The string is not panagram')
# method 2
str1 = string.replace(" ",'')
str1 = str1.lower()
x = list(set(str1))
x.sort()
x ="".join(x)
alphabets="abcdefghijklmnopqrstuvwxyz"
if x == alphabets:
    print('the string is panagram')
else:
    print("the string is not panagram")

# 12. Python Set | Pairs of complete strings in two sets
#13 heretogram
def heterogram(input):
    alphabets = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(alphabets)) == len(alphabets):
        print('Yes')
    else:
        print('No')
if __name__ == "__main__":
    input = 'the big dwarf only jumps'
    s = "geeksforgeeks"
    heterogram(input)
    heterogram(s)








