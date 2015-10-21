# Small program to calculate useable capacity in a cluster
import math
from math import *
from bitmath import *

sel_funct = ""

while sel_funct != "1" or sel_funct != "2":
    print "To get the number of devices per node/server, type (1)"
    print "To get the total useable storage, type (2)"
    sel_funct = raw_input("Please choose: ")
else:
    def calc_reserve(nodes):  # this function calculates the recommended reserve
        if (1 / nodes) > 0.1:  # Calculate recommended_reserve percent is over 10%
            reserve = 1 / nodes
        else:  # Recommend minimum 10% reserve
            reserve = 0.1
        return reserve


    if sel_funct == "1":

        # input number of nodes desired
        desired_number_nodes = int(raw_input("How many nodes are desired?: "))
        recommended_reserve = calc_reserve(desired_number_nodes)

        print ""

        print "The recommended reserve is", recommended_reserve * 100, "%"
        print ""

        desired_useable_storage = TiB(int(raw_input("How much useable storage is required (TiB)?: ")))
        print ""

        device_size = TB(int(raw_input("Which block device size will be used (TB)?: ")))  # input device size, TB
        device_size_tib = device_size.to_TiB()  # convert to TiB

        # calculate the amount of raw storage needed including reserve in TB
        storage_with_reserve = desired_useable_storage * (
            1 + recommended_reserve)
        storage_with_reserve_overhead = storage_with_reserve * 2
        required_amount_of_devices_total = storage_with_reserve_overhead / (
            device_size)  # calculate the required amount of devices

        # calculate the required amount of devices per node/server
        required_amount_of_device_node = required_amount_of_devices_total / desired_number_nodes
        recommended_reserve_pct = recommended_reserve * 100
        print ""
        print "Raw storage with reserve", storage_with_reserve, "TiB"
        print ""
        print "Storage with reserve and copies", storage_with_reserve_overhead, "TiB"
        print ""
        print "To get %i TiB with the recommended reserve %.1f pct using %i devices at %i TB" % (
            desired_useable_storage, recommended_reserve_pct, desired_number_nodes, device_size)
        print "you will need %i devices per node/server" % math.ceil(required_amount_of_device_node)

    elif sel_funct == "2":
        # input number of nodes to be used
        number_nodes = int(raw_input("How many nodes will be used?: "))

        # Calculate the reserve
        recommended_reserve = calc_reserve(number_nodes)
        print "The recommended reserve is %.2s %%" % (recommended_reserve * 100)

        # input the size of the devices in TB
        device_size = TB(int(raw_input("Which block device size will be used (TB)?: ")))  # input device size, TB
        device_size_tib = device_size.to_TiB()  # convert to TiB

        print "Marketing device size is %s and logical device size is %.1f" % (device_size, device_size_tib)

        # input the number of devices per node/server
        amount_of_devices_per_node = int(raw_input("How many nodes will be used?: "))
