sandwhich_orders = ['pastrami','rueben','chip butty','pastrami','triple cheese','pastrami']

while 'pastrami' in sandwhich_orders:
	sandwhich_orders.remove('pastrami')

finished_sandwhiches = []

while sandwhich_orders:
	current_sandwhich = sandwhich_orders.pop()

	print('The current sandwhich being made is: ' + current_sandwhich.title())

	finished_sandwhiches.append(current_sandwhich)

print("\nAll sandwhich orders are complete!\n")
print("The finished sandwhiches are:")


for sandwhich in finished_sandwhiches:
	print("- " + sandwhich.title())