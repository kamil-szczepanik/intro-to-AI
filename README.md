# Wprowadzenie do sztucznej inteligencji

_Kamil Szczepanik_

_303782_


## Dokumentacja

<details><summary>Ćwiczenie 1</summary>

### Ćw 1. (7 pkt), data oddania: do 18.10.2021 - Zagadnienie przeszukiwania i podstawowe podejścia do niego

Zaimplementować metodę gradientu prostego dla funkcji jednej zmiennej.
Zbadać działanie metody w zależności od parametrów wejściowych:
- punkt startowy
- współczynnika uczenia

Eksperymenty przeprowadzić dla funkcji z jednym minimum oraz dla funkcji z minimum lokalnym, czyli np.:

    f(x) = x^2 + 3x + 8
    f(x) = x^4 - 5x^2 - 3x


Nie trzeba implementować liczenia pochodnej z funkcji wejściowej - podajemy jako już znaną funkcję,

hint: f(x) i ∇f(x) najlepiej przekazać jako argument funkcji np.:

    # lambda x: x ** 2
    # lambda gx: 2 * gx


#### Rozwiązanie

Metoda gradientu prostego dla funkcji zmiennej pozwala znaleźć jej minumum lub maximum lokalne. Algorytm jest następujący:
1) Wybranie punktu startowego (x_k) oraz współczynnika uczenia
2) Policzenie wartości pochodnej funkcji w x_k czyli gradientu
3) Policzenie kolejnego punktu x ze wzoru: x_k+1 = x_k -+ wsp_ucz * d 
    
    gdzie: `d` to gradient. Do liczenia minimum (-), do liczenia maximum (+)

4) Powtarzamy punkty 2) i 3) do momentu aż otrzymamy punkt z zadowalającą dokładnością lub przekroczymy ustalony limit iteracji.

Algorytm dostosowuje wartość skoku kolejnej wartości `x`, w zależności od gradientu dla poprzedniego `x` i wartości współczynnika uczenia

W pliku `przeszukiwanie.py` znajduje się implementacja zadania. 

### Wykonane eksperymenty

###### Przyjęto parametry:
- Maksymalna liczba iteracji: 1000
- Zadowalająca dokładność: 0.0001

#### Dla funkcji f(x) = x^2 + 3x + 8 :
##### 1)
- punkt startowy = 0.5
- współczynnik uczenia = 0.1

![](task1/images/f1_05_01.png )

Wynik:  -1.4999643188076823,
Liczba iteracji:  49

##### 2)
- punkt startowy = 0.5
- współczynnik uczenia = 0.9

![](task1/images/f1_05_09.png )

Wynik:  -1.5000356811923177,
Liczba iteracji:  49

#### Obserwacje
Dla funkcji kwadratowej algorytm działał prawidłowo. Wartości kolejnych x zbiegały do rozwiązania w obu przypadkach wielkości współczynnika uczenia.

#### Dla funkcji f(x) = x^4 - 5x^2 - 3x :
##### 1)
- punkt startowy = 0
- współczynnik uczenia = 0.1

![](task1/images/f2_0_01.png )

Wynik:  1.0393324789193148,
Liczba iteracji:  1000

##### 2)
- punkt startowy = 0
- współczynnik uczenia = 0.9

**OverflowError: (34, 'Numerical result out of range')**

Wartość pochodnej rośnie do nieskończoności - złe parametry

##### 3)
- punkt startowy = 0
- współczynnik uczenia = 0.2

![](task1/images/f2_0_02.png )

Wynik:  -1.4120028141545609,
Liczba iteracji:  1000

##### 4)
- punkt startowy = 0
- współczynnik uczenia = 0.01

![](task1/images/f2_0_001.png )

Wynik:  1.7139370174658386,
Liczba iteracji:  63

##### 5)
- punkt startowy = 0
- współczynnik uczenia = 0.05

![](task1/images/f2_0_005.png )

Wynik:  1.7139398323504043,
Liczba iteracji:  14

##### 6)
- punkt startowy = -0.5
- współczynnik uczenia = 0.1

![](task1/images/f2_-05_01.png )

Wynik:  -1.40177304570067,
Liczba iteracji:  12

##### 7)
- punkt startowy = -0.5
- współczynnik uczenia = 0.05

![](task1/images/f2_-05_005.png )

Wynik:  -1.4017700669801165,
Liczba iteracji:  17

#### Obserwacje
Dla eksperymentów 1), 2) i 3) algorytm nie zadziałał- minimum lokalne nie zostało osiągnięte. Jest to spowodowane zbyt dużą wartością współczynnika uczenia oraz samą charakterystyką wielomianu, ponieważ osiąga on bardzo różne wartości w stosunkowo niewielkim przedziale x. 
W eksperymentach 4) i 5) dobrano współczynnik uczenia taki, że minimum lokalne zostało osiągnięte. W eksperymencie 4) rozwiązanie zostało znalezione już po 14 iteracjach.
W eksperymentach 6) i 7) nieco przesunięto punkt startowy, co spowodowało znalezienie innego minima lokalnego.

#### Wnioski
Algorytm działa poprawnie dla dobrze dobranych parametrów. 

Należy dobrze wybrać punkt startowy oraz być świadomym, że w zależności od jego wartości algorytm znajduje inne rozwiązania (dla wielomianów o stopniu większym niż 2). Punkt startowy musi być także w takim miejscu, aby rozwiązanie nie zbiegało do +-nieskończoności (chyba, że damy wystarczająco mały współczynnik uczenia). 

Innym bardzo ważnym parametrem jest współczynnik uczenia. Dla funkcji większego stopnia współczynnik powinien być raczej mały (około 0.01-0.1). Można go oszacować na podstawie charakterystyki funkcji. Jeżeli występują w niej (nawet na oko) duże gradienty to lepiej dać ten współczynnik mały.

Chodzi o to, żeby iloczyn gradientu i współczynnika uczenia był na tyle mały aby nie spowodował niestabiloności w wyszukiwaniu. Jeżeli ten iloczyn będzie na tyle duży, że w następnym kroku algorytm znajdzie gradient większy od poprzedniego to możemy nie znaleźć optiumum lokalnego.

</details>



<details><summary>Ćwiczenie 2</summary>

## Algorytm ewolucyjny
Algorytm ewolucyjny dla problemu minimalizacji funkcji n-zmiennych. W algortmie zastosowano selekcję turniejową oraz sukcjesję elitarną.
Implementacje wykonano na podstawie pseudokodu przedstawionego na wykładzie:

![](task2/images/pseudokod.png )

Parametrami pragramu są:
- Liczba iteracji
- Wielkość populacji inicjalnej
- Rozmiar turnieju
- Rozmiar elity
- Siła mutacji
- Prawdopodobieństwo mutacji
- Funkcja celu - jako minimalizacje pewnej funkcji

### Eksperymenty:
Funkcja, na której testowano algorytm to Bird Function

![](task2/images/bird_formula.png )

![](task2/images/bird.png )

Jest  to dobra funkcja na testowanie przeszukujących algorytmów, ponieważ ma kilka minimów, w tym dwa optima globalne:
f(x)=−106.764537 ulokowane w x=(4.70104 ,3.15294) oraz x=(−1.58214 ,−3.13024)



#### Zależność wartości funkcji celu od wielkości populacji:
Parametry funkcji
- pop_arg_num = 2
- tournament_size = 2
- elite = 1
- sigma = 0.1
- mutation_prob = 0.5
- function_to_minimize = bird_function

![](task2/images/pop_size1.png )

![](task2/images/pop_size2.png )

Na powyższych wykresach widać, że funcja celu maleje dla każdej wielkości populacji. Dodatkowo robi to całkiem szybko bo już po kilku iteracjach algorytm znajduje przybliżone rozwiązanie. Widać jednak, że populacja wielkości 10 może czasem nie wystarczyć na znalezienie rozwiązania - algorytm
utyka w minimum lokalnym i pozostaje tam do końca trwania programu.

#### Zależność wartości funkcji celu od siły mutacji (sigma):
Parametry:
- pop_size = 50
- pop_arg_num = 2
- tournament_size = 2
- elite = 1
- mutation_prob = 0.5
- function_to_minimize = bird_function

![](task2/images/sigma1.png )

![](task2/images/sigma2.png )

![](task2/images/sigma3.png )

Sigma = 0.1 - W większości eksperymentów taka sigma była wystarczająca. Algorytm zbiega do rozwiązania. Czasami jednak dla tej wartości siły 
mutacji algorytm utyka w jednym z minimów lokalnych i nie udaje mu się stamtąd wydostać.

Sigma = 0.5 - Wydaje się być optymalną wartością siły mutacji. W jednym z eksperymentów bardzo dobre rozwiązanie zostało znalezione już w drugiej iteracji.

Sigma = 2 - Na pierwszej ilustracji można zauważyć, że algorymt dla sigmy = 2 jest mocno niestabilny i "skacze" po przeszukiwanej przestrzeni.
W końcu jednak znajduje minimum globalne. W innych przypadkach funkcja celu dla takie siły mutacji również szybko znajduje dobre rozwiazanie. Duża wartość sigmy zapobiega nadmiernej eksploatacji i pozwala na lepszą eksplorację.

#### Zależność wartości funkcji celu od rozmiaru elity:
Parametry:
- t_max = 20
- pop_size = 100
- pop_arg_num = 2
- tournament_size = 2
- elite = 1
- sigma = 0.1
- mutation_prob = 0.5

![](task2/images/elite1.png )

![](task2/images/elite2.png )

Sukcjesja elitarna jest dobrą metodą na pozostawienie dobrych osobników z poprzedniej iteracji. Na wykresach widać, że mała elita jest wystarczajaco dobra. Elita = 10 wypada jednak tak samo dobrze jeśli nie lepiej. Dla dużej wielkości elity, czasem algorytm znajdzie minimum lokalne i będzie się niego przez pewnien czas trzymał, tzn. nawet jeśli będzie znajdywał pojedyńcze lepsze osobniki to przez kolejne iteracje w elicie wciąż będą osobniki z minimum lokalnego, które będą hamowały znalzienie rozwiązania. Taką sytuację przedstawia pierwsza ilustacja.


</details>

<details><summary>Ćwiczenie 3</summary>
Do zrobienia
</details>

<details><summary>Ćwiczenie 4</summary>
Do zrobienia
</details>

<details><summary>Ćwiczenie 5</summary>
Do zrobienia
</details>
