
## Algorytm ewolucyjny
Algorytm ewolucyjny dla problemu minimalizacji funkcji n-zmiennych. W algortmie zastosowano selekcję turniejową oraz sukcjesję elitarną.
Implementacje wykonano na podstawie pseudokodu przedstawionego na wykładzie:

![](task2-evolutionary_algorithm/images/pseudokod.png )

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

![](task2-evolutionary_algorithm/images/bird_formula.png )

![](task2-evolutionary_algorithm/images/bird.png )

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

![](task2-evolutionary_algorithm/images/pop_size1.png )

![](task2-evolutionary_algorithm/images/pop_size2.png )

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

![](task2-evolutionary_algorithm/images/sigma1.png )

![](task2-evolutionary_algorithm/images/sigma2.png )

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

![](task2-evolutionary_algorithm/images/elite1.png )

![](task2-evolutionary_algorithm/images/elite2.png )

Sukcjesja elitarna jest dobrą metodą na pozostawienie dobrych osobników z poprzedniej iteracji. Na wykresach widać, że mała elita jest wystarczajaco dobra. Elita = 10 wypada jednak tak samo dobrze jeśli nie lepiej. Dla dużej wielkości elity, czasem algorytm znajdzie minimum lokalne i będzie się niego przez pewnien czas trzymał, tzn. nawet jeśli będzie znajdywał pojedyńcze lepsze osobniki to przez kolejne iteracje w elicie wciąż będą osobniki z minimum lokalnego, które będą hamowały znalzienie rozwiązania. Taką sytuację przedstawia pierwsza ilustacja.


##### 1) Animacja znajdywania rozwiązania w kolejnych pokoleniach:
Parametry:
- t_max = 10
- pop_size = 20
- pop_arg_num = 2
- tournament_size = 2
- elite = 1
- sigma = 0.1
- mutation_prob = 0.5
- function_to_minimize = bird_function

![](task2-evolutionary_algorithm/images/gif1.gif )


##### 2) Animacja znajdywania rozwiązania w kolejnych pokoleniach:
Parametry:
- t_max = 10
- pop_size = 50
- pop_arg_num = 2
- tournament_size = 4
- elite = 10
- sigma = 0.1
- mutation_prob = 0.1
- function_to_minimize = bird_function

![](task2-evolutionary_algorithm/images/gif3.gif )

W tym doświadczeniu algorytm pozostał nieco dłużej w minimum lokalnym. Jest tak za sprawą dużego rozmiaru elity, który zmniejsza eksploracje w poszukiwaniu lepszego rozwiązania. Małe prawdopodobieństwo oraz siła mutacji (sigma) również sprawiają, że różnorodność osobników nie jest duża, co spowalnia znalezienie optimum globalnego.


#### Populacja początkowa: losowa i klony:

Doświadczenie 1)

![](task2-evolutionary_algorithm/images/klon1.png )

Doświadczenie 2)

![](task2-evolutionary_algorithm/images/klon2.png )

Na pierwszej ilustracji widać, że algorytm z początkową populacją złożoną z takich samych osobników działa o wiele wolniej niż z osobnikami losowymi. Z kolei w drugim doświadczeniu algorytm z klonami zatrzymał się w minimum lokalnym, prawdopodobnie dlatego, że populacja początkowa znajdowała się blisko tego minimim lokalnego.

##### Animacja znajdywania rozwiązania z populacją początkową z klonami
Pokolenia: 1, 5, 10, 15, 20, 25, 30, 35

![](task2-evolutionary_algorithm/images/gif4.gif )

W powyższym przypadku algorytm nie zatrzymuje się w minimum lokalnym i znajduje optimum globalne.

### Podsumowanie
Algorytm ewolucyjny daje różne wyniki w zależności od wybranych parametrów oraz z samej losowości tego algorytmu. Parametry takie jak siła mutacji (sigma), prawdopodobieństwo mutacji, rozmiar turnieju, rozmiar elity wpływają na to czy algorytm ma charakter bardziej eksploracyjny czy eksploatacyjny. Dobrze gdy populacja jest odpowiednio duża, gdyż zwiększa to szansę na znalezienie optimum globalnego. Populacja początkowa złożona z różnorodnych osobników daje lepsze efekty pod względem rozwiązania i szybkości działania. Dla tych samych parametrów algorytm może znaleźć zupełnie różne rozwiązania - wynika to z wielu losowych kroków takich jak: inicjalizacja losowej populacji początkowej, losowy dobór uczestników turnieju, losowa mutacja osobników. Mimo tego, funkcja celu maleje w każdym przeprowadzonym doświadczeniu. Aby otrzymać optymalne rozwiązanie, najlepiej dla pewności włączyć algorytm kilka razy.


