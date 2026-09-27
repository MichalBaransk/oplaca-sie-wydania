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

## Czy plik jest prawdziwy?

- **Pobieraj wyłącznie stąd**, z [oplacasie.org](https://oplacasie.org) albo
  z linku na naszym Discordzie. Plik przesłany na grupie czy w wiadomości może
  być podrobiony.
- **Jeśli masz już aplikację**, Android nie zainstaluje na niej pliku
  podpisanego innym kluczem — pokaże błąd o konflikcie z istniejącą aplikacją.
  Nie odinstalowuj wtedy aplikacji, żeby „przejść dalej": to znak, że plik
  nie jest nasz.
- **Odcisk SHA-256 certyfikatu podpisu** jest ten sam przy każdym wydaniu
  (od 8 września 2026):

  ```
  aee052e80dcbae4aa076263bec44eb80273f6b6a470c205e192c8eb642d3387a
  ```

  Sprawdzisz go na komputerze poleceniem
  `apksigner verify --print-certs oplaca-sie.apk` (Android SDK). `keytool`
  go nie pokaże, bo plik ma podpis w nowszym formacie (v2).
- **Każde wydanie podaje na swojej stronie SHA-256 pliku** (od wersji
  następnej po 1.3.0-36). Windows: `certutil -hashfile oplaca-sie.apk SHA256`,
  Linux i macOS: `sha256sum oplaca-sie.apk`.

Przebieg wydania sam sprawdza podpis: plik podpisany innym kluczem niż ten
w `certyfikat.txt` nie zostaje wydany.

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
