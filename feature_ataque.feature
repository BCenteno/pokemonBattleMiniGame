Feature:ataque1
Scenario: 1.entrenador attacks rival using ataque1
Given i select the pokemon chikorita
When rival select the pokemon bulbasaur
When my pokemon has 100 salud
When rival pokemon has 100 salud
When my pokemon executes atacar
Then rival pokemon has less than 100 salud