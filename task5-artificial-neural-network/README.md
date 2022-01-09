### Zespół:
**Piotr Hondra**

**Kamil Szczepanik 303782**

# Ćw 5. - Sztuczne sieci neuronowe

Zaimplementować sztuczną sieć neuronową z warstwą ukrytą.
Implementacja powinna być elastyczna na tyle, żeby można było zdefiniować liczbę neuronów wejściowych, ukrytych i wyjściowych.
Wykorzystać sigmoidalną funkcję aktywacji i do trenowania użyć wstecznej propagacji błędu z użyciem metody stochastycznego najszybszego spadku.
Sieć nauczyć rozpoznawać jakość wina jak w ćwiczeniu 4. i porównać wyniki z otrzymanymi poprzednio.
Na wykresie pokazać jak zmieniał się błąd uczonej sieci w kolejnych epokach.
Poeksperymentować ze współczynnikiem uczenia oraz liczbą epok.

## Implementacja

Zadanie zaimplementowano tworząc klasę sieci nueronowej oraz klasy warstw - fully connected i aktywacji. Dzięki temu możliwe jest łatwe dodawanie warstw oraz zmiana parametrów takich jak liczbe neuronów wejściowych, ukrytych i wyjściowych. W klasie warstwy zaimplementowana jest propagacja w przód i wsteczna. W klasie sieci neuronowej najważniejsza metodą jest `fit()`. Wywołuje ona uczenie sieci według podanych parametrów, takich jak liczba epok czy współczynnik uczenia. Aby poprawić jakość uczenia, zastosowano standaryzacje.

Implementacje zadania oraz eksperymenty znajdują się w pliku [neural_network.ipynb](neural_network.ipynb)

## Eksperymenty

**Wykresy przedstawiają jak zmieniał się błąd w uczonej sieci**

### 1. Liczba neuronów ukrytych = 50, liczba epok = 500 , współczynnik uczenia = 0.1

| test accuracy | train accuracy | error |
| ------------- | -------------- | ----- |
| 0.610938 | 0.839416 | 0.045849 |


![](/images/experiment1.png)

### 2. Liczba neuronów ukrytych = 50, liczba epok = 500 , współczynnik uczenia = 0.4

| test accuracy | train accuracy | error |
| ------------- | -------------- | ----- |
| 0.603125 | 0.932221 | 0.017000 |


![](/images/experiment2.png)

### 3. Liczba neuronów ukrytych = 50, liczba epok = 500, współczynnik uczenia = 0.05

| test accuracy | train accuracy | error |
| ------------- | -------------- | ----- |
| 0.604688 | 0.755996 | 0.063980 |


![](/images/experiment3.png)

### 4. Liczba neuronów ukrytych = 50, liczba epok: 2000, współczynnik uczenia = 0.05

| test accuracy | train accuracy | error |
| ------------- | -------------- | ----- |
| 0.6046875 | 0.93534 | 0.021004 |


![](/images/experiment4.png)

### 5. Liczba neuronów ukrytych = 100, liczba epok: 2000, współczynnik uczenia = 0.05

| test accuracy | train accuracy | error |
| ------------- | -------------- | ----- |
| 0.5828125 | 0.9457768508863399 | 0.016521 |


![](/images/experiment5.png)

### 6. Liczba neuronów ukrytych = 1000, liczba epok: 2000, współczynnik uczenia = 0.05

| test accuracy | train accuracy | error |
| ------------- | -------------- | ----- |
| 0.571875 | 0.89676 | 0.018868 |


![](/images/experiment6.png)

## Porównanie eksperymentów
| test_acc 	| train_acc 	| epochs 	| learning_rate 	| hidden_neurons 	|
|----------	|-----------	|--------	|---------------	|----------------	|
| 0.61     	| 0.84      	| 500    	| 0.1           	| 50             	|
| 0.60     	| 0.93      	| 500    	| 0.4           	| 50             	|
| 0.60     	| 0.76      	| 500    	| 0.05          	| 50             	|
| 0.60     	| 0.94      	| 2000   	| 0.05          	| 50             	|
| 0.58     	| 0.95      	| 2000   	| 0.05          	| 100            	|
| 0.57     	| 0.90      	| 2000   	| 0.05          	| 1000           	|

### Obserwacje
- Wraz ze zwiększaniem liczby epok, liczby neuronów w warstwie ukrytej wydłuża się czas uczenia.
- Zwiększanie liczby neuronów w warstwie ukrytej powoduje zwiększenie ilości stopni swobody modelu, przez co może lepiej dopasowywać się do danych trenujących
- Inicjalizacja wag tymi samymi liczbami skutkuje brakiem możliwości uczenia sieci.
- Dokładność na zbiorze testowym rośnie, a potem utrzumuje się lub spada.
- Po pewnej liczbie epok dokładność na zbiorze testowym rośnie, a potem utrzumuje się lub spada, a dokładność na zbiorze treningowy cały czas rośnie.
- Standaryzacja danych pozwala osiągnać dużo lepsze wyniki.

### Wnioski
- Perceptron wielowarstwowy z jedną warstwą ukrytą może aproksymować dowolnie nieliniową funkcję z dowolną dokładności, co skutkuje łatwością przeuczenia.
- Należy odpowiednio inicjalizować wagi.
- Zbyt dużu liczba epok prowadzi do przeuczenia, zbyt mała do niedouczenia.
- Zbyt duży krok uczenia prowadzi skutkuje brakiem zbieżności, natomiast zbyt mały znacząco wydłuża proces uczenia.
- Warto zastosować early stopping, gdy błąd na zbiorze walidacyjnym utrzymuje się przez określona liczbę epok, co poprawi czas uczenia i zmniejszy przeuczenie.



## Porównanie z naiwnym klasyfikatorem Bayesa

Porównanie wartości accuracy dwóch klasyfiktorów przedstawiono w tabeli. Wynik naiwnego klasyfikatora Bayesa jest rezultatem 5-krotnej walidacji krzyżowej. Wynik sieci neuronowej to najlepszy uzyskany wynik z powyższych eksperymentów.

| Naiwny klasyfikator Bayesa | Sieć neuronowa  |
| ------------- | -------------- |
| 0.5568 | 0.610938 |

Zgodnie z oczekiwaniami naiwny klasyfikator Bayesa osiąga gorszą dokładność od perceptronu wielowarstowego z jedna warstwą ukrytą. Uważamy, że wynika to m.in. z niespełnienia założeń klasyfikatora Bayesa (niezależność liniowa atrybutów/rokzład normalny atrybutów).





