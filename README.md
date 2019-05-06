<b>Time Complexity in Python</b> - https://bit.ly/2rlovyG<br />
<b>Data Structure in Python</b> - https://bit.ly/2QghIxN<br />

<b>With and Try..Except</b><br>
With is a context manager it's usually used to manage resource objects. Try/except catches exception in a block of code.<br>

with is a loop. It's got nothing to do with exceptions. If you want to check for exceptions, you can do

<code>
try:<br>
    some requests code<br>
except SomeError:<br>
    tell user about an exception.<br>
</code>

Play around with invalid pages and find what kind of exceptions you get<br>

Like ConnectionRefusedError<br>
<br>

<code>
try:<br>
    code<br>
except ConnectionRefusedError:<br>
    print('Your connection was refunded')<br>
</code>

For files it's usually a good idea to use a with loop.<br> 

Depending on what you're doing, you might need to use both, neither or just one of them. Check the documentation for the function you're running. <br>

<b>'r' before string</b><br>

When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without change, and all backslashes are left in the string. For example, the string literal r"\n" consists of two characters: a backslash and a lowercase 'n'. String quotes can be escaped with a backslash, but the backslash remains in the string; for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote; r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw string cannot end in a single backslash (since the backslash would escape the following quote character). Note also that a single backslash followed by a newline is interpreted as those two characters as part of the string, not as a line continuation.