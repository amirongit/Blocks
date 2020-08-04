from chainblock import Chain, Block


def difficulty_test(hash_):
    return hash_[:1] == 1 * '0'


my_block = Block('Genesis', '', difficulty_test)
print(my_block)
print('\nvalidating block ...', my_block.is_valid())
my_block.data = 'CHANGED!'
print('validating after data change ...', my_block.is_valid(), '\n')
my_chain = Chain(lambda hash_: hash_[:2] == '0' * 2)
my_chain.add_block('Another Block')
print(my_chain)
print('\nvalidating chain ...', my_chain.is_valid())
my_chain.chain[0].data = 'CHANGED!'
print('validating after data change ...', my_chain.is_valid())
