<b>Documentation</b> - https://docs.python.org/3/tutorial/index.html<br/>
<b>Time Complexity in Python</b> - https://bit.ly/2rlovyG<br />
<b>Data Structure in Python</b> - https://bit.ly/2QghIxN<br />

<b>With and Try..Except</b><br>
With is a context manager it's usually used to manage resource objects. Try/except catches exception in a block of code.<br>

with is a loop. It's got nothing to do with exceptions. If you want to check for exceptions, you can do

try:<br/>
&nbsp; &nbsp; some requests code<br/>
except SomeError:<br/>
&nbsp; &nbsp; tell user about an exception.<br/>


Play around with invalid pages and find what kind of exceptions you get<br>

Like ConnectionRefusedError<br>

try:<br/>
&nbsp; &nbsp; code<br/>
except ConnectionRefusedError:<br/>
&nbsp; &nbsp; print('Your connection was refunded')<br/>

For files it's usually a good idea to use a with loop.<br> 

Depending on what you're doing, you might need to use both, neither or just one of them. Check the documentation for the function you're running. <br>

<b>'r' before string</b><br>

When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without change, and all backslashes are left in the string. For example, the string literal r"\n" consists of two characters: a backslash and a lowercase 'n'. String quotes can be escaped with a backslash, but the backslash remains in the string; for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote; r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw string cannot end in a single backslash (since the backslash would escape the following quote character). Note also that a single backslash followed by a newline is interpreted as those two characters as part of the string, not as a line continuation.

O 'r' indica uma raw string, é uma string pura, o que você escrever será tratado como caractere normal. O '\' que é um caractere de escape será impresso em uma raw string da mesma forma que qualquer outro caractere.