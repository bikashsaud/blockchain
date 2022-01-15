blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]
    

def add_value(transation_amount, last_transection):
    blockchain.append([last_transection, transation_amount])
    
    

add_value(12, [1])
add_value(0.1, get_last_blockchain_value())
add_value(19, get_last_blockchain_value())
add_value(43, get_last_blockchain_value())
print (blockchain)