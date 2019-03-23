guest_list = ['Brendon Leonard','Fitz Cahall','Mark Manson']

print ("Would you like to come to dinner, " + guest_list[0] + "?")
print ("Would you like to come to dinner, " + guest_list[1] + "?")
print ("Would you like to come to dinner, " + guest_list[2] + "?")

print ("\n" + guest_list[2] + " can't make it :(")

busy_guest = 'Mark Manson'

guest_list.remove(busy_guest)

guest_list.append('Alex Honnold')

print ("\nWould you like to come to dinner, " + guest_list[0] + "?")
print ("Would you like to come to dinner, " + guest_list[1] + "?")
print ("Would you like to come to dinner, " + guest_list[2] + "?")

print ("\nI found a bigger table!!!")

guest_list.insert(0, "Tommy Caldwell")
guest_list.insert(2, "Scott Jurek")
guest_list.append("The Real Hiking Viking")

print ("\nWould you like to come to dinner, " + guest_list[0] + "?")
print ("Would you like to come to dinner, " + guest_list[1] + "?")
print ("Would you like to come to dinner, " + guest_list[2] + "?")
print ("Would you like to come to dinner, " + guest_list[3] + "?")
print ("Would you like to come to dinner, " + guest_list[4] + "?")
print ("Would you like to come to dinner, " + guest_list[5] + "?")

print ("\nMy bigger dinner table didn't arrive! :(")

uninvited_guest = guest_list.pop()
print ("\nSorry, " + uninvited_guest + ", my bigger table didn't arrive so you can't come to the party!")
uninvited_guest = guest_list.pop()
print ("Sorry, " + uninvited_guest + ", my bigger table didn't arrive so you can't come to the party!")
uninvited_guest = guest_list.pop()
print ("Sorry, " + uninvited_guest + ", my bigger table didn't arrive so you can't come to the party!")
uninvited_guest = guest_list.pop()
print ("Sorry, " + uninvited_guest + ", my bigger table didn't arrive so you can't come to the party!")

print ("\nWould you like to come to dinner, " + guest_list[0] + "?")
print ("Would you like to come to dinner, " + guest_list[1] + "?")

del guest_list[0]
del guest_list[0]

print (guest_list)
