from newlines import *
import itemlist

def equipItem(player):
	realItem = ""
	finished = 0
	owo = 0
	
	player.printInv()
	newline()
	itemName = input("What is the item youd like to equip?\n")

	for item in player.inv:
		if item.name == itemName:
			owo = 1
	if owo != 1:
		bigboi()
		print("You don't have that item!")
		newline()
		return()

	for itemNum in range(len(itemlist.item_name_array) - 1):
		if finished == 1:
			do = "nothing"
		elif itemName == itemlist.item_array[itemNum].name:
			finished = 1
			realItem = itemlist.item_array[itemNum]

	if realItem.type == "Armor":
		tempHolder = player.equipped["armor"]
		if tempHolder != "":
			player.inv.append(tempHolder)
		player.equipped["armor"] = realItem
		bigboi()
		print("You equipped armor.")
		newline()
		return()
	elif realItem.type in itemlist.weapons:
		bigboi()
		player.printEquipped()
		newline()
		whichSlot = input("Which slot would you like to put this in? (Main or Side)\n")
		if whichSlot == "Main":
			tempHolder = player.equipped["main"]
			if tempHolder != "":
				player.inv.append(tempHolder)
			player.equipped["main"] = realItem
		elif whichSlot == "Side":
			tempHolder = player.equipped["side"]
			if tempHolder != "":
				player.inv.append(tempHolder)
			player.equipped["side"] = realItem
		else:
			bigboi()
			print("You didnt input Main or Side.")
			newline()
			return()
		bigboi()
		print("The item was equipped!")
		newline()
		return()
	else:
		bigboi()
		print("You can't equip a potion!")
		newline()
		return()
