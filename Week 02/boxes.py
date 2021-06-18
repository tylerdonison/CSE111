items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

def neededBoxes (items, boxsize):
    neededBoxes = items // boxsize
    checker = items % boxsize
    if checker > 0 :
        neededBoxes += 1
    return neededBoxes

total_boxes = neededBoxes(items,items_per_box)

print(f"For {items} items, packing {items_per_box} items in each box, you will need {total_boxes} boxes.")