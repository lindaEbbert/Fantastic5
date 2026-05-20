MAX_LENGTH_USER_TOPIC = 255

def check_themesearch_output(five_wiki_titles):
    """ Checks if the output of the wiki_themesearch function is a list of 5 titles
    :param five_wiki_titles: output of the wiki_themesearch function
    :return: Boolean
    """
    is_list = isinstance(five_wiki_titles, list)
    try:
        has_5_items = len(five_wiki_titles) == 5
    except Exception:
        has_5_items = False
    try:
        items_are_all_strings = all([isinstance(item,str) for item in five_wiki_titles])
    except Exception:
        items_are_all_strings = False
    try:
        has_no_empty_strings = all([len(item) > 0 for item in five_wiki_titles])
    except Exception:
        has_no_empty_strings = False
    return all([is_list, has_5_items, items_are_all_strings, has_no_empty_strings])


def check_topic_input_from_user_is_ok(user_main_topic):
    try:
        is_correct_length = len(user_main_topic) <= MAX_LENGTH_USER_TOPIC
    except Exception:
        is_correct_length = False
    is_string = isinstance(user_main_topic, str)
    return all([is_correct_length, is_string])

