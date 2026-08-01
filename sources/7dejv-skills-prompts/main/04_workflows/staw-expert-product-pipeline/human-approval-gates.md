# Human Approval Gates

## Gate A — wybór kierunku produktu

Po analizie konkurencji człowiek zatwierdza problem klienta, kategorię i zakres dalszych badań.

## Gate B — skład i bezpieczeństwo

Technolog/laboratorium zatwierdza albo odrzuca brief formulacji. AI nie może nadać `APPROVED`.

Wymagane minimum:
- źródła danych o składnikach,
- ocena ryzyka,
- status regulacyjny,
- lista brakujących badań.

## Gate C — plan dawkowania

Człowiek zatwierdza warunki prób, kryteria STOP, grupę kontrolną i sposób pomiaru.

## Gate D — nazwa i komunikacja

Właściciel marki zatwierdza nazwę oraz deklaracje marketingowe. Nazwa z ryzykiem podobieństwa pozostaje `HOLD`.

## Gate E — etykiety

Zatwierdzenie obejmuje:
- zgodność treści,
- czytelność,
- wymagane dane,
- brak imitacji konkurenta,
- fizyczny test wydruku etykiety A6.

## Gate F — release

Ostateczna decyzja przed pilotażem wymaga zatwierdzenia składu, dawkowania, dokumentacji, etykiet, kosztów i planu kontroli jakości.

## Realizacja w n8n

```text
Set status = WAITING_APPROVAL
→ zapisz rekord approvals
→ Wait node / Form / Webhook
→ zweryfikuj reviewer i decision
→ APPROVED: przejdź dalej
→ CHANGES_REQUIRED: cofnij do wskazanego etapu z nową input_version
→ REJECTED: BLOCKED
```

Akceptacja musi zawierać osobę, datę, decyzję i notatkę. Samo kliknięcie bez identyfikacji nie wystarcza dla bramek B, C, E i F.
