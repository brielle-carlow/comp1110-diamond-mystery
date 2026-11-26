from project import get_player_choice, check_answer, display_result

# Test get_player_choice()
def test_get_player_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Sarah")
    assert get_player_choice() == "Sarah"

# Test check_answer()
def test_check_answer_correct():
    assert check_answer("Sarah", "Sarah") == True

def test_check_answer_incorrect():
    assert check_answer("John", "Sarah") == False

# Test display_result()
def test_display_result_correct(capsys):
    display_result(True, "Sarah")
    assert "Congratulations!" in capsys.readouterr().out

def test_display_result_incorrect(capsys):
    display_result(False, "Sarah")
    assert "CASE UNSOLVED" in capsys.readouterr().out
