from app.matematica import Matematica

def test_somar():
  assert Matematica.somar(1, 1) == 2
  assert Matematica.somar(-1, 1) == 0
  assert Matematica.somar(0, 0) == 0
