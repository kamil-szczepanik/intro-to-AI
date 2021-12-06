# Naiwny klasyfikator Bayesa (Gaussowski)

Naiwny klasyfikator Bayesa to prosty klasyfikator probabilistyczny. Jest to rodzina algortmów, których wspólną regułą jest wzajemna niezależność predyktorów ( zmiennych niezależnych ). Często nie mają one żandego związku z rzeczywistością i właśnie z tego powodu nazywa się je naiwnymi. Bardziej opisowe jest określenie - "model cech niezależnych". Naiwny klasyfikator Bayesa opiera się na twierdzeniu Bayesa.


## Zadanie: 
Zaimplementować naiwny klasyfikator Bayesa (Gaussowski).
Do eksperymentów wykorzystać zbiór danych dot. jakości wina.
Do weryfikacji jakości modelu wykorzystać:
 - k-krotną walaidację krzyżową (k=5)
 - oraz podział na zbiór treningowy i testowy (60/40)

Do eksperymentów użyte zostały dane o winie czerwonym. Jest to zbiór danych wielkości około 1500 zapisów dotyczących właściwości wina. Klasami, do których dane były klasyfikowane była cecha jakości wina ( quality ). Klasyfikator miał na podstawie danych o winie przyporządkować mu jakość.




### Pytania:
**Jakiego podzbioru danych (z tych którymi dysponujemy) użyjemy do zbudowania docelowego modelu na potrzeby klasyfikowania nowych próbek (czyli dla tych dla których budujemy klasyfikator)?**

Dla walidacji z prostym podziałem danych na zbiór treningowy i testowy, do budowy docelowego modelu należy użyć **tylko zbiór treningowy**. Jest to konieczne, ponieważ walidację należy przeprowadzać na danych, które "nie widziały" danych treningowych. Chodzi o to, aby nie sprawdzać modelu na danych, na których model się uczyło. W ten sposób ominięty zostanie problem nadmiernego dopasowania ( overfitting ).

Dla k-krotnej walidacji krzyżowej dane, do budowy docelowego modelu używane są wszystkie dane lecz "nie wszystkie na raz". Po podzieleniu danych na k podzbiorów, zbiór treningowy to wszystkie podzbiory oprócz jednego, a zbiór testowy to ten jeden podzbiór, którego nie ma w zbiorze treningowym. Takich par zbiorów treningowych i testowych będzie k. Na każdej takiej parze model jest budowany i weryfikowany, co w rezultacie oznacza, że wszystkie dane zostaną użyte do zbudowania modelu.



**Jak zinterpretować różnice/brak różnic w wynikach z weryfikacji jakości modelu obu metod (k-krotna walidacja vs zbiór treningowy i testowy)**

### Podsumowanie


