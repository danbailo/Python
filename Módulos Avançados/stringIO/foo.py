import io

message = 'This is a normal string'

f = io.StringIO(message)

print(f.read())

#é tratado como um arquivo