blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]
    

def add_value(transation_amount, last_transection=[1]):
    blockchain.append([last_transection, transation_amount])
    
def get_user_input():
    return float(input("your transection amount: "))

tr_amount = get_user_input()
add_value(tr_amount)
tr_amount = get_user_input()

add_value(tr_amount, get_last_blockchain_value())
tr_amount = get_user_input()

add_value(tr_amount, get_last_blockchain_value())
tr_amount = get_user_input()

add_value(tr_amount, get_last_blockchain_value())
print (blockchain)