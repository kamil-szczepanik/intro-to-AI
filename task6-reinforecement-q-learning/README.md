# Ćwiczenie 6 - Uczenie się ze wzmocnieniem

Zaimplementować algorytm Q-Learning.
Zebrać i przedstawić na wykresie liczbę wykonanych kroków i naliczoną karę/nagrodę w kolejnych epokach.
Problem do rozwiązania to znalezienie drogi z punktu 'S' do punktu 'F' w "labiryncie" / świecie z przeszkodami.
Rezultatem działania algorytmu powinna być ścieżka w postaci: (1,1)->(0,1)->...->(2,3) oraz ww. wykres.

## Algorytm

Algorytm uczenia ze wzmocnieniem opiera się na symulowaniu kolejnych kroków, i w zależności czy jest on porządany czy nie przyznajemy agentowi nagrodę, bądź karę. W przypadku labiryntu nagroda jest przyznawana w momencie dojścia do celu a kara np. w momecie wejścia w ścianę. Następnie na podstawie tego jaka nagroda została przyznana po wykonaniu akcji w danym stanie, aktualizowana jest tabela Q. Ma ona wierszy tyle ile jest stanów w środowiku i kolumn tyle ile jest możliwych akcji. W niej zapisana jest "jakość" (quality) danej akcji w danym stanie. Dzięki temu algorytm "uczy się" na podstawie przeszłych doświadczeń. 

## Implementacja

W pliku [q-learning.ipynb](https://gitlab-stud.elka.pw.edu.pl/kszczep4/wsi-21z/-/blob/main/task6-reinforecement-q-learning/q-learning.ipynb)
znajduje się cała implementacja zadania. Stworzona tam klasa MazeEnv imlpementuje środowisko labiryntu, czyli opisuje stany, nagrody oraz
zawiera funkcję kroku z jednego miejsca na mapie do drugiego.

Do stowrzenia środowiska potrzebna jest mapa dostarczona jako lista z kolejnymi wierszami labiryntu.

