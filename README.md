# projekt_2
Zadaniem projektu 2 było utworzenie wtyczki do programu qgis.
Aby wtyczka zadziałała należy wkleić folder projekt_2 do folderu plugins dla programu QGIS np: C:\Users\sokem\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins

Do skorzystania z wtyczki potrzebne będą w qgisie punkty z podanymi wartościmi geometrii x,y,h. 
Po zaimportowaniu punktów należy się upewnić, że współrzędne są odpowiednio onaczone. Żeby wtyczka zadziałała należy zamienić komórki z danymi według podanych kroków:
- w programie Qgis podwójnym kliknięciem na warstwę z danymi żeby otworzyć okno właściwości warstwy. 
- w zakładce Pola na górze uruchomić edycję poprzez kliknięcie na ikonę z ołówkiem i zmienić w kolumnie "Name" poprzez podwójne kliknięcie przy odpowiedniej danej komórkę ze wspoólrzędną x na "X"(bez cudzysłowiu) współrzędną y na "Y" oraz współrzędną z wysokością na "H" i zastosować zmienione dane
Po wprowadzeniu zmian uruchomić wtyczkę na początek zainstalować ją przez wejście do Wtyczki -> Zarządzanie wtyczkami i wyszukanie nazwy "Projekt 2" i klknąć Zainstaluj wtyczkę.
Po zainstalowaniu wtyczka jest gotowa do użycia.
Wykorzystanie jej polega na wyborze odpowiedniej ilości punktów i kliknięcu przycisku do wybranej akcji:
-oblicz wysokość - onlicza różnicę wysokości pomiędzy dwoma punktami
-oblicz pole - oblicza polie figurey utworzonej z danych punktów