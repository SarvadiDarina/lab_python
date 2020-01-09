#4.	Довідник покупця. База торгівельних підприємств міста: назва, адреса та телефон,
# спеціалізація, час роботи. Організувати вибір магазину за довільним запитом.
# Дані зберігаються в масиві.
class Merchant:
	def __init__(self, name, address, phone, spec, worktime):
		self.name = name
		self.address = address
		self.phone = phone
		self.spec = spec
		self.worktime = worktime

	def __str__(self):
		return "{0} ({1}, {2}, {3}, {4})".format(self.name, self.address, self.phone, self.spec, self.worktime)

class MerchantDB:
	def __init__(self):
		self.merchants = []

	def load_from_file(self):
		with open("merchants.txt") as f:
			count = int(f.readline())

			for i in range(count):
				name = f.readline().rstrip()
				address = f.readline().rstrip()
				phone = f.readline().rstrip()
				spec = f.readline().rstrip()
				worktime = f.readline().rstrip()

				self.merchants.append(
					Merchant(name, address, phone, spec, worktime)
				)

	def finder(self, crit, search, item):
		if crit == "name":
			return search in item.name
		if crit == "phone":
			return search in item.phone
		if crit == "spec":
			return search in item.spec
		if crit == "address":
			return search in item.address
		if crit == "worktime":
			return search in item.worktime
		return False


	def find_merchants(self, crit, search):
		return list(filter(lambda x: self.finder(crit, search, x), self.merchants))

db = MerchantDB()
db.load_from_file()

crit = input("Search criteria (name, phone, address, spec, worktime): ")
s = input("Search: ")

for m in db.find_merchants(crit, s):
	print(m)