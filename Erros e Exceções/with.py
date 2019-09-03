class Test:
	def __init__(self,n):
		self.n=n
	def __enter__(self):
		return self.n
	def __exit__(self, exc_type, exc_val, exc_tb):
		print("\t",exc_type, exc_val, exc_tb)
		print(f"\tclose {self.n}")

print("caso 1 sem erro")
with Test(2) as i:
	i+=2
print("caso 2 exception dentro with")
try:
	with Test(2) as i:
		raise Exception("erro")
		i+=2
except Exception:
	pass
