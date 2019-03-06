import uuid

def create_user(un, pw):
	try:
		f = open(f"{un}.user", "w")
		f.write(un + "\n")
		f.write(pw + "\n")
		user_id = str(uuid.uuid4())
		f.write(user_id)
		return True
	except Exception:
		return False

un = input("Username: ")
pw = input("Password: ")
status = create_user(un, pw)
if not status:
	print("User couldn't be created")
else:
	print("User created successfully!")
		
