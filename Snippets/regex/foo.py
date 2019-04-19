import re

text = "Dummy python text"

print(re.sub("m", "-", text))

print(re.sub("m|t", "-", text))

print(re.sub("m|t|o", "-", text))

#Du--y python text
#Du--y py-hon -ex-
#Du--y py-h-n -ex-
