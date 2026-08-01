# Skill: DPD API Adapter

Data utworzenia: 2026-06-06
Główne zastosowanie: `dpdshipmvp`

---

## Cel skillu

Ten skill służy do projektowania bezpiecznej warstwy komunikacji z API DPD.

Ma oddzielić:

- panel Back Office,
- kontrolery akcji,
- logikę biznesową,
- rzeczywistą komunikację z DPD,
- mocki testowe,
- obsługę błędów.

---

## Najważniejsza zasada

API DPD nie może być wywoływane przypadkowo.

Wywołanie API jest dozwolone tylko po świadomej akcji administratora, np.:

- kliknięcie `Test połączenia`,
- kliknięcie `Nadaj przesyłkę`,
- kliknięcie `Pobierz etykietę`,
- kliknięcie `Sprawdź tracking`.

---

## Kiedy używać

Użyj tego skillu, gdy zadanie dotyczy:

- adaptera API DPD,
- testu połączenia,
- tworzenia przesyłki,
- pobierania etykiety,
- trackingu,
- FID,
- timeoutów,
- retry,
- mocków,
- mapowania błędów DPD,
- bezpiecznego logowania odpowiedzi API.

---

## Źródła do sprawdzenia

Przed pracą przeczytaj:

1. `README.md`
2. `AGENTS.md`
3. `.ai/CONTEXT.md`
4. `.ai/GOTCHAS.md`
5. `docs/modules/dpdshipmvp/wymagania.md`
6. `docs/modules/dpdshipmvp/api-dpd-notatki.md`, jeśli istnieje
7. `skills/skill-prestashop-order-hooks.md`
8. `skills/skill-prestashop-symfony-config-form.md`
9. oficjalną dokumentację DPD dostarczoną przez użytkownika albo link w repo

Jeżeli nie ma oficjalnej dokumentacji DPD, nie zgaduj endpointów. Przygotuj interfejs, mocki i miejsca integracji.

---

## Proponowana architektura

```text
src/
  Dpd/
    DpdClientInterface.php
    DpdApiClient.php
    DpdMockClient.php
    DpdRequestFactory.php
    DpdResponseMapper.php
    DpdException.php
  Service/
    ShipmentService.php
    LabelService.php
    TrackingService.php
    DpdConfigService.php
```

---

## Interfejs adaptera

Adapter powinien mieć metody wysokiego poziomu, np.:

```text
testConnection()
createShipment(orderData)
downloadLabel(shipmentId)
getTracking(trackingNumber)
```

Kontroler Back Office nie powinien znać szczegółów API DPD.

---

## Mocki

MVP powinien mieć mocki, zanim pojawi się realna integracja.

Mock powinien pozwolić testować:

- sukces testu połączenia,
- błąd logowania,
- timeout,
- sukces utworzenia przesyłki,
- błąd walidacji danych,
- sukces pobrania etykiety,
- brak etykiety,
- tracking dostępny,
- tracking niedostępny.

---

## Timeouty i błędy

Każde wywołanie DPD powinno mieć:

- timeout,
- limit retry lub świadomą decyzję o braku retry,
- mapowanie błędów technicznych,
- mapowanie błędów biznesowych,
- czytelny komunikat dla administratora,
- bezpieczny log techniczny.

---

## Bezpieczne logowanie

Logować wolno:

- typ akcji,
- id zamówienia,
- status,
- kod błędu,
- czas trwania,
- skrócony komunikat.

Nie logować:

- haseł,
- tokenów,
- pełnych danych klienta,
- pełnego adresu,
- pełnej odpowiedzi API,
- PDF etykiety,
- danych kart/płatności.

---

## Przechowywanie etykiet

Etykiety PDF nie powinny być publicznie dostępne bez kontroli.

Zalecenia:

- zapisywać plik w kontrolowanym katalogu modułu albo generować na żądanie,
- zapisywać w bazie tylko ścieżkę/metadane,
- nie zapisywać PDF jako blob w bazie w MVP,
- kontrolować uprawnienia przy pobieraniu.

---

## Czego unikać

- API DPD w `orderpanelmvp`,
- API DPD w hooku przy samym wyświetleniu zamówienia,
- generowania etykiety bez potwierdzenia administratora,
- pełnych odpowiedzi API w logach,
- endpointów wpisanych na sztywno bez konfiguracji,
- braku mocków,
- braku timeoutu,
- mieszania adaptera z kontrolerem.

---

## Procedura pracy Codex

```text
Etap 1: Sprawdź, czy jest oficjalna dokumentacja DPD.
Etap 2: Jeżeli nie ma dokumentacji, zaprojektuj interfejs i mocki bez realnych endpointów.
Etap 3: Zaprojektuj strukturę klas adaptera.
Etap 4: Zaprojektuj obsługę błędów i logów.
Etap 5: Zaprojektuj przepływ: panel -> kontroler akcji -> serwis -> adapter.
Etap 6: Przygotuj checklistę testów.
Etap 7: Dopiero po zatwierdzeniu implementuj realną komunikację.
```

---

## Wynik końcowy

Codex powinien zwrócić:

- interfejs adaptera,
- strukturę klas,
- listę mocków,
- mapę błędów,
- zasady logowania,
- zasady przechowywania etykiet,
- ryzyka,
- pytania blokujące, jeśli brakuje dokumentacji DPD.
