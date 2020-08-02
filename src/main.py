from chainblock import Chain

my_chain = Chain()
my_chain.add_block('This is a new block')
my_chain.add_block('And this is another block')
print(f'This is my chain:\n{my_chain}')
print(f'Is it a valid chain?! {my_chain.is_valid()}')
my_chain.chain[2].data = 'Changed data'
print(f'Is it still valid?! {my_chain.is_valid()}')
