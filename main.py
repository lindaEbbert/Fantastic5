import modules.wiki as wiki
import modules.openai_api as openai_api
import time
from rich.progress import track
from rich.console import Console
from rich.theme import Theme

five_fact_foundry_theme = Theme({"input":"green", "waiting":"yellow", "output":"blue", "choice":"cyan"})
console = Console(theme = five_fact_foundry_theme)


def titel_print():
    console.print("*************************************", style="blue on white")
    console.print("[red on white]*********     [/][black on white] This is [/][red on white]     *********[/]")
    console.print("[blue on white]********* [/][bold blue on white] THE FANTASTIC 5 [/][blue on white] *********[/]")
    console.print("[red on white]*********     [/][black on white] made by [/][red on white]     *********[/]")
    console.print("[blue on white]*********[/][bold red on white] FIVE FACT FOUNDRY [/][blue on white]*********[/]")
    console.print("*************************************", style="red on white")
    print(" ")


def user_main_input():
    user_main_topic = console.input("[bold purple]Please give me your topic of this request (english only!):[/bold purple] ")
    print(" ")
    console.print("Give me a second for checking your request...", style = "waiting")
    for i in track(range(100), description=""):
        time.sleep(0.05)
    print(" ")
    return user_main_topic


def show_us_the_first_5(first_5):
    console.print("Here are the results of your request:", style = "choice")
    top_num = 1
    for index in first_5:
        print(f"{top_num}. {first_5[top_num - 1]}")
        top_num += 1
    print(" ")


def choose_one_of_the_first_5():
    user_first_5_choice  = int(console.input("[bold purple]Please select one of the possible topics (1-5 only!):[/bold purple] "))
    print(" ")
    console.print("Great choice! I'm currently putting everything together for your selected content...", style = "waiting")
    for i in track(range(100), description=""):
        time.sleep(0.05)
    print(" ")
    return user_first_5_choice


def get_the_chosen_word(number_of_choice, wiki_output_first_5):
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
        print("Invalid input!")


def show_us_the_5_subtopics(the_5_subtopics):
    console.print("Here are the subtopics you can choose from:", style = "choice")
    top_sub = 1

    #print(f"Type: {type(the_5_subtopics)}")

    for index in the_5_subtopics:
        print(f"{top_sub}. {the_5_subtopics[top_sub -1]}")
        top_sub += 1
    print(f"5. Enter an own subtopic")
    print("")


def choose_one_of_the_subtopics():
    user_subtopic_choice  = int(console.input("[bold purple]Please select one of my subtopics (1-5 only!):[/bold purple] "))
    return user_subtopic_choice


def get_the_chosen_subtopic(selected_subtopic, open_ai_subtopic_of_5):
    if selected_subtopic == 1:
        print(" ")
        console.print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[0]} are on its way...", style = "waiting")
        for i in track(range(100), description=""):
            time.sleep(0.05)
        print(" ")
        return open_ai_subtopic_of_5[0]
    elif selected_subtopic == 2:
        print(" ")
        console.print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[1]} are on its way...", style = "waiting")
        for i in track(range(100), description=""):
            time.sleep(0.05)
        print(" ")
        return open_ai_subtopic_of_5[1]
    elif selected_subtopic == 3:
        print(" ")
        console.print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[2]} are on its way...", style = "waiting")
        for i in track(range(100), description=""):
            time.sleep(0.05)
        print(" ")
        return open_ai_subtopic_of_5[2]
    elif selected_subtopic == 4:
        print(" ")
        console.print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[3]} are on its way...", style = "waiting")
        for i in track(range(100), description=""):
            time.sleep(0.05)
        print(" ")
        return open_ai_subtopic_of_5[3]
    elif selected_subtopic == 5:
        print(" ")
        user_subtopic = console.input("[bold purple]Alright! Please give me your desired subtopic:[/bold purple] ")
        print(" ")
        console.print(f"Stay patient! Your [bold blue]FANTASTIC 5[/] of [bold green]{choose_subtopic}[/] are on its way...", style = "waiting")
        for i in track(range(100), description=""):
            time.sleep(0.05)
        print(" ")
        return user_subtopic
    else:
        print("Invalide input!")


def final_fantastic_5(the_5_facts, choose_subtopic):
    console.print(f"And here are your final [bold blue]FANTASTIC 5[/] facts about [bold green]{choose_subtopic}[/]:", style = "choice")
    print(" ")
    print(f"1. {the_5_facts[0]}", end="\n\n")
    print(f"2. {the_5_facts[1]}", end="\n\n")
    print(f"3. {the_5_facts[2]}", end="\n\n")
    print(f"4. {the_5_facts[3]}", end="\n\n")
    print(f"5. {the_5_facts[4]}", end="\n\n")
    print(" ", end="\n\n")
    console.print("We hope, you had a little bit of fun with our [bold blue]FANTASTIC 5![/]")
    print(" ")
    console.print("We are Günter, Linda, Marcel & Thorsten - FIVE FACT FOUNDRY", end="\n\n\n\n", style = "bold underline red")


def main():
    titel_print()
    for_the_first_5 = user_main_input()

    #print("\033[33mTEST-PRINT: for_the_first_5", for_the_first_5, type(for_the_first_5), end="\n\n\033[0m")

    wiki_output_first_5 = wiki.wiki_themesearch(for_the_first_5)

    #print("\033[33mTEST-PRINT: von Günter Top 5", wiki_output_first_5, type(wiki_output_first_5), end="\n\n\033[0m")

    show_us_the_first_5(wiki_output_first_5)
    selected_first_5 = choose_one_of_the_first_5()
    chosen_topic = get_the_chosen_word(selected_first_5, wiki_output_first_5)

    #print("\033[33mTEST-PRINT: chosen_topic", chosen_topic, type(chosen_topic), end="\n\n\033[0m")

    get_wiki_text = wiki.wiki_text(chosen_topic)

    #print("\033[33mTEST-PRINT: von Günter text", type(get_wiki_text), end="\n\n\033[0m")

    nano_subtopics = openai_api.generate_subtopics(get_wiki_text)

    show_us_the_5_subtopics(nano_subtopics)
    selected_subtopic = choose_one_of_the_subtopics() # returns int

    chosen_subtopic = get_the_chosen_subtopic(selected_subtopic, nano_subtopics) # takes int and returns str
    if chosen_subtopic in nano_subtopics:
        openai_api.get_fantastic5(get_wiki_text, chosen_subtopic)
    else:
        openai_api.get_fantastic5(get_wiki_text, chosen_subtopic, stick_to_article_only = False)

    #print("\033[33mTEST-PRINT: chosen_subtopic", chosen_subtopic, type(chosen_subtopic), end="\n\n\033[0m")

    the_5_facts = openai_api.get_fantastic5(get_wiki_text, chosen_subtopic)

    final_fantastic_5(the_5_facts, chosen_subtopic)


if __name__ == "__main__":
    main()
