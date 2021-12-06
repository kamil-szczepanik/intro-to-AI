# Naiwny klasyfikator Bayesa (Gaussowski)

Naiwny klasyfikator Bayesa to prosty klasyfikator probabilistyczny. Jest to rodzina algortmów, których wspólną regułą jest wzajemna niezależność predyktorów ( zmiennych niezależnych ). Często nie mają one żandego związku z rzeczywistością i właśnie z tego powodu nazywa się je naiwnymi. Bardziej opisowe jest określenie - "model cech niezależnych". Naiwny klasyfikator Bayesa opiera się na twierdzeniu Bayesa.

Gaussowski naiwny klasyfikator Bayesa opiera się na założeniu, że dane związane z klasą są rozłożone zgodnie z rozkładem normalnym ( Gaussa ). prawdopodobieństwo jest liczone ze wzoru:

![](task4-naive-bayes-classifier/images/probability_density_function_gauss.jpg)


## Zadanie: 
Zaimplementować naiwny klasyfikator Bayesa (Gaussowski).
Do eksperymentów wykorzystać zbiór danych dot. jakości wina.
Do weryfikacji jakości modelu wykorzystać:
 - k-krotną walaidację krzyżową (k=5)
 - oraz podział na zbiór treningowy i testowy (60/40)

Do eksperymentów użyte zostały dane o winie czerwonym. Jest to zbiór danych wielkości około 1500 zapisów dotyczących właściwości wina. Klasami, do których dane były klasyfikowane była cecha jakości wina ( quality ). Klasyfikator miał na podstawie danych o winie przyporządkować mu jakość.


### Implementacja

W implementacji użyto bibliotekę `pandas`, służącą do manipulacji i analizy danych. Dzięki niej można łatwo wczytać dane i wydobyć z nich potrzebne informacje. Bibliotekę tą użyto w celu grupowania danych od klas, podstawowych obliczeń oraz liczenia średniej i odchylenia standardowego cech wina. W celu policzenia prawdopodobieństwa użyto biblioteki `scipy.stats`, której funkcja `norm.pdf()` oblicza prawdopodobieństwo według wyżej wymienionego wzoru.

W pliku [classifier.ipynb](task4-naive-bayes-classifier/classifier.ipynb) znajduje się implementacja klasyfikatora oraz przeprowadzone eksperymenty.

#### Miara oceny jakości klasyfikatora
Do oceny jakości klasyfikatora wybrano dokładność ( accuracy ), czyli stosunek liczby poprawnych predykcji do liczby danych testowych ( liczba danych, dla których predykcji była robiona). Jest do dobra metoda sprawdzania jakości modelu, ponieważ jest intuicyna, łatwa w implementacji oraz dostarcza wystarczającą ocenę.

### Eksperymenty
#### k-krotna walidacja krzyżowa
Dla k-krotnej walidacji krzyżowej należy przeprowadzić tylko jeden eksperyment, ponieważ dane są dzielone w zawsze taki sam sposób ( nie ma tasowania danych przed podziałem ).

Wynik:
```
    accuracy = 0.5253663793103448
```
#### Prosty podział na zbiór treningowy i testowy
Dla tej metody walidacji wykonano trzy eksperymenty i każdy z nich dał inny rezultat. Jest tak, ponieważ za każdym razem zbiór treningowy i testowy jest inny ( są losowane ), jednak ich stosunek jest taki sam i równy 60/40 (treningowy/testowy).

1) Wynik:
```
    accuracy =  0.4609375
```
2) Wynik:
```
    accuracy = 0.5640625
```
3) Wynik:
```
    accuracy = 0.5828125
```
Jak widać wyniki eksperymentów bardzo się różnią. Ciężko stwierdzić jaka jest dokładność modelu na prawdę.
### Wyniki

| k-krotna walidacja krzyżowa ( k = 5 ) | Prosty podział na zbiór treningowy i testowy |
| ------ | ------ |
| accuracy = 0.5253663793103448 | accuracy =  0.4609375 |
| - | accuracy = 0.5640625 |
| - | accuracy = 0.5828125 |


### Pytania:
##### Jakiego podzbioru danych (z tych którymi dysponujemy) użyjemy do zbudowania docelowego modelu na potrzeby klasyfikowania nowych próbek (czyli dla tych dla których budujemy klasyfikator)?

 - **Dla walidacji z prostym podziałem danych na zbiór treningowy i testowy**, do budowy docelowego modelu należy użyć **tylko zbiór treningowy**. Jest to konieczne, ponieważ walidację należy przeprowadzać na danych, które "nie widziały" danych treningowych. Chodzi o to, aby nie sprawdzać modelu na danych, na których model się uczyło. W ten sposób ominięty zostanie problem nadmiernego dopasowania ( overfitting ).

 - **Dla k-krotnej walidacji krzyżowej** dane, do budowy docelowego modelu używane są **wszystkie dane lecz "nie wszystkie na raz"**. Po podzieleniu danych na _k_ podzbiorów, zbiór treningowy to wszystkie podzbiory oprócz jednego, a zbiór testowy to ten jeden podzbiór, którego nie ma w zbiorze treningowym. Takich par zbiorów treningowych i testowych będzie _k_. Na każdej takiej parze model jest budowany i weryfikowany, co w rezultacie oznacza, że wszystkie dane zostaną użyte do zbudowania modelu.

##### Jak zinterpretować różnice/brak różnic w wynikach z weryfikacji jakości modelu obu metod (k-krotna walidacja vs zbiór treningowy i testowy)
 - Dużą różnicą tych metod weryfikacji modelu jest to, że w k-krotnej walidacji otrzymujemy jeden wynik, a w prostym podziale otrzymujemy inny wynik w każdym wywołaniu. Wnioskiem tego jest to, że dla prostego podziału nie możemy jednoznacznie stwierdzić jaka jest jakość modelu, a dla k-krotnej walidacji już tak i jest to bardziej miarodajna metoda.


