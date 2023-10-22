from casino_game_logic import spin_roulette, play_round


def main():
    capital = 1000  # Начальный капитал игрока

    while True:
        print(f"Ваш текущий капитал: ${capital}")

        bet = input("Сделайте вашу ставку (число от 0 до 36): ")
        bet = int(bet)

        if 0 <= bet <= 30:
            capital, win = play_round(capital, bet)

            if win:
                print("Вы выиграли!")
            else:
                print("Вы проиграли.")

        if capital <= 0:
            print("У вас больше нет денег. Игра окончена.")
            break

        play_again = input("Сыграть еще раз? (да/нет): ")
        if play_again.lower() != 'да':
            break


if __name__ == "__main__":
    main()
