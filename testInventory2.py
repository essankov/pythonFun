def getItem(ID):
    counter = 0
    found = False
    userID = input("Enter the ID: ")
    while counter < len(ID) and not found:
        if userID == ID[counter]:
            found = True
        else:
            counter += 1
    if found:
        return counter
    else:
        return -1

def findQty(ID, qty):
    for counter in range(0, len(qty)):
        if qty[counter] < 25:
            print(ID[counter], qty[counter])

def totalRetail(qty, price):
    retTotal = 0
    for counter in range(0, len(qty)):
        total = qty[counter] * (1.2 * price[counter])
        retTotal += total
    print("Total reatail inventory: ", retTotal)
    
def main():
    invFile = open("inventory.txt", "r")
    invID = []
    description = []
    quantity = []
    price = []
    for line in invFile:
        data = line.split(",")
        invID.append(data[0])
        description.append(data[1])
        quantity.append(int(data[2]))
        price.append(float(data[3]))
    loc = getItem(invID)
    if loc == -1:
        print("error")
    else:
        print(invID[loc], description[loc], quantity[loc],
              price[loc])
    print("Quantities less than 25")
    findQty(invID, quantity)
    totalRetail(quantity, price)
    
main()
