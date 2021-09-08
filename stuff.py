# iteration
print('sds')

if __name__ == '__main__':

    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    frenchDays = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sat']

    # TODO iter method
    # itdays = iter(days)
    # print(next(itdays))
    #
    # print(f'itrated days {next(itdays)}')

    # TODO enumerate method
    for x, i in enumerate(days):
        print(f'{x} {i}')