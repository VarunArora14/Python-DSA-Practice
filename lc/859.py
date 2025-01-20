def buddyStrings(f: str, s: str):
  if len(f) != len(s):
    return False

  # if lens are equal check if double like "aa" or "aabc" to swap
  if f == s and len(f) > len(set(f)):
    return True

  diff = []  # stores the different indices
  for i in range(len(f)):
    if f[i] != s[i]:
      diff.append(i)
    if len(diff) > 2:
      return False
  print(diff)
  if len(diff) == 2 and s[diff[0]] == f[diff[1]] and s[diff[1]] == f[diff[0]] :
    return True
  return False


print(buddyStrings("AB", "AB"))
