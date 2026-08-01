# Skill: GitHub Repo Organizer

## Cel skillu

Pomagać w porządkowaniu repozytoriów GitHub i lokalnych repozytoriów bez chaotycznych zmian, bez kasowania danych i bez mieszania ról projektów.

Skill prowadzi do jasnej odpowiedzi:

- które repo do czego służy,
- co jest aktywne, testowe, biznesowe, archiwalne albo pomocnicze,
- gdzie są duplikaty,
- co powinno zostać przeniesione dopiero po decyzji użytkownika,
- czego nie trzymać w repozytorium.

## Kiedy używać

Używać, gdy zadanie dotyczy:

- mapy repozytoriów,
- porządkowania lokalnych repo i repo GitHub,
- struktury folderów,
- wykrywania duplikatów plików, skilli, promptów lub dokumentacji,
- rozdzielania repozytoriów według przeznaczenia,
- archiwizacji,
- decyzji, które repo jest głównym centrum pracy,
- oceny, czy repo nie zawiera rzeczy, których nie powinno zawierać.

## Dane wejściowe

- lista repozytoriów albo katalogów,
- ścieżki lokalne,
- linki do repo GitHub,
- obecna struktura folderów,
- lista skilli, promptów i dokumentacji,
- cel biznesowy projektu,
- informacja, które repo jest aktywne,
- ograniczenia użytkownika.

Jeśli brakuje danych, oznaczyć brak jako `DO DECYZJI`, zamiast zgadywać.

## Zakres analizy

Analizować:

- rolę każdego repozytorium,
- dublowanie plików, skilli, promptów i dokumentacji,
- powtarzające się katalogi,
- niejasne nazwy folderów,
- pliki robocze pomieszane z wersją gotową,
- repozytoria aktywne i archiwalne,
- repozytoria testowe,
- repozytoria biznesowe,
- repozytoria biblioteki skilli i promptów,
- ryzyko danych wrażliwych.

Proponować podział na:

- główne centrum pracy,
- repo biznesowe,
- repo testowe,
- repo archiwalne,
- repo biblioteki skilli i promptów.

## Procedura pracy krok po kroku

1. Ustal cel porządkowania.
2. Zbierz listę repozytoriów i ważnych folderów.
3. Przygotuj mapę repozytoriów.
4. Określ rolę każdego repo.
5. Wskaż duplikaty i konflikty nazw.
6. Oznacz elementy niepewne jako `DO DECYZJI`.
7. Przygotuj raport przed zmianami.
8. Zaproponuj docelową strukturę folderów.
9. Zaproponuj nazwy folderów i repo.
10. Podziel prace na małe, bezpieczne etapy.
11. Wykonuj duży porządek przez małe commity.
12. Po każdej zmianie przygotuj krótki raport.

Zasada główna: najpierw raport, potem zmiany.

## Zasady bezpieczeństwa

- Nie wrzucać haseł.
- Nie wrzucać danych SMTP.
- Nie wrzucać danych bazy.
- Nie wrzucać danych produkcyjnego hostingu.
- Nie wrzucać plików środowiskowych `.env`.
- Nie wrzucać backupów produkcji.
- Nie kasować nic bez backupu i decyzji użytkownika.
- Nie wykonywać masowych zmian bez raportu.
- Nie mieszać repo produkcyjnego z repo testowym.
- Nie przepisywać historii Git bez wyraźnej decyzji użytkownika.

## Format raportu

```text
# Raport porządku repozytoriów

## Zakres

## Mapa repozytoriów

| Repo / folder | Rola | Status | Uwagi |
|---|---|---|---|

## Duplikaty

## Ryzyka bezpieczeństwa

## Elementy DO DECYZJI

## Rekomendowana struktura

## Proponowane etapy prac

## Następny mały commit
```

## Format rekomendacji

Każda rekomendacja powinna zawierać:

- problem,
- proponowaną zmianę,
- powód,
- ryzyko,
- pliki lub foldery objęte zmianą,
- decyzję: `WYKONAĆ / DO DECYZJI / ODRZUCIĆ`.

Przykład:

```text
Rekomendacja: wydzielić prompty produktowe do osobnego repo biblioteki promptów.
Powód: prompty dublują się w kilku miejscach.
Ryzyko: trzeba ustalić, która wersja jest aktualna.
Decyzja: DO DECYZJI.
```

## Czego nie robić

- Nie kasować plików bez decyzji użytkownika.
- Nie przenosić plików bez planu i raportu.
- Nie zmieniać struktury repo na dużą skalę jednym commitem.
- Nie wrzucać sekretów ani danych produkcyjnych.
- Nie traktować niepewnych plików jako śmieci.
- Nie mieszać archiwum z aktywną pracą.
- Nie wykonywać automatycznego `git pull`, `git reset`, `git clean` ani force push.

## Przykładowy prompt użycia

```text
Użyj skill-github-repo-organizer.md.
Przeanalizuj moje lokalne repozytoria i przygotuj raport:
- rola każdego repo,
- duplikaty,
- co jest aktywne,
- co jest archiwalne,
- co wymaga decyzji,
- proponowana struktura folderów.
Najpierw raport, bez kasowania i bez przenoszenia plików.
```
