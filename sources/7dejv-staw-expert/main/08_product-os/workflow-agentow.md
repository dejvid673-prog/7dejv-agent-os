# Workflow agentów — STAW EXPERT Product OS

## Cel

Ten workflow opisuje, jak grupa agentów ma opracowywać produkt STAW EXPERT.

## Agenci logiczni

| Agent | Rola | Główny wynik |
|---|---|---|
| A001 Product Director | prowadzi cały produkt | decyzja i komplet dokumentów |
| A002 Market Research | bada rynek i konkurencję | tabela konkurencji i wnioski |
| A003 Safety & Claims | sprawdza ryzyka i język | bezpieczne deklaracje |
| A004 Product Copy | tworzy opisy | opis sklepu, SEO, FAQ |
| A005 Label & Graphics | planuje etykiety i grafiki | G1-G30, front, tył, packshoty |
| A006 Pricing & Logistics | liczy cenę i wysyłkę | minimalna cena, marża, pakowanie |
| A007 Commerce Publisher | przygotowuje wdrożenie | PrestaShop, Allegro |
| A008 Final Auditor | blokuje błędy | release gate |

## Kolejność pracy

1. Product Director tworzy brief.
2. Market Research zbiera konkurencję.
3. Safety & Claims oznacza ryzyka.
4. Product Copy pisze opisy tylko w granicach bezpiecznych deklaracji.
5. Label & Graphics tworzy tekst etykiety i mapę grafik.
6. Pricing & Logistics liczy opłacalność.
7. Commerce Publisher przygotowuje pola sklepu i Allegro.
8. Final Auditor robi release gate.

## Reguła cofania

Jeżeli Final Auditor znajdzie błąd krytyczny, produkt wraca do właściwego agenta:

- problem w deklaracjach → A003,
- problem w opisie → A004,
- problem w etykiecie lub grafice → A005,
- problem w cenie lub wysyłce → A006,
- problem w karcie sklepu → A007.

## Tryby pracy

### FULL PRODUCT MODE

Pełne opracowanie produktu od zera do wdrożenia.

### AUDIT MODE

Kontrola istniejącego produktu, opisu, etykiety lub oferty.

### LABEL MODE

Praca tylko nad etykietą, ale z kontrolą deklaracji.

### COMMERCE MODE

Praca tylko nad PrestaShop, Allegro lub marketplace.

### REPAIR MODE

Poprawa produktu po audycie.
