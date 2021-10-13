# Wprowadzenie do sztucznej inteligencji

Kamil Szczepanik

303782


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
2) Policzenie wartości pochodnej funkcji w x_k
3) Policzenie kolejnego punktu x ze wzoru: x_k+1 = x_k -+ wsp_ucz * d 
    
    gdzie: `d` to policzona wcześniej pochodna. Do liczenia minimum (-), do liczenia maximum (+)

4) Powtarzamy punkty 2) i 3) do momentu aż otrzymamy punkt z zadowalającą dokładnością lub przekroczymy ustalony limit iteracji.

Algorytm dostosowuje wartość skoku kolejnej wartości `x`, w zależności od gradientu dla poprzedniego `x` i wartości współczynnika uczenia

### Wykonane eksperymenty

###### Przyjęto parametry:
- Maksymalna liczba iteracji: 1000
- Zadowalająca dokładność: 0.0001

#### Dla funkcji f(x) = x^2 + 3x + 8 :
###### 1)
- punkt startowy = 0.5
- współczynnik uczenia = 0.1

![](cw1/images/f1_05_01.png )

Wynik:  -1.4999643188076823,
Liczba iteracji:  49

###### 2)
- punkt startowy = 0.5
- współczynnik uczenia = 0.9

![](cw1/images/f1_05_09.png )

Wynik:  -1.5000356811923177,
Liczba iteracji:  49

#### Wnioski:


#### Dla funkcji f(x) = x^4 - 5x^2 - 3x :
###### 1)
- punkt startowy = 0
- współczynnik uczenia = 0.1

![](cw1/images/f2_0_01.png )

Wynik:  1.0393324789193148,
Liczba iteracji:  1000

###### 2)
- punkt startowy = 0
- współczynnik uczenia = 0.2

![](cw1/images/f2_0_02.png )

Wynik:  -1.4120028141545609,
Liczba iteracji:  1000

###### 3)
- punkt startowy = 0
- współczynnik uczenia = 0.01

![](cw1/images/f2_0_001.png )

Wynik:  1.7139370174658386,
Liczba iteracji:  63

###### 4)
- punkt startowy = 0
- współczynnik uczenia = 0.05

![](cw1/images/f2_0_005.png )

Wynik:  1.7139398323504043,
Liczba iteracji:  14

###### 5)
- punkt startowy = -0.5
- współczynnik uczenia = 0.1

![](cw1/images/f2_-05_01.png )

Wynik:  -1.40177304570067,
Liczba iteracji:  12

###### 6)
- punkt startowy = -0.5
- współczynnik uczenia = 0.05

![](cw1/images/f2_-05_005.png )

Wynik:  -1.4017700669801165,
Liczba iteracji:  17

#### Wnioski:





</details>



<details><summary>Ćwiczenie 2</summary>
Do zrobienia
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
