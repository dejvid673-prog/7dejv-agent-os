# Status Transition Matrix

| Etap | PASS prowadzi do | HOLD | BLOCKED | Wymagana akceptacja |
|---|---|---|---|---|
| DISCOVERED | SHORTLISTED | uzupełnij dane ofert | zakończ kandydata | nie |
| SHORTLISTED | ANALYZED | popraw scoring | odrzuć kandydatów | nie |
| ANALYZED | COMPOSITION_EVIDENCE | uzupełnij źródła | ryzyko kopiowania | nie |
| COMPOSITION_EVIDENCE | FORMULATION_DRAFT | szukaj dokumentów | krytyczna sprzeczność | nie |
| FORMULATION_DRAFT | DOSAGE_TEST_PLAN | uzupełnij brief | nieakceptowalne ryzyko | tak, technolog/lab |
| DOSAGE_TEST_PLAN | HUMAN_LAB_REVIEW | popraw plan | brak bezpiecznej ścieżki | tak |
| HUMAN_LAB_REVIEW | NAMING_DRAFT | zmiany wymagane | odrzucenie projektu | tak |
| NAMING_DRAFT | COPY_DRAFT | nowa propozycja | konflikt nazwy | tak |
| COPY_DRAFT | FRONT_LABEL_DRAFT | popraw deklaracje | niedozwolone twierdzenia | tak |
| FRONT_LABEL_DRAFT | BACK_LABEL_DRAFT | popraw makietę | imitacja konkurenta | tak |
| BACK_LABEL_DRAFT | RELEASE_AUDIT | popraw dane/DTP | brak obowiązkowych danych | tak |
| RELEASE_AUDIT | READY_FOR_PILOT | lista poprawek | produkt zablokowany | tak |

## Reguły

- `ERROR` nie zmienia etapu; uruchamia politykę retry.
- `WAITING_APPROVAL` wstrzymuje wykonanie przez Wait/Webhook/Form w n8n.
- `BLOCKED` wymaga nowej decyzji projektowej, nie automatycznego ponowienia.
- Cofnięcie etapu tworzy nową `input_version` i zachowuje poprzedni raport.
