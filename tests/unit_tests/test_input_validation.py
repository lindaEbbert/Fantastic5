from modules.input_validation import check_themesearch_output, check_topic_input_from_user_is_ok, MAX_LENGTH_USER_TOPIC

def test_user_main_input(monkeypatch):
    # monkeypatch.setattr("builtins.input", lambda _: "Topics 1")
    # assert main.user_main_input() == "Hello World!"
    pass

def test_check_themesearch_output_types():
    assert check_themesearch_output("") == False
    assert check_themesearch_output(123) == False
    assert check_themesearch_output(None) == False
    assert check_themesearch_output(True) == False

def test_check_themesearch_output_length():
    assert check_themesearch_output(["test","test","test","test","test"]) == True
    assert check_themesearch_output(["test","test","test","test"]) == False
    assert check_themesearch_output(["test","test","test","test","test","test"]) == False
    assert check_themesearch_output([]) == False
    assert check_themesearch_output("test") == False

def test_check_themesearch_output_content():
    assert check_themesearch_output(["", "", "", "", ""]) == False
    assert check_themesearch_output(["test", "", "test", "test", "test"]) == False


def test_check_topic_input_from_user_is_ok_types():
    assert check_topic_input_from_user_is_ok(123) == False
    assert check_topic_input_from_user_is_ok(None) == False
    assert check_topic_input_from_user_is_ok(True) == False
    assert check_topic_input_from_user_is_ok(["Test"]) == False
    assert check_topic_input_from_user_is_ok("Test") == True


def test_check_topic_input_from_user_is_ok_length():
    assert check_topic_input_from_user_is_ok("t"*MAX_LENGTH_USER_TOPIC) == True
    assert check_topic_input_from_user_is_ok("t"*(MAX_LENGTH_USER_TOPIC+1)) == False


def test_check_topic_input_from_user_is_ok_content():
    assert check_topic_input_from_user_is_ok("") == True
    assert check_topic_input_from_user_is_ok(" ") == True
    assert check_topic_input_from_user_is_ok("123") == True
    assert check_topic_input_from_user_is_ok("!?§$% (,-.") == True
    assert check_topic_input_from_user_is_ok("test") == True
    assert check_topic_input_from_user_is_ok("TEST") == True