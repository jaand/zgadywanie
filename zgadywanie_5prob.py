import random
def play_game():
    myname = input('Jak mam Cię nazywać?')
    print ('Dobra',myname,'zgadnij cyfrę bądź liczbę od 1 do 100, masz 5 szans.')
    number = random.randint(1,100)
    guess = 0
    while guess < 5:
        try:
            guess_number = int(input('Co obstawiasz?'))
        except ValueError:
            print('Wpisz liczbę.')
            continue
        guess = guess + 1
        if guess_number < number:
            print ('Troche więcej')
        elif guess_number > number:
            print ('Troche mniej')
        elif guess_number == number:
            continue_game = input('Zgadłeś! Chesz zagrać jeszcze raz? (Y/N)')
            if continue_game == "Y":
                print("--" * 42)
                play_game()
            else:
                print("Thanks for playing :)")
                exit(0)    
        if guess == 5:
            continue_game = input('Przegrałeś, prawidłowy numer to',number, 'Chcesz zagrać jeszcze raz? (Y/N)')
            if continue_game == "Y":
                print("--" * 42)
                play_game()




            else:
                print("Thanks for playing :)")
                exit(0)

play_game()
