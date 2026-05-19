import main
import modules.wiki as wiki
import modules.openai_api as openai_api

def test_user_main_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Topics 1")
    assert main.user_main_input() == "Hello World!"