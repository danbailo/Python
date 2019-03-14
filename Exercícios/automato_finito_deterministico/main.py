import gui

if __name__ == "__main__":

    while True:
        print('Input a word: ', end='')
        if gui.aut.feed(input()) == True: print('word accepted!')
        else: print('word rejected!')

        gui.aut.reset()
        test = str(input('test again? "yes" or "not": ')).lower()
        print()
        if test[0] == 'n':
            break

    gui.f.view()
