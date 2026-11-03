# coke pride 50 cents, amount due initiially 50: and decreses as more amount is added. but will show the number left if the unaccepted denomination are added

def main():
    Amount = 50 
    print(f"Amount due: {Amount}")
    while Amount > 0:
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin == 25 or inserted_coin == 10 or inserted_coin == 5: 
            Amount = Amount - inserted_coin
            if Amount >= 0: 
                print(f"Amount due: {Amount}")
            else:
                print("Change Owed:", Amount*-1)
        else:
            print(f"Amount due: {Amount}")


main()                              