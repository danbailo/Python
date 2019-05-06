<b>Time Complexity in Python</b> - https://bit.ly/2rlovyG<br />
<b>Data Structure in Python</b> - https://bit.ly/2QghIxN<br />

<b>With and Try..Except</b>
With is a context manager it's usually used to manage resource objects. Try/except catches exception in a block of code.<br>

with is a loop. It's got nothing to do with exceptions. If you want to check for exceptions, you can do

try:
    some requests code
except SomeError:
    tell user about an exception. 
Play around with invalid pages and find what kind of exceptions you get

Like ConnectionRefusedError

try:
    code
except ConnectionRefusedError:
    print('Your connection was refunded') <br>

For files it's usually a good idea to use a with loop.    

Depending on what you're doing, you might need to use both, neither or just one of them. Check the documentation for the function you're running.

