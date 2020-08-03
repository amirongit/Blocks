from chainblock import Chain, Block


def difficulty_test(hash_):
    return hash_[:2] == 2 * '0'


my_block = Block('Genesis', '', difficulty_test)
print(my_block, '\n')
print('Testing the block validation: ', my_block.is_valid(difficulty_test, ''))
print()
my_block.data = 'Changed'
print('Testing after data changed: ', my_block.is_valid(difficulty_test, ''),
      '\n')

my_chain = Chain(lambda hash_: hash_[:2] == 2 * '0')
my_chain.add_block('Hi')
print(my_chain, '\n')
print('Testing validation of chain: ', my_chain.is_valid(), '\n')
my_chain.chain[0].data = 'CHANGED'
print('Testing after data changed: ', my_chain.is_valid())
