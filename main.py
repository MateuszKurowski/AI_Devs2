from tasks import helloapi, moderation, blogger, liar, inprompt, embedding, whisper, functions, rodo, scraper
import os

tasks = {
    'helloapi': helloapi.main,
    'moderation': moderation.main,
    'blogger': blogger.main,
    'liar': liar.main,
    'inprompt': inprompt.main,
    'embedding': embedding.main,
    'whisper': whisper.main,
    'functions': functions.main,
    'rodo': rodo.main,
    'scraper': scraper.main,
}

def main():
    try:
        os.system('cls')
        print('AI_DEVS 2')
        print()
        print('Dostępne zadania:')
        for i, task_name in enumerate(tasks.keys(), start=1):
            print(f'{i}. {task_name}')

        print()
        choice = input('Podaj numer lub nazwę zadania który chcesz wykonać: ')
        os.system('cls')

        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(tasks):
                selected_function = list(tasks.values())[number - 1]
                selected_function()
            else:
                print('Nieprawidłowy numer zadania.')
                print()
                input('Naciśnij [enter], aby wrócić do menu wyboru.')
                main()
        else:
            if choice in tasks:
                selected_function = tasks [choice]
                selected_function()
            else:
                print('Nieprawidłowy numer zadania.')
                print()
                input('Naciśnij [enter], aby wrócić do menu wyboru.')
                main()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()