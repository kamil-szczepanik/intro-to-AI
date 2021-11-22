## Dwuosobowe gry deterministyczne - gra w kółko i krzyżyk z użyciem algorytmu Minimax

Algorytm minimax jest metodą znajdywania optymalnego ruchu w deterministycznych grach dwuosobowych. Jej ideą jest minimalizowanie maksymalnych możliwych strat. Algorytm odnosi się do teorii gry o sumie zerowej, działając dla gier gdzie gracze wykonują ruchy naprzemiennie albo jednocześnie. Ważnym elementem algorytmu i tego jak działa jest to, że ruch zapewniający największą wypłatę jest wybierany przy założeniu, że przeciwnik gra optymalnie

Algorytm zaimplementowano na podstawie pseudokodu prezentowanego na wykładzie:

![](task3-minimax-tic-tac-toe/images/pseudokod.png )

### Wykonane eksperymenty

 - Graczem max jest X

 - Graczem min jest O

W każdym eksperymencie wykonano 10 symulacji gier.

Zapisana została też ilość stanów przeszukana podczas algorytmu. Dla każdej rundy jest podana wartość, co oznacza, że liczby te dotyczą naprzemiennie gracza min i max.

### Gra pomiędzy dwoma AI minimax

##### 1. Parametry: depth_min = 1, depth_max = 1, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 0 | 10 |

Stany przeszukane w kolejnych rundach:

- 81, 64, 49, 36, 25, 16, 9, 4, 1

##### 2. Parametry: depth_min = 5, depth_max = 5, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 0 | 10 |

Stany przeszukane w kolejnych rundach:

- 73449, 23824, 5227, 1054, 257, 50, 15, 4, 1

#### Obserwacje i wnioski do eksperymentów 1 i 2:

Dla tych samych ustawień głębokości przeszukiwania zawsze wynikiem jest remis. Co więcej, ruchy graczy są zawsze takie same - czyli algorytm jest deterministyczny dla użytych parametrów. W każdej z 10 symulacji przebieg gry był taki sam. Można również zauważyć, że liczba przeszukanych stanów dla głębokości przeszukiwania 5 drastycznie wzrosła, w porównaniu do wielkości z eksperymentu 1.

Algorytm zakłada że przeciwnik gra optymalnie i wyszukuje optymalne rozwiązanie. Ponieważ przeciwnikiem jest ten sam algorytm o tych samych parametrach, obaj gracze grają optymalnie co wynikuje remisem.

##### 3. Parametry: depth_min = 1, depth_max = 5, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 0 | 10 |

Stany przeszukane w kolejnych rundach:

- 73449, 64, 5227, 36, 257, 16, 15, 4, 1

##### 4. Parametry: depth_min = 1, depth_max = 0, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 10 | 0 |

Stany przeszukane w kolejnych rundach:

- 9, 64, 7, 36, 5, 13

#### Obserwacje i wnioski do eksperymentów 3 i 4:

Dla różnych ustawień głębokości przeszukiwania algorytmy i tak wynikami są tylko remisy. Przeszukiwanie z głębią 1 wystarcza aby nie przegrać rozgrywki, algorytm i tak znajduje optymalne zagranie. Możliwe, że jest to spowodowane małą złożonością gry "Kółko i krzyżyk". Prawdopodbnie przykładowo dla szach byłaby tu różnica. Po zmniejszeniu głębokości przeszukiwania do 0, wygrywa zawsze O. Przy głębokości równej 0 algorytm nie przeszukuje możliwych zagrań tylko wybiera najlepsze zagranie na podstawie heurysyki. To jednak nie wystarcza aby obronić się przed minimax, który wybiera zagrania optymalne. Gry wyglądają za każdym razem tak samo - deterministyczność.


**W kolejnych eksperymentach liczba przeszukanych stanów odnosi się tylko do gracza używającego algorytmu**

##### 5. Parametry: Gracz max wybiera ruch losowo, depth_min = 1, zaczyna X

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 9 | 1 |

Stany przeszukane w kolejnych rundach są rózne:
- 64, 36, 13
- 64, 36, 16, 3
- 64, 36, 13, 2

##### 6. Parametry: Gracz max wybiera ruch losowo, depth_min = 1, zaczyna O ( teraz zaczyna algorytm)

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 7 | 3 |

Stany przeszukane w kolejnych rundach są rózne:
- 81, 49, 25, 7, 1
- 81, 49, 21, 9, 1
- 81, 49, 21, 7, 1
- 81, 49, 21, 5, 1
- 81, 49, 21
- ...

##### 7. Parametry: Gracz max wybiera ruch losowo, depth_min = 5, zaczyna O ( teraz zaczyna algorytm)

Wynik:

| Wygrane X | Wygrane O | Remisy |
| ------ | ------ | ------ |
| 0 | 10 | 0 |

Stany przeszukane w kolejnych rundach są rózne:
- 73449, 5227, 105
- 73449, 5227, 144, 7
- 73449, 5227, 149, 3
- 73449, 5335, 181, 6
- 73449, 5335, 161, 11
- ...


#### Obserwacje i wnioski do eksperymentów 5, 6 i 7:
W tych eksperymentach jeden z graczy losował ruch z dostępnych, a drugi korzystał z algorytmu minimax. Wydawałoby się, że minimax powinien sobie dobrze radzić, i rzeczywiście w większości wygrywa ale nie zawsze. Dla głębokości przeszukiwania depth=1, w sytuacji kiedy zaczyna gracz losowy remisów jest mniej niż kiedy zaczyna algorytm. Algorytm zakłada, że przeciwnik gra optymalnie, a losowe ruchy takie nie są, więc algorytm może nie działać - szczególnie dla małej głębokości przeszukiwania. Kiedy jednak ustalono, że depth=5 algortym nie miał problemów z pokonaniem gracza losowego. 
Warto zaznaczyć, że rozgrywki z tych eksperymentów nie były jednakowe. Przeciwnik nie gra optymalnie tylko losowo, zatem dla takich ustawień gra nie jest deterministyczna.

### Podsumowanie
Algorytm minimax jest prostą w implementacji i ciekawą metodą znajdywania optymalnych ruchów w deterministycznych grach dwuosobowych. W grze "Kółko i krzyżyk" głębokość przeszukiwania w rozgrywce między dwoma AI nie miała znaczenia, dopóki jedno z nich było równe 0 - wtedy oczywiście nie ma przeszukiwania tylko wybieranie heurystyczne i gra kończyła się wygraną algorytmu z większą głębokością. W takiej małej grze jak kółko i krzyżyk występuje zaskakująco dużo stanów, które algorytm może rozpatrzyć jeśli ma dużą wartość głębokości przeszukiwania.
