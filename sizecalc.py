# Small program to calculate useable capacity in a cluster
import bitmath
import math
from math import *
from bitmath import *

print "To get the number of devices per node/server, type (1)"
print "To get the total useable storage, type (2)"
sel_funct = raw_input("Please choose: ")
print ""


def calc_reserve(nodes):  # this function calculates the recommended reserve
    if (1 / nodes) > 0.1:  # Calculate recommended_reserve percent is over 10%
        reserve = 1 / nodes
    else:  # Recommend minimum 10% reserve
        reserve = 0.1
    return reserve


if sel_funct == "1":
    desired_number_nodes = float(raw_input("How many nodes are desired?: "))  # input number of nodes desired
    recommended_reserve = calc_reserve(desired_number_nodes)
    print ""
    print "The recommended reserve is", recommended_reserve * 100, "%"
    print ""
    desired_useable_storage = TiB(
        float(raw_input("How much useable storage is required (TiB)?: ")))  # input desired storage
    print ""
    device_size = TB(float(raw_input("Which block device size will be used (TB)?: ")))  # input device size, TB
    device_size_tib = device_size.to_TiB()  # convert to TiB
    storage_with_reserve = desired_useable_storage * (
    1 + recommended_reserve)  # calculate the amount of raw storage needed including reserve in TB
    storage_with_reserve_overhead = storage_with_reserve * 2
    required_amount_of_devices_total = storage_with_reserve_overhead / (
    device_size)  # calculate the required amount of devices
    required_amount_of_device_node = required_amount_of_devices_total / desired_number_nodes  # calculate the required amount of devices per node/server
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
    number_nodes = float(raw_input("How many nodes will be used?: "))  # input number of nodes to be used
    recommended_reserve = calc_reserve(number_nodes)
    print ""
    print "The recommended reserve is", recommended_reserve * 100, "%"
    print ""
    device_size = TB(float(raw_input("Which block device size will be used (TB)?: ")))  # input device size, TB
    device_size_tib = device_size.to_TiB()  # convert to TiB
    print ""
    devices_per_node = raw_input(
        "How many devices will be used per node/server?: ")  # input number of devices per node/server
    raw_storage = int(devices_per_node) * int(device_size_tib) * int(number_nodes)  # calculate the raw storage
    storage_with_reserve = int(raw_storage) / int(
        (recommended_reserve + 1))  # calculate the raw storage with reserve deducted
    storage_with_reserve_overhead = storage_with_reserve / 2
    recommended_reserve_pct = recommended_reserve * 100
    print "With %i nodes/servers using %i GiB devices and a reserve of %.1f pct" % (
    number_nodes, device_size_tib, recommended_reserve_pct)
    print "You will get approximately %i TiB" % (round(storage_with_reserve_overhead, 2))
