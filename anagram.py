# program to check for anagrams
str1=input("enter string1 :");
str2=input("enter string2 :");
if(sorted(str1.lower())==sorted(str2.lower())):
 print("given string are anagrams");
else:
 print("given strings are not anagrams");
