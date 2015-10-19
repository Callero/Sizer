# Small program to calculate useable capacity in a ScaleIO cluster
import math


print "To get the number of devices per node/server, type (1)"
print "To get the total useable storage, type (2)"
sel_funct = raw_input("Please choose:")

def calc_reserve(nodes): #this function calculates the recommended reserve
		if (1 / nodes) > 0.1: #Calculate recommended_reserve percent is over 10%
			reserve = 1 / nodes
		else: #Recommend minimum 10% reserve
			reserve = 0.1
		return recommended

if sel_funct == "1":
	desired_number_nodes = float(raw_input("How many nodes are desired?: ")) #input number of nodes desired
	recommended_reserve = calc_reserve(desired_number_nodes)
	print ""
	print "The recommended reserve is", recommended_reserve * 100, "%"
	print ""
	desired_useable_storage = float(raw_input("How much useable storage is required (TiB)?: ")) #input desired storage
	print ""	
	device_size = float(raw_input("Which block device size will be used (TB)?: ")) #input device size
	storage_with_reserve = desired_useable_storage * (1 + recommended_reserve) #calculate the amount of raw storage needed including reserve in TiB
	storage_with_reserve_overhead = storage_with_reserve * 2
	required_amount_of_devices_total = storage_with_reserve_overhead / (device_size) #calculate the required amount of devices
	required_amount_of_device_node = required_amount_of_devices_total / desired_number_nodes #calculate the required amount of devices per node/server
	print ""
	print "Raw storage with reserve", storage_with_reserve, "TiB"
	print ""
	print "Storage with reserve and copies", storage_with_reserve_overhead, "TiB"
	print ""
	print "To get", desired_useable_storage, "TiB (base 2)", "with the recommended reserve", recommended_reserve * 100, "%", "using", "devices", "at", device_size, "TB"
	print "you will need", math.ceil(required_amount_of_device_node), "devices per node/server"

elif sel_funct == "2":
	number_nodes = float(raw_input("How many nodes will be used?: ")) #input number of nodes to be used
	recommended_reserve = calc_reserve(number_nodes)
	print ""
	print "The recommended reserve is", recommended_reserve * 100, "%"
	print ""
	device_size = float(raw_input("Which block device size will be used (TB)?: ")) #input device size
	devices_per_node = raw_input("How many devices will be used per node/server?")
	raw_storage = devices_per_node * device_size * number_nodes
	storage_with_reserve
	print "With", number_nodes, "nodes/servers", "using", device_size, "TB devices and a reserve of", recommended_reserve, "%"
	print "You will get approximately", 