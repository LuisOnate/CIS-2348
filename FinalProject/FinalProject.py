# Luis Onate
# 1596900

# importing the csv module
import csv


# functions that return the 1st index of a list for sorting purposes
def sort_manufacturer(lis_manufacturer):
    return lis_manufacturer[0]


def sort_price(lis_price):
    return lis_price[0]


def sort_service_date(lis_service_date):
    return lis_service_date[0]


# function that return the 2nd index of a list for sorting purposes
def sort_inventory(inventory):
    return inventory[1]


# functions that return the 1st index of a list for sorting purposes
def sort_phone_type(p_type):
    return p_type[0]


def sort_desktop_type(d_type):
    return d_type[0]


def sort_ipad_type(i_type):
    return i_type[0]


def sort_laptop_type(l_type):
    return l_type[0]


def sort_tower_type(t_type):
    return t_type[0]


def sort_camera_type(c_type):
    return c_type[0]


def sort_tablet_type(tab_type):
    return tab_type[0]


def sort_speaker_type(s_type):
    return s_type[0]


# function that return the 5th index of a list for sorting purposes
def sort_past_service(pas_service):
    return pas_service[4]


# functions that return the 4th index of a list for sorting purposes
def sort_damaged_inventory(dam_inventory):
    return dam_inventory[3]


def sort_dis_price(dis):
    return dis[3]


# an emtpy list is created and an input csv file is opened
manufacturer = []
with open("ManufacturerList.csv") as manufacturer_list:
    for row in csv.reader(manufacturer_list):  # input file is read by row
        manufacturer.append(row)  # the rows are appended to the empty list
        manufacturer.sort(key=sort_manufacturer)  # the list is sorted using a function as the sorting key

# an emtpy list is created and an input csv file is opened
price = []
with open("PriceList.csv") as price_list:
    for row in csv.reader(price_list):  # input file is read by row
        price.append(row)  # the rows are appended to the empty list
        price.sort(key=sort_price)  # the list is sorted using a function as the sorting key

# an emtpy list is created and an input csv file is opened
service_date = []
with open("ServiceDatesList.csv") as service_date_list:
    for row in csv.reader(service_date_list):  # input file is read by row
        service_date.append(row)  # the rows are appended to the empty list
        service_date.sort(key=sort_service_date)  # the list is sorted using a function as the sorting key

# a copy of the manufacture is stored in the variable new_manufacturer_lis
new_manufacturer_lis = manufacturer
for i in range(len(new_manufacturer_lis)):
    new_manufacturer_lis[i].append(price[i][1])  # the price column in the price list is appended to the new list
    new_manufacturer_lis[i].append(service_date[i][1])  # the service date column in the service date
                                                        # list is appended to the new list

# the damaged column is placed before the price column and it should be at the end of each list
for i in range(len(new_manufacturer_lis)):
    pop = new_manufacturer_lis[i].pop(3)  # the damaged column is removed using the pop
                                            # method and assigned to the variable pop
    new_manufacturer_lis[i].append(pop)  # the popped column is appended to the end of each list accordingly

# a copy of the new_manufacturer_lis is made and assigned to inventory_list
inventory_list = new_manufacturer_lis
inventory_list.sort(key=sort_inventory)  # the inventory list is sorted using a function as the key
open_inventory = open("FullInventory.csv", 'w')  # the rows in the inventory list are written
                                                # into the FullInventroy.csv file
for i in range(len(inventory_list)):
    csv.writer(open_inventory).writerow(inventory_list[i])


# the lists of posible item types are created
phone = []
desktop = []
ipad = []
laptop = []
tower = []
tablet = []
camera = []
speaker = []
for i in range(len(inventory_list)):  # a for loop iterating through the inventory list checking the item types and
                                        # appending the entire row to the corresponding item type list
    if inventory_list[i][2] == "phone":
        phone.append(inventory_list[i])
    elif inventory_list[i][2] == "desktop":
        desktop.append(inventory_list[i])
    elif inventory_list[i][2] == "ipad":
        ipad.append(inventory_list[i])
    elif inventory_list[i][2] == "laptop":
        laptop.append(inventory_list[i])
    elif inventory_list[i][2] == "tower":
        tower.append(inventory_list[i])
    elif inventory_list[i][2] == "tablet":
        tablet.append(inventory_list[i])
    elif inventory_list[i][2] == "camera":
        camera.append(inventory_list[i])
    elif inventory_list[i][2] == "speaker":
        speaker.append(inventory_list[i])

# the phone list is sorted with a function as the sorting key
phone.sort(key=sort_phone_type)
type_phone = open("PhoneInventory.csv", 'w')  # the phone inventory csv file is opened to be written into
for i in range(len(phone)):  # for loop iterating through the phone type list and writing each row to the csv file
    csv.writer(type_phone).writerow(phone[i])

# the desktop list is sorted with a function as the sorting key
desktop.sort(key=sort_desktop_type)
type_desktop = open("DesktopInventory.csv", 'w')  # the desktop inventory csv file is opened to be written into
for i in range(len(desktop)):  # for loop iterating through the desktop type list and writing each row to the csv file
    csv.writer(type_desktop).writerow(desktop[i])

# the ipad list is sorted with a function as the sorting key
ipad.sort(key=sort_ipad_type)
type_ipad = open("iPadInventory.csv", 'w')  # the ipad inventory csv file is opened to be written into
for i in range(len(ipad)):  # for loop iterating through the ipad type list and writing each row to the csv file
    csv.writer(type_ipad).writerow(ipad[i])

# the laptop list is sorted with a function as the sorting key
laptop.sort(key=sort_laptop_type)
type_laptop = open("LaptopInventory.csv", 'w')  # the laptop inventory csv file is opened to be written into
for i in range(len(laptop)):  # for loop iterating through the laptop type list and writing each row to the csv file
    csv.writer(type_laptop).writerow(laptop[i])

# the tower list is sorted with a function as the sorting key
tower.sort(key=sort_tower_type)
type_tower = open("TowerInventory.csv", 'w')  # the tower inventory csv file is opened to be written into
for i in range(len(tower)):  # for loop iterating through the tower type list and writing each row to the csv file
    csv.writer(type_tower).writerow(tower[i])

# the tablet list is sorted with a function as the sorting key
tablet.sort(key=sort_tablet_type)
type_tablet = open("TabletInventory.csv", 'w')  # the tablet inventory csv file is opened to be written into
for i in range(len(tablet)):  # for loop iterating through the tablet type list and writing each row to the csv file
    csv.writer(type_tablet).writerow(tablet[i])

# the camera list is sorted with a function as the sorting key
camera.sort(key=sort_camera_type)
type_camera = open("CameraInventory.csv", 'w')  # the camera inventory csv file is opened to be written into
for i in range(len(camera)):  # for loop iterating through the camera type list and writing each row to the csv file
    csv.writer(type_camera).writerow(camera[i])

# the speaker list is sorted with a function as the sorting key
speaker.sort(key=sort_speaker_type)
type_speaker = open("SpeakerInventory.csv", 'w')  # the speaker inventory csv file is opened to be written into
for i in range(len(speaker)):  # for loop iterating through the speaker type list and writing each row to the csv file
    csv.writer(type_speaker).writerow(speaker[i])


# an empty list is created to append any past due items from the inventory list
past_service = []
for i in range(len(inventory_list)):
    if inventory_list[i][4] > "2/1/2021":
        past_service.append(inventory_list[i])

# the past service list is sorted using a function as the sorting key
past_service.sort(key=sort_past_service)
service = open("PastServiceDateInventory.csv", 'w')  # the past service date inventory csv
                                                    # file is opened in order to write into it
for i in range(len(past_service)):  # for loop iterating through each row of the past service list and writing it
    csv.writer(service).writerow(past_service[i])  # into the csv file


# an empty list is created to append any damaged items from the inventory list
damaged_inventory = []
for i in range(len(inventory_list)):
    if inventory_list[i][5] == "damaged":
        damaged_inventory.append(inventory_list[i])

# the damaged inventory list is sorted using a function as the sorting key
damaged_inventory.sort(key=sort_damaged_inventory, reverse=True)
damaged = open("DamagedInventory.csv", 'w')  # the damaged inventory csv file is opened in order to write into it
for i in range(len(damaged_inventory)):  # for loop iterating through each row of the damaged inventory list
    csv.writer(damaged).writerow(damaged_inventory[i])  # and writing it into the csv file


# empty list is created
manufacturer_item_type = []
user_input = input("Enter Manufacturer and item type: ").split()  # user input is requested and
                                                                # split into individual strings
manufacturer_item_type.append(user_input)  # the user input individual strings are appended to the list
man_and_typ = []  # new empty list is created

# while loop used for generating outputs to user until q is entered
while user_input != 'q':
    for i in range(len(manufacturer_item_type)):  # for loop that checks for q or manufacturer in
                                                # the manufacturer and item type list
        # if and elif statements used to append strings into a new list that will only contain one or two strings
        if "q" in manufacturer_item_type[i]:
            man_and_typ.append('q')
        elif "Apple" in manufacturer_item_type[i] or "apple" in manufacturer_item_type[i]:
            man_and_typ.append("Apple")
        elif "Dell" in manufacturer_item_type[i] or "dell" in manufacturer_item_type[i]:
            man_and_typ.append("Dell")
        elif "Lenovo" in manufacturer_item_type[i] or "lenovo" in manufacturer_item_type[i]:
            man_and_typ.append("Lenovo")
        elif "Samsung" in manufacturer_item_type[i] or "samsung" in manufacturer_item_type[i]:
            man_and_typ.append("Samsung")
        elif "Microsoft" in manufacturer_item_type[i] or "microsoft" in manufacturer_item_type[i]:
            man_and_typ.append("Microsoft")
        elif "HP" in manufacturer_item_type[i] or "hp" in manufacturer_item_type[i]:
            man_and_typ.append("HP")
        elif "Acer" in manufacturer_item_type[i] or "acer" in manufacturer_item_type[i]:
            man_and_typ.append("Acer")
        elif "Asus" in manufacturer_item_type[i] or "asus" in manufacturer_item_type[i]:
            man_and_typ.append("Asus")
        elif "Toshiba" in manufacturer_item_type[i] or "toshiba" in manufacturer_item_type[i]:
            man_and_typ.append("Toshiba")
        elif "Sony" in manufacturer_item_type[i] or "sony" in manufacturer_item_type[i]:
            man_and_typ.append("Sony")

    for i in range(len(manufacturer_item_type)):  # for loop that checks for item type in
                                                # the manufacturer and item type list

        # if and elif statements used to append strings into a new list that will only contain one or two strings
        if "Laptop" in manufacturer_item_type[i] or "laptop" in manufacturer_item_type[i]:
            man_and_typ.append("laptop")
        elif "Phone" in manufacturer_item_type[i] or "phone" in manufacturer_item_type[i]:
            man_and_typ.append("phone")
        elif "Tower" in manufacturer_item_type[i] or "tower" in manufacturer_item_type[i]:
            man_and_typ.append("tower")
        elif "Desktop" in manufacturer_item_type[i] or "desktop" in manufacturer_item_type[i]:
            man_and_typ.append("desktop")
        elif "iPad" in manufacturer_item_type[i] or "ipad" in manufacturer_item_type[i]:
            man_and_typ.append("iPad")
        elif "Tablet" in manufacturer_item_type[i] or "tablet" in manufacturer_item_type[i]:
            man_and_typ.append("tablet")
        elif "Camera" in manufacturer_item_type[i] or "camera" in manufacturer_item_type[i]:
            man_and_typ.append("camera")
        elif "Speaker" in manufacturer_item_type[i] or "speaker" in manufacturer_item_type[i]:
            man_and_typ.append("speaker")

    # three empty lists are created
    display = []
    dis = []
    recommend = []
    for i in range(len(inventory_list)):  # for loop iterating through the rows in the inventory list
        # if else staments comparing index 1 and index 2 of the man_and_type list to index 2
        # and index 3 of each row in the inventory list
        if man_and_typ[0] == inventory_list[i][1] and man_and_typ[1] == inventory_list[i][2]:  # if both match
            display.append(inventory_list[i])  # the row is appened to the display list
            display.sort(key=sort_dis_price, reverse=True)  # the display list is sorted in
                                                            # reverse order using a function as the sorting key
            dis = display[0]  # only the first row is taken and stored in the dis list
        if man_and_typ[1] == inventory_list[i][2]:  # if statment used for appending inventory of
                                                    # the same type to the recommend list
            recommend.append(inventory_list[i])

    # empty list is created
    no_inventory = []
    for i in range(len(inventory_list)):  # for loop iterating through the rows in the inventory list
        # while loop verifying that strings in the man_and_type list dont match the strings in the inventory list
        while man_and_typ[0] not in inventory_list[i] or man_and_typ[1] not in inventory_list[i]:
            no_inventory = man_and_typ
            break

    # if index 1 in the man_and_type list is in the dis list the while loop runs
    while man_and_typ[0] in dis:
        if man_and_typ[0] == dis[1] and man_and_typ[1] == dis[2]:  # if index 1 and 2 of the man_and_type list
                                                        # match index 2 and 3 of the dis list an output is displayed
            print("Your item is: {} {} {} {}".format((dis[0]), dis[1], dis[2], dis[3]))
            break

    # index 2 of the recommend list is assigned to the item variable
    item = recommend[1]
    while man_and_typ[1] in item:  # if the string in index 2 of the man_and_type list are in the item list,
        # the while loop runs and an output is displayed to user
        print("You may, also, consider: {} {} {} {}\n".format(item[0], item[1],
                                                            item[2], item[3], ))
        break

    # if index 1 in the man_and_type list is in the no inventory list the while loop runs
    while man_and_typ[0] in no_inventory:
        # if index 1 and 2 in the man_and_type list match the strings in the no inventory list,
        # an output is displayed to user
        if man_and_typ[0] == no_inventory[0] and man_and_typ[1] == no_inventory[1]:
            print("No such item in inventory\n")
            break

    # if the user enters q, the program terminates
    if man_and_typ[0] == 'q':
        break

    # empty list is created
    manufacturer_item_type = []
    user_input = input("Enter Manufacturer and item type or q to quit: ").split()   # user input is requested and
                                        # split into individual strings and if q wasn't entered, the loop starts again
    manufacturer_item_type.append(user_input)  # the user input individual strings are appended to the list
    man_and_typ = []  # new empty list is created
