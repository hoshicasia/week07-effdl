from toxic_server.model import predict


def test_predict_toxic():
    assert predict("Listen here you dumbass")


def test_predict_non_toxic():
    assert not predict("Thank you, have a pleasant evening")


def test_predict_empty_text():
    assert not predict("")
