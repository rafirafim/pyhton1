def print_menu():
	print('1. Km to Miles')
	print('2. Miles to Km')

def km_to_miles():
	km = float(input('Enter the distance in Km  :  '))
	miles=km/1.609
	print ('Distance in miles: {}'.format(miles))

def miles_to_km():
	miles = float(input('Enter the distance in miles  :  '))
	km = miles*1.609
	print ('Distance in km: {}'.format(km))

print_menu()
a=input('enter thr conversion type :')
if a == 1:
	km_to_miles()
if a == 2:
	miles_to_km()

