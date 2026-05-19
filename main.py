from models import wiki


def titel_print():
    print("*************************************")
    print("************** This is **************")
    print("********** THE FANTASTIC 5 **********")
    print("************** made by **************")
    print("********* FIVE FACT FOUNDRY *********")
    print("*************************************")
    print(" ")


def user_main_input():
    user_main_topic = input("Please give me your topic of this request (english only!): ")
    print("Give me a second for checking your request...")
    print(" ")
    return user_main_topic


"""def wikis_first_5(topic):
    GÜNTERS_ERSTE_FUNKTION: Dies ist die Funktion,
    die die erste User-Eingabe an Wikipedia weiter
    gibt und dann die first_5 zurückgibt, damit der
    User seine Auswahl konkretisieren kann.

    first_5 = ["choice 1","choice 2", "choice 3", "choice 4", "choice 5"] # Platzhalter für Liste aus Wikipedia
    return first_5"""


def show_us_the_first_5(first_5):
    print("Here are the results of your request:")
    ###Dean
    #think about DRY Do Not Repeat yourself
    #for index, item in enumerate(first_5, start=1):
        #print(f"{index}. {item}")
    print(f"1. {first_5[0]}")
    print(f"2. {first_5[1]}")
    print(f"3. {first_5[2]}")
    print(f"4. {first_5[3]}")
    print(f"5. {first_5[4]}")
    print(" ")


def choose_one_of_the_first_5():
    user_first_5_choice  = int(input("Please select one of the possible topics (1-5 only!): "))
    print("Great choice! I'm currently putting everything together for your selected content...")
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
        return wikis_first_5[0]
    elif number_of_choice == 2:
        return wiki_output_first_5[1]
    elif number_of_choice == 3:
        return wiki_output_first_5[2]
    elif number_of_choice == 4:
        return wiki_output_first_5[3]
    elif number_of_choice == 5:
        return wiki_output_first_5[4]
    else:
        print("Invalide input!")



def get_the_subtopics(chosen_topic):
    """LINDAS_UND_MARCELS_ERSTE_FUNKTION: Dies ist die Funktion,
    die das ausgewählte Thema aus WIKIPEDIA an OPEN_AI weiter
    gibt und dann die 5 Sub-Themen zurückgibt, damit
    der User seine Auswahl treffen kann."""

    the_5_subtopics = ["Subtopic 1", "Subtopic 2", "Subtopic 3", "Subtopic 4", "Subtopic 5"] # Platzhalter für Liste aus Open AI
    return the_5_subtopics


def show_us_the_5_subtopics(the_5_subtopics):
    print("Here are the subtopics you can choose from:")
    print(f"1. {the_5_subtopics[0]}")
    print(f"2. {the_5_subtopics[1]}")
    print(f"3. {the_5_subtopics[2]}")
    print(f"4. {the_5_subtopics[3]}")
    print(f"5. Enter an own subtopic")
    print("")


def choose_one_of_the_subtopics():
    user_subtopic_choice  = int(input("Please select one of my subtopic (1-5 only!): "))
    return user_subtopic_choice


def get_the_chosen_subtopic(selected_subtopic, open_ai_subtopic_of_5):
    if selected_subtopic == 1:
        print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[0]} are on its way...")
        print(" ")
        return open_ai_subtopic_of_5[0]
    elif selected_subtopic == 2:
        print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[1]} are on its way...")
        print(" ")
        return open_ai_subtopic_of_5[1]
    elif selected_subtopic == 3:
        print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[2]} are on its way...")
        print(" ")
        return open_ai_subtopic_of_5[2]
    elif selected_subtopic == 4:
        print(f"Stay patient! Your FANTASTIC 5 of {open_ai_subtopic_of_5[3]} are on its way...")
        print(" ")
        return open_ai_subtopic_of_5[3]
    elif selected_subtopic == 5:
        user_subtopic = input("Alright! Please give me your desired subtopic: ")
        print(f"Stay patient! Your FANTASTIC 5 of {user_subtopic} are on its way...")
        print(" ")
        return user_subtopic
    else:
        print("Invalid input!")


def get_the_final_5(choose_topic):
    """LINDAS_UND_MARCELS_ZWEITE_FUNKTION: Dies ist die Funktion,
        die das ausgewählte Subthema noch einmal an OPEN_AI übergibt
        und dann die FANTASTIC 5 zurückgibt."""

    the_5_facts = ["Bla,bla, bla, Text1", "Bla,bla, bla, Text2", "Bla,bla, bla, Text3", "Bla,bla, bla, Text4", "Bla,bla, bla, Text5"]  # Platzhalter für Liste aus Open AI
    return the_5_facts

def final_fantastic_5(the_5_facts, choose_subtopic):
    print(f"And here are your final FANTASTIC 5 facts about {choose_subtopic}:")
    print(f"1. {the_5_facts[0]}")
    print(f"2. {the_5_facts[1]}")
    print(f"3. {the_5_facts[2]}")
    print(f"4. {the_5_facts[3]}")
    print(f"5. {the_5_facts[4]}")
    print(" ")
    print("We hope, you had a little bit of fun with our FANTASTIC 5!")
    print(" ")
    print("We are Günter, Linda, Marcel & Thorsten - FIVE FACT FOUNDRY")


def main():
    titel_print()
    for_the_first_5 = user_main_input()

    print("\033[33mTEST-PRINT: for_the_first_5", for_the_first_5, type(for_the_first_5), end="\n\n\033[0m")

    wiki_output_first_5 = wiki.wiki_themesearch(for_the_first_5)

    print("\033[33mTEST-PRINT: von Günter", wiki_output_first_5, type(wiki_output_first_5), end="\n\n\033[0m")

    show_us_the_first_5(wiki_output_first_5)
    selected_first_5 = choose_one_of_the_first_5()
    chosen_topic = get_the_chosen_word(selected_first_5, wiki_output_first_5)

    print("\033[33mTEST-PRINT: chosen_topic", chosen_topic, type(chosen_topic), end="\n\n\033[0m")

    open_ai_subtopic_of_5 = get_the_subtopics(chosen_topic)
    show_us_the_5_subtopics(open_ai_subtopic_of_5)
    selected_subtopic = choose_one_of_the_subtopics()
    choose_subtopic = get_the_chosen_subtopic(selected_subtopic, open_ai_subtopic_of_5)

    print("\033[33mTEST-PRINT: choose_subtopic", choose_subtopic, type(choose_subtopic), end="\n\n\033[0m")

    the_5_facts = get_the_final_5(choose_subtopic)

    final_fantastic_5(the_5_facts, choose_subtopic)


if __name__ == "__main__":
    main()
