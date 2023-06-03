from hangman import guessing

def test_empty():
    assert guessing([], "apple") == "_____"
    assert guessing([], "inconcievable") == "_____________"

def test_partial():
    assert guessing(["a", "b", "c", "p"], "apple") == "app__"

def test_final():
    assert guessing(["a", "p", "l", "e"], "apple") == "apple"