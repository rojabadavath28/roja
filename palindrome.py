def palindrome(s):
  rev = "".join(reversed(s))#reverse the string and join it back
  return s==rev
#compare the original string with  the reversed string
#example usage:
print(palindrome("racecar")) #true
print(palindrome("hello")) #false




































