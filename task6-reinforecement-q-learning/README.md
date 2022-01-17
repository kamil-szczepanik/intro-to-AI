# Ćwiczenie 6 - Uczenie się ze wzmocnieniem

Zaimplementować algorytm Q-Learning.
Zebrać i przedstawić na wykresie liczbę wykonanych kroków i naliczoną karę/nagrodę w kolejnych epokach.
Problem do rozwiązania to znalezienie drogi z punktu 'S' do punktu 'F' w "labiryncie" / świecie z przeszkodami.
Rezultatem działania algorytmu powinna być ścieżka w postaci: (1,1)->(0,1)->...->(2,3) oraz ww. wykres.

## Algorytm

Algorytm uczenia ze wzmocnieniem opiera się na symulowaniu kolejnych kroków, i w zależności czy jest on porządany czy nie przyznajemy agentowi nagrodę, bądź karę. W przypadku labiryntu nagroda jest przyznawana w momencie dojścia do celu a kara np. w momecie wejścia w ścianę. Następnie na podstawie tego jaka nagroda została przyznana po wykonaniu akcji w danym stanie, aktualizowana jest tabela Q. Ma ona wierszy tyle ile jest stanów w środowiku i kolumn tyle ile jest możliwych akcji. W niej zapisana jest "jakość" (quality) danej akcji w danym stanie. Dzięki temu algorytm "uczy się" na podstawie przeszłych doświadczeń. 

Tabela Q jest aktualizowana według poniższego wzoru:

![](task6-reinforecement-q-learning/images/q_formula.png)

gdzie:

- alpha ( 0 < alpha < 1) to współczynnik uczenia - ustala jak bardzo wartości Q mają się zmieniać
- gamma ( 0 < gamma < 1) współczynnik zniżki - determinuje jak dużo wagi algorytm przywiązuje do przyszłych zniżek, tzn. czy koncentruje się na tym co już wie i w to idzie ( eksploatacja ) czy "zwiedza" przestrzeń stanów aby w przyszłości mieć jak największą nagrodę.

## Implementacja

W pliku [q-learning.ipynb](task6-reinforecement-q-learning/q-learning.ipynb)
znajduje się cała implementacja zadania. Stworzona tam klasa MazeEnv imlpementuje środowisko labiryntu, czyli opisuje stany, nagrody oraz
zawiera funkcję kroku z jednego miejsca na mapie do drugiego.

Do stowrzenia środowiska potrzebna jest mapa dostarczona jako lista z kolejnymi wierszami labiryntu.


# Eksperymenty

Parametry `alpha` i `gamma` udało się dobrać, tak że algorytm z powodzeniem uczy się drogi w labiryncie.

## 1) Mała mapa

Stworzono następującą mapę:

![](task6-reinforecement-q-learning/images/mapa1.png)

##### Parametry: `alpha = 0.1`, `gamma = 0.6`
##### Liczba epok: `1001`

### Wynik nauczonego agenta:

![](task6-reinforecement-q-learning/images/maze.gif)

![](task6-reinforecement-q-learning/images/ex1_result.png)


#### Wykresy liczby wykonanych kroków i naliczonej kary w kolejnych epokach podczas uczenia:

![](task6-reinforecement-q-learning/images/ex1_plot_steps.png)

![](task6-reinforecement-q-learning/images/ex1_plot_penalties.png)

## 2) Duża mapa

Stworzono następującą mapę:

![](task6-reinforecement-q-learning/images/mapa2.png)

##### Parametry: `alpha = 0.1`, `gamma = 0.6`
##### Liczba epok: `1001`

### Wynik nauczonego agenta:

![](task6-reinforecement-q-learning/images/ex2_result.png)


#### Wykresy liczby wykonanych kroków i naliczonej kary w kolejnych epokach podczas uczenia:

![](task6-reinforecement-q-learning/images/ex2_plot_steps.png)

![](task6-reinforecement-q-learning/images/ex2_plot_penalties.png)

# Wnioski

Algorymt działa bardzo dobrze i szybko znajduje optymalną trasę w labiryncie. Praktycznie już przy 500 epoce algorytm już nie popełnia błedów. Nauczony agent bezbłednie przechodzi labirynt. 


