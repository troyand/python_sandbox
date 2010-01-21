'''
this doesn't reflect native vlans, or q-in-q vlans
encapsulation on parent physical interface equals to 1
'''
for i in R1.cviRoutedVlanIfIndex:
    vlan_id, parent_if_index = i
    child_if_index = R1.cviRoutedVlanIfIndex[i]
    print R1.ifDescr[parent_if_index], R1.ifDescr[child_if_index], vlan_id

