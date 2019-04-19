import colorama
from colorama import Fore, Style

print("-"*45)
z = input("Enter something: ")[:15]
x = len(z)
print(Style.BRIGHT+Fore.RED)
print("{:-^15}{:-^15}{:-^15}".format("First","Second","Third"))
print(Fore.RESET)

for i in range(x):
    n = z[i]
    s = z[i:]
    j = i+1
    d = z[x-j:]
    print(Fore.GREEN+"{:-^15}{:-^15}{:-^15}".format(s,n,d))
print(Fore.RESET+"-"*45)