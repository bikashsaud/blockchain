blockchain = [1]

def add_value(val):
    blockchain.append([blockchain[0],val])
    print(blockchain)

add_value(12)
add_value(14)
add_value(19)
add_value(43)
