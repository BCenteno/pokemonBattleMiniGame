Feature:curacion
Scenario: 1.damaged pokemon gets healed
Given i select the pokemon bulbasaur
When my pokemon has 50 salud
And my pokemon executes curar
Then my pokemon has more than 50 salud

Scenario: 2.damaged pokemon gets healed
Given i select the pokemon bulbasaur
When my pokemon has 80 salud
And my pokemon executes curar
Then my pokemon has more than 50 salud

Scenario: 3.damaged pokemon gets healed
Given i select the pokemon charmander
When my pokemon has 70 salud
And my pokemon executes curar
Then my pokemon has more than 70 salud

Scenario: 4.damaged pokemon gets healed
Given i select the pokemon noexiste
When my pokemon has 80 salud
And my pokemon executes curar
Then my pokemon has more than 50 salud