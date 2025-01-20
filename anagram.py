def is_anagram(str1:str, str2:str):
  return sorted(str1) == sorted(str2)

first:str = "yolo"
second:str = "looy"
print(is_anagram(first,second))