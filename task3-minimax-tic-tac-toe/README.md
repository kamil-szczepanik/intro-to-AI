
### Dwuosobowe gry deterministyczne - gra w kółko i krzyżyk z użyciem algorytmu Minimax

Algorytm minimax jest metodą znajdywania optymalnego ruchu w deterministycznych grach dwuosobowych. Jej ideą jest minimalizowanie maksymalnych możliwych strat. Algorytm odnosi się do teorii gry o sumie zerowej, działając dla gier gdzie gracze wykonują ruchy naprzemiennie albo jednocześnie. Ważnym elementem algorytmu i tego jak działa jest to, że ruch zapewniający największą wypłatę jest wybierany przy założeniu, że przeciwnik gra optymalnie

Algorytm zaimplementowano na podstawie pseudokodu prezentowanego na wykładzie:

![](task3-minimax-tic-tac-toe/images/pseudokod.png )

#### Wykonane eksperymenty

 - Graczem max jest X

 - Graczem min jest O

W każdym eksperymencie wykonano 10 symulacji gier.

Zapisane zostały

##### Gra pomiędzy dwoma AI minimax

###### 1. Parametry: depth_min = 1, depth_max = 1, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 0 | 10 |

Stany przeszukane w kolejnych rundach:

- 81, 64, 49, 36, 25, 16, 9, 4, 1

###### 2. Parametry: depth_min = 5, depth_max = 5, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 0 | 10 |

Stany przeszukane w kolejnych rundach:

- 73449, 23824, 5227, 1054, 257, 50, 15, 4, 1

#### Obserwacje i wnioski:

Dla tych samych ustawień głębokości przeszukiwania zawsze wynikiem jest remis. Co więcej, ruchy graczy są zawsze takie same - czyli algorytm jest deterministyczny dla użytych parametrów. W każdej z 10 symulacji przebieg gry był taki sam. Można również zauważyć, że liczba przeszukanych stanów dla głębokości przeszukiwania 5 drastycznie wzrosła, w porównaniu do wielkości z eksperymentu 1.

Algorytm zakłada że przeciwnik gra optymalnie i wyszukuje optymalne rozwiązanie. Ponieważ przeciwnikiem jest ten sam algorytm o tych samych parametrach, obaj gracze grają optymalnie co wynikuje remisem.

###### 3. Parametry: depth_min = 1, depth_max = 5, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 0 | 10 |

Stany przeszukane w kolejnych rundach:

- 73449, 23824, 5227, 1054, 257, 50, 15, 4, 1

###### 4. Parametry: depth_min = 1, depth_max = 0, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 10 | 0 |

Stany przeszukane w kolejnych rundach:

- 9, 64, 7, 36, 5, 13

#### Obserwacje i wnioski:

Dla tych samych ustawień głębokości przeszukiwania zawsze wynikiem jest remis. Co więcej, ruchy graczy są zawsze takie same - czyli algorytm jest deterministyczny dla użytych parametrów. W każdej z 10 symulacji przebieg gry był taki sam. Można również zauważyć, że liczba przeszukanych stanów dla głębokości przeszukiwania 5 drastycznie wzrosła, w porównaniu do wielkości z eksperymentu 1.

Algorytm zakłada że przeciwnik gra optymalnie i wyszukuje optymalne rozwiązanie. Ponieważ przeciwnikiem jest ten sam algorytm o tych samych parametrach, obaj gracze grają optymalnie co wynikuje remisem.


