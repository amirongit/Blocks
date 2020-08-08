from chainblock import Chain, Block

new_block = Block('A new block!', '', lambda hash_: hash_[:2] == 2 * '0')
print(new_block)
print(f'validating... {new_block.is_valid()}')
print('changing data...')
new_block.data = 'This data is now changed!'
print(f'validating... {new_block.is_valid()}')

new_chain = Chain(lambda hash_: hash_[:2] == 2 * '0')
new_chain.add_block('This is the first valid block!')
new_chain.add_block('And this is another block.')
print(f'validating... {new_chain.is_valid()}')
print('changing data...')
new_chain.chain[1].data = 'This data is now changed!'
print(new_chain)
print(f'validating... {new_chain.is_valid()}')
