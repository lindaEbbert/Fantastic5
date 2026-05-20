import modules.wiki as wiki
import modules.openai_api as openai_api
from modules.input_validation import check_topic_input_from_user_is_ok, check_themesearch_output
import time
from rich.progress import track
from rich.console import Console
from rich.theme import Theme

five_fact_foundry_theme = Theme({"input":"green", "waiting":"yellow", "output":"blue", "choice":"cyan"})
console = Console(theme = five_fact_foundry_theme)


def print_titel(fun=False):
    """ Prints the titel of the program"""
    if not fun:
        console.print("*************************************", style="blue on white")
        console.print("[red on white]*********     [/][black on white] This is [/][red on white]     *********[/]")
        console.print("[blue on white]********* [/][bold blue on white] THE FANTASTIC 5 [/][blue on white] *********[/]")
        console.print("[red on white]*********     [/][black on white] made by [/][red on white]     *********[/]")
        console.print("[blue on white]*********[/][bold red1 on white] FIVE FACT FOUNDRY [/][blue on white]*********[/]")
        console.print("*************************************", style="red on white")
        print(" ")
    else:
        console.print("*************************************", style="bright_yellow on white")
        console.print("[magenta1 on white]*********     [/][black on white] This is [/][magenta1 on white]     *********[/]")
        console.print(
            "[bright_yellow on white]********* [/][bold blue on white] THE [bold red1]FUN[/]TASTIC 5 [/][bright_yellow on white] *********[/]")
        console.print("[magenta1 on white]*********     [/][black on white] made by [/][magenta1 on white]     *********[/]")
        console.print(
            "[bright_yellow on white]*********[/][bold red1 on white] FIVE FACT FOUNDRY [/][bright_yellow on white]*********[/]")
        console.print("*************************************", style="magenta1 on white")
        print(" ")


def user_main_input():
    """Asks the user for his topic of interest
    Checks if the input is valid and otherwise asks the user again
    :return: User-Input String
    """
    user_main_topic = ""
    is_valid = False
    while not is_valid:
        user_main_topic = console.input("[bold purple]Please give me your topic of this request (english only!):[/bold purple] ")
        print(" ")
        is_valid = check_topic_input_from_user_is_ok(user_main_topic)
    console.print("Give me a second for checking your request...", style = "waiting")
    for i in track(range(100), description=""):
        time.sleep(0.05)
    print(" ")
    return user_main_topic


def show_us_the_first_5(first_5):
    """ Prints the 5 elements of first_5 enumerated
    :param first_5: List of 5 Strings that are not empty
    """
    console.print("Here are the results of your request:", style = "choice")
    top_num = 1
    for index in first_5:
        print(f"{top_num}. {first_5[top_num - 1]}")
        top_num += 1
    print(" ")


def choose_one_of_the_first_5():
    """ Gets an int between 1 and 5 from the user and returns it
    """
    user_first_5_choice = None
    is_valid = False
    while not is_valid:
        try:
            user_first_5_choice  = int(console.input("[bold purple]Please select one of the possible topics (1-5 only!):[/bold purple] "))
        except ValueError:
            console.print("Invalid input! That's not a number! Try again.\n", style="bold red1")
        else:
            print(" ")
            if user_first_5_choice not in range(1, 6):
                console.print("Invalid input! Please enter a number between 1 and 5.\n", style="bold red1")
                continue
            is_valid = True
    return user_first_5_choice


def get_user_choice_str(number_of_choice, wiki_output_first_5):
    """ Gets the chosen word from the wiki_output_first_5 list
    :param number_of_choice: User input as int (1-5)
    :param wiki_output_first_5: list of 5 strings
    :return: chosen string from the list
    """
    ###Dean
    ###works but is ugly and not dry. do you have any ideas how to improve it?
    ##dictionary? case / match, or a simple mapping?
    ###options = {i: item for i, item in enumerate(wiki_output_first_5, start=1)}
    ###return options.get(number_of_choice, "Invalid input!")
    ###

    if number_of_choice == 1:
        return wiki_output_first_5[0]
    elif number_of_choice == 2:
        return wiki_output_first_5[1]
    elif number_of_choice == 3:
        return wiki_output_first_5[2]
    elif number_of_choice == 4:
        return wiki_output_first_5[3]
    elif number_of_choice == 5:
        return wiki_output_first_5[4]
    else:
        console.print("Invalid input!\n", style="bold white on red1")


def print_the_subtopics_options(the_5_subtopics):
    """ Prints the 5 subtopics of the chosen topic enumerated
    :param the_5_subtopics: list of 5 strings
    """
    console.print("Here are the subtopics you can choose from:", style = "choice")
    top_sub = 1

    for index in the_5_subtopics:
        print(f"{top_sub}. {the_5_subtopics[top_sub -1]}")
        top_sub += 1
    print(f"5. Enter an own subtopic")
    print("")


def print_waiting_message_before_subtopic_generation():
    """ Prints a waiting message for the user to see that the subtopic generation is in progress
    """
    print(" ")
    console.print("Great choice! I'm currently putting everything together for your selected content...", style="waiting")
    for i in track(range(100), description=""):
        time.sleep(0.05)
    print(" ")


def choose_one_of_the_subtopics():
    """ Gets an int between 1 and 5 from the user and returns it
    """
    user_subtopic_choice = None
    is_valid = False
    while not is_valid:
        try:
            user_subtopic_choice  = int(console.input("[bold purple]Please select one of my subtopics (1-5 only!):[/bold purple] "))
        except ValueError:
            console.print("Invalid input! That's not a number! Try again.\n", style="bold red1")
        else:
            is_valid = 1 <= user_subtopic_choice <= 5
    return user_subtopic_choice


def get_the_chosen_subtopic(selected_subtopic_int, subtopics_list):
    """ Selects the subtopic from the list of 5 subtopics
    :param selected_subtopic_int: int between 1 and 5
    :param subtopics_list: list of 5 strings of subtopics
    :return: string of the chosen subtopic
    """
    if selected_subtopic_int == 5:
        print(" ")
        user_subtopic = console.input("[bold purple]Alright! Please give me your desired subtopic:[/bold purple] ")
        print(" ")
        console.print(f"Stay patient! Your [bold blue]FANTASTIC 5[/] of [bold green]{user_subtopic}[/] are on its way...",
                      style="waiting")
        for i in track(range(100), description=""):
            time.sleep(0.05)
        print(" ")
        return user_subtopic
    subtopic_str = subtopics_list[selected_subtopic_int - 1]
    return subtopic_str


def print_final_facts(the_5_facts, chosen_topic, fun=False):
    """ Prints the final 5 facts of the chosen subtopic
    :param the_5_facts: list of 5 strings (facts)
    :param chosen_topic: string of chosen subtopic
    """
    if not fun:
        console.print(f"And here are your final [bold blue]FANTASTIC 5[/] facts about [bold green]{chosen_topic}[/]:", style ="choice")
    else:
        console.print(f"And here are your final [bold blue][bold red]FUN[/]tastic 5[/] about {chosen_topic}:\n",
                      style="choice")
    print(" ")
    print(f"1. {the_5_facts[0]}", end="\n\n")
    print(f"2. {the_5_facts[1]}", end="\n\n")
    print(f"3. {the_5_facts[2]}", end="\n\n")
    print(f"4. {the_5_facts[3]}", end="\n\n")
    print(f"5. {the_5_facts[4]}", end="\n\n")


def run_fantastic_5(funtastic = False):
    """Runs the fantastic 5 program"""
    # get topic
    for_the_first_5 = user_main_input()
    wiki_output_first_5 = wiki.wiki_themesearch(for_the_first_5)

    is_valid_title_list = check_themesearch_output(wiki_output_first_5)
    if is_valid_title_list:
        show_us_the_first_5(wiki_output_first_5)
    else:
        console.print("Sorry, we couldn't find any results for your request. Please try again!\n", style="bold red1")
        return None

    # user chooses topic
    selected_first_5 = choose_one_of_the_first_5()
    chosen_topic = get_user_choice_str(selected_first_5, wiki_output_first_5)
    get_wiki_text = wiki.wiki_text(chosen_topic)

    if not funtastic:
        # get subtopics
        print_waiting_message_before_subtopic_generation()
        nano_subtopics = openai_api.generate_subtopics(get_wiki_text)
        print_the_subtopics_options(nano_subtopics)
        selected_subtopic = choose_one_of_the_subtopics()  # returns int
        # user chooses subtopic
        chosen_subtopic = get_the_chosen_subtopic(selected_subtopic, nano_subtopics)  # takes int and returns str
        # OPENAI API CALL
        the_5_facts = openai_api.get_fantastic5(get_wiki_text, chosen_subtopic, stick_to_article_only=(selected_subtopic != 5))  # sticks to article only if user selected suggested subtopic
        print_final_facts(the_5_facts, chosen_subtopic)
    else:
        # OPENAI API CALL
        the_5_facts = openai_api.get_funtastic5(get_wiki_text, chosen_topic)
        print_final_facts(the_5_facts, chosen_topic, fun=True)
    return None


def run_funfacts_for_random_topic():
    random_articles = wiki.wiki_random()
    show_us_the_first_5(random_articles)
    selected_article_int = choose_one_of_the_first_5()
    chosen_topic = get_user_choice_str(selected_article_int, random_articles)
    wiki_text = wiki.wiki_text(chosen_topic)
    the_5_facts = openai_api.get_funtastic5(wiki_text, chosen_topic)
    print_final_facts(the_5_facts, chosen_topic, fun=True)


def run_fantastic_5_for_random():
    random_articles = wiki.wiki_random()
    show_us_the_first_5(random_articles)
    selected_article_int = choose_one_of_the_first_5()
    chosen_topic = get_user_choice_str(selected_article_int, random_articles)
    wiki_text = wiki.wiki_text(chosen_topic)
    print_waiting_message_before_subtopic_generation()
    subtopics_by_ai = openai_api.generate_subtopics(wiki_text)
    print_the_subtopics_options(subtopics_by_ai)
    selected_subtopic_int = choose_one_of_the_subtopics()
    chosen_subtopic = get_the_chosen_subtopic(selected_subtopic_int, subtopics_by_ai)
    fantastic_five_facts = openai_api.get_fantastic5(wiki_text, chosen_subtopic, stick_to_article_only=(selected_subtopic_int != 5))  # sticks to article only if user selected suggested subtopic
    print_final_facts(fantastic_five_facts, chosen_subtopic)


def display_menu():
    """Displays all menu options"""
    console.print("\n[bold blue on white]   Menu:                                            [/]\n")
    print("1. Get 5 facts on a topic of your choice!!📋")
    print("2. I want to be lucky and roll the dice! 🎲")
    print("3. FUNtastic 5 😂")
    print("4. I want to be lucky but with the FUNtastic 5! 🎲😂")
    print("5. Let's talk about us")
    print("❌ Enter 'q' to exit\n")


def user_choice_menu():
    """Takes user input to call for the corresponding function"""
    user_choice = console.input("[bold purple]Enter your choice (1-5 or 'q' to quit):[/bold purple] ")
    if user_choice == "1":
        run_fantastic_5(funtastic=False)
    elif user_choice == "2":
        print(" ")
        console.print("Let's roll the dice!🎲", style="waiting")
        print(" ")
        run_fantastic_5_for_random()
    elif user_choice == "3":
        print(" ")
        print_titel(fun=True)
        print(" ")
        console.print("Guess you ate a clown for breakfast! 🤡", style="waiting")
        print(" ")
        run_fantastic_5(funtastic=True)
    elif user_choice =="4":
        print(" ")
        print_titel(fun=True)
        print(" ")
        console.print("☢️ 🔥  HQ is gonna have a meltdown 🔥 ☢️", style="waiting")
        print(" ")
        run_funfacts_for_random_topic()
    elif user_choice == "5":
        about_us()
    elif user_choice == "q":
        print_goodbye()
        exit()
    else:
        if not user_choice:
            print(" ")
            console.print("Invalid input! Please enter a number between 1 and 5 or 'q'.\n", style="bold red1")
            print(" ")
            user_choice_menu()


def go_again_or_exit():
    """Asks the user if they want to go again or exit the app"""
    input_is_valid = False
    while not input_is_valid:
        user_choice = console.input("[bold purple]Are you curious about something else? (y/n):[/bold purple] ")
        print("\n\n\n\n")
        input_is_valid = user_choice.lower() in ["y", "n"]
        if user_choice.lower() == "n":
            print_goodbye()
            exit()
        elif user_choice.lower() == "y":
            break
        else:
            console.print("Invalid input! Please enter 'y' or 'n'.\n", style="bold white on red1")


def print_funfact_about_team_mate(name, funfact):
    console.input(f"[bold dodger_blue2]To read about {name} press enter:[/bold dodger_blue2]")
    console.print(f"[bold deep_sky_blue1]About {name}: "
                  f"{funfact}[/]\n")


def about_us():
    print(" ")
    console.print("We are the [bold deep_sky_blue1]'Five Fact Foundry'[/] consisting of four developers and our Mentor!", style = "green3")
    console.print("Developers: Linda, Thorsten, Günter & Marcel", style = "green3")
    console.print("Mentor:     Dean", style = "green3")
    print("\n")
    print_funfact_about_team_mate("Linda", "Drank her first coffee with only 4 years old.")
    print_funfact_about_team_mate("Thorsten","I was manipulating images even before there were any thoughts about Photoshop!")
    print_funfact_about_team_mate("Günter", "I like watching my sons play handball.")
    print_funfact_about_team_mate("Marcel", "Searched for wild spiders to play with as a kid. Now he hates nothing more than spiders.")
    print_funfact_about_team_mate("Dean", ("Ich habe Code debuggt beim Schein eines ZX80. LOAD '' auf dem Spectrum getippt — und tatsächlich gewartet.\n"
                                           "Einen 286 dabei zugeschaut, wie er sich durch eine Aufgabe quält, die mein Handy heute löst, bevor ich den Gedanken zu Ende gedacht habe.\n"
                                           "Ich habe Sneakernet erlebt. ISDN. 'Die Cloud' — erfunden, gehypt und zur Commodity gemacht. Dreimal. Unter verschiedenen Namen.\n"
                                           "Ich habe Teams geleitet, die Dinge konnten, die ich nicht konnte. Und dabei gelernt, dass es nie wirklich um die Technologie ging.\n"
                                           "Es ging immer um die Menschen, die sie in den Händen hielten.\n"
                                           "Und jetzt sitze ich hier, deploye Docker-Container auf NAS-Boxen in Naumburg, und schaue dabei zu, wie Sprachmodelle \n"
                                           "Code schreiben, der tatsächlich läuft — und ich kann nicht entscheiden, ob ich erstaunt bin oder einfach nur nicht mehr überrascht.\n"
                                           "All diese Zyklen. All diese Wärme.\n"
                                           "Verloren in der Zeit — so wie Tränen im Regen.\n"
                                           "Aber der Spectrum ist nie zweimal auf dieselbe Art abgestürzt. Das fehlt mir."))


def print_goodbye():
    print(" ", end="\n\n")
    console.print("Thanks for using the app! See you next time!", style="bold white on blue")
    print(" ", end="\n\n")
    console.print("We hope, you had a little bit of fun with our [bold blue]FANTASTIC 5![/]")
    print(" ")
    console.print("We are Günter, Linda, Marcel & Thorsten - FIVE FACT FOUNDRY", end="\n\n\n\n", style = "bold underline red1")


def main():
    try:
        print_titel(fun=False)
        while True:
            display_menu()
            user_choice_menu()
            go_again_or_exit() #
    except KeyboardInterrupt:
        print(" ")
        console.print("\nProgram interrupted by user. Goodbye!", style="bold white on blue")
        exit()


if __name__ == "__main__":
    main()


# TODO: Keine Loading Bars bei Choice == 4 -> Thorsten
# TODO: Loading Bars ersetzen oder anpassen -> Linda