def isValid(s:str):
  
  stack = []
  for char in s:
  if char=='(' or char == '{' or char == '[':
    stack.append(char)
  else:
    if len(stack)==0:
    return "False1" # as  char left but a closing tag found
    if char == '}' and stack[-1]=='{':
    stack.pop()
    elif char == ')' and stack[-1]=='(':
    stack.pop()
    elif char==']' and stack[-1]=='[':
    stack.pop()
    else:
    print(f"char: {char} and stack: {stack}")
    return "False2" # unwanted input
    
  print(stack)
  return len(stack)==0

print(isValid("()"))