from strategy_pattern.animals import Horse, Human, Lion


def test_herbivore_strategy(capsys):
    horse: Horse = Horse()
    horse.eat()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Eating salad"


def test_carnivore_strategy(capsys):
    lion: Lion = Lion()
    lion.eat()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Eating meat"


def test_omnivore_strategy(capsys):
    human: Human = Human()
    human.eat()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Eating salad with meat"
