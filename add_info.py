import main as load

def main():
    while True:
        print('Choose your action')
        print('1 - Add short link')
        print('2 - Remove short link')
        print('3 - Show all links')
        print('4 - Exit program')
        print('-----------------------')
        add_info = int(input('What do you want to do:'))
        if add_info == 1:
            load.dictionary_services[input('Input a link:')] = input('Input a value:')
        elif add_info == 2:
            load.dictionary_services.pop(input('Input a link to delete:'))
        elif add_info == 3:
            print(load.dictionary_services)
        elif add_info == 4:
            print('See you next time')
            break
        else:
            print('Unknown action.')
            continue

main()