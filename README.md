# Opłaca się? — pliki do pobrania

Aplikacja dla kuriera na Androida: liczy zarobek, godziny, kilometry i paliwo,
a przez pływające kółko ocenia opłacalność ofert z aplikacji kurierskich.

**Aplikacja jest i zostanie darmowa.** W tym repozytorium leży wyłącznie plik
do zainstalowania i instrukcja — kodu źródłowego tu nie ma.

---

## Pobranie i instalacja — krok po kroku

Wszystko robisz na telefonie. Zajmuje to około dwóch minut.

### 1. Pobierz plik

Otwórz na telefonie ten adres i dotknij pliku `.apk` — przeglądarka zapyta,
czy pobrać. Zgódź się.

👉 **[oplaca-sie.apk — pobierz](https://github.com/MichalBaransk/oplaca-sie-wydania/releases/latest/download/oplaca-sie.apk)**

Jeżeli Chrome ostrzeże, że „ten typ pliku może zaszkodzić urządzeniu" —
dotknij **Pobierz mimo to**. To standardowe ostrzeżenie przy każdym pliku
instalacyjnym spoza Sklepu Play.

### 2. Otwórz pobrany plik

Rozwiń pasek powiadomień i dotknij pobranego pliku, albo wejdź w **Moje pliki
→ Pobrane** i dotknij `oplaca-sie.apk`.

### 3. Pozwól na instalację z tego źródła

Android zapyta: *„Ze względów bezpieczeństwa nie możesz instalować nieznanych
aplikacji z tego źródła"*. To pytanie zadaje się **raz**:

1. dotknij **Ustawienia**,
2. przestaw przełącznik **Zezwalaj z tego źródła**,
3. cofnij się i dotknij **Zainstaluj**.

### 4. Zainstaluj

Jeżeli wyskoczy okno Play Protect („nierozpoznana aplikacja") — dotknij
**Zainstaluj mimo to**. Aplikacja nie jest podpisana przez Sklep Play, więc
Android nie ma jej skąd znać.

### 5. Pierwsze uruchomienie

Aplikacja poprowadzi Cię przez wybór języka i zgody. Trzy są **wymagane**,
żeby kółko oceniało oferty:

- **wyświetlanie nad innymi aplikacjami** — bez tego kółko nie ma jak się
  pokazać nad aplikacją kurierską,
- **aplikacja pomocnicza (asystent)** — tym aplikacja czyta ofertę z ekranu,
- **lokalizacja, także w tle** — z tego liczą się kilometry na zmianie.

Reszta (powiadomienia, mikrofon do notatek głosowych, zdjęcia) jest dodatkiem
i można ją włączyć później.

---

## Aktualizacje

**Nie musisz pobierać pliku przy każdej zmianie.** Aplikacja sama pobiera
poprawki po uruchomieniu: pierwsze otwarcie ściąga paczkę w tle, drugie ją
włącza. Wystarczy więc zamknąć i otworzyć aplikację dwa razy.

Nowy plik `.apk` z tej strony jest potrzebny tylko wtedy, gdy napiszę o tym
wprost na kanale — zmieniło się wtedy coś, czego aktualizacja w tle nie
przenosi.

---

## Zanim zainstalujesz na wierzch starszej wersji

Instalacja nowego pliku **na wierzch** zostawia wszystkie Twoje dane.
Odinstalowanie aplikacji **kasuje je bezpowrotnie** — kopii w chmurze nie ma
i to jest celowe: dane nie opuszczają telefonu.

Dlatego przed każdą większą zmianą zrób kopię:
**Więcej → Kopia zapasowa → zapisz plik**.

---

## Czego ta aplikacja nie robi

- **Nie ma serwera.** Wszystko liczy telefon, dane leżą w nim i nigdzie nie są
  wysyłane.
- **Nie zapisuje danych klientów** — ani imienia, ani adresu dostawy, ani
  telefonu. Z ekranu oferty czyta kwotę, kilometry i nazwę lokalu, z którego
  odbierasz.
- **Nie ma reklam, konta ani opłat.**
