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

##### Działanie

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
