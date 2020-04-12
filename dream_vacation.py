responses = {}
poll_active = True

while poll_active:
    name = input('Hi, what\'s your name ? ')
    response = input('Where would you like to spend your dream vacation: ')
    
    responses[name] = response
    repeat = input('Would you like to let another person repond (yes/no) ')
    if repeat.lower() == 'no':
        poll_active = False
        print(responses[name])
        
print('\n Poll Result')
for name, response in responses.items():
    print(f'{name}\'s dream vacation is {response}.')
