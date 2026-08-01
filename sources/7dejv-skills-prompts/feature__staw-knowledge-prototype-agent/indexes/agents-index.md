# Agents index

| Nazwa | Zrodlo | Typ | Do czego sluzy | Przydatnosc dla 7dejv | Ryzyko | Rekomendacja |
|---|---|---|---|---|---|---|
| cs-fullstack-engineer | claude-skills agents/engineering | procedure | Stack i architektura fullstack | wysoka | Nie jest natywnym agentem Codexa | adapt |
| cs-frontend-engineer | claude-skills agents/engineering | procedure | Frontend, CWV, a11y, rendering | srednia | Wymaga recznej adaptacji | adapt |
| cs-backend-engineer | claude-skills agents/engineering | procedure | API, DB, SLO, tenancy | wysoka | Pytania moga byc za ciezkie dla malych zmian | use |
| cs-engineer-grill | claude-skills commands | procedure | Forcing questions przed decyzjami | wysoka | Za duzo ceremonii dla prostych fixow | use |
| karpathy-check | claude-skills command/agent | procedure | Review diff przed commitem | wysoka | Skrypty moga miec sciezki vendorowe | adapt |
| cs-bizops-orchestrator | claude-skills business-operations | agent procedure | Procesy, vendorzy, capacity, SOP | wysoka | Nie uruchamiac jako natywnego agenta | use |
| cs-commercial-orchestrator | claude-skills commercial | agent procedure | Pricing, marza, deal, forecast | wysoka | Wymaga danych kosztowych | use |
| cs-research-ops-orchestrator | claude-skills research-ops | agent procedure | Badania rynku i produktu | srednia | Wyniki sa estimates | adapt |
| startup-cto | claude-skills personas | persona | Decyzje techniczne startup/MVP | wysoka | Moze byc zbyt strategiczna | use |
| growth-marketer | claude-skills personas | persona | SEO, content, launch, growth | wysoka | Bez danych klienta moze halucynowac | use |
| solo-founder | claude-skills personas | persona | Priorytety solo founder | srednia | Moze uproscic compliance/finance | adapt |
| 7dejv-staw-knowledge-prototype-agent | 7dejv/agents | 7dejv agent procedure | Research bazy wiedzy polaczony z klikalna wizualizacja HTML/CSS od pierwszej iteracji | bardzo wysoka | Moze przeciazyc mala iteracje; wymagany limit 1-3 tematow i max 3 skille | candidate |
| 7dejv-prestashop-developer | 7dejv/agents | 7dejv agent procedure | Moduly PrestaShop | wysoka | Zgadywanie hookow | use |
| 7dejv-sql-vat-reporter | 7dejv/agents | 7dejv agent procedure | VAT i raporty SQL | wysoka | Ryzyko danych finansowych | use |
| 7dejv-product-margin-analyst | 7dejv/agents | 7dejv agent procedure | Marza i ceny | wysoka | Brak kosztow = zly wynik | use |
| 7dejv-allegro-offer-manager | 7dejv/agents | 7dejv agent procedure | Oferty Allegro | wysoka | Opisy bez danych produktu | use |
| 7dejv-baselinker-operator | 7dejv/agents | 7dejv agent procedure | Statusy i wysylki BaseLinker | wysoka | Zmiana automatyzacji bez mapy | use |
| 7dejv-shipping-cost-auditor | 7dejv/agents | 7dejv agent procedure | Koszty wysylek | wysoka | Brak doplat w danych | use |
| 7dejv-seo-growth-agent | 7dejv/agents | 7dejv agent procedure | SEO i content sklepu | wysoka | Lanie wody bez intentu | use |
| 7dejv-procurement-agent | 7dejv/agents | 7dejv agent procedure | Dostawcy i zakupy | srednia | Niepelne zrodla | use |
| 7dejv-pond-product-expert | 7dejv/agents | 7dejv agent procedure | Produkty stawowe | srednia | Nie wolno wymyslac parametrow | use |
| 7dejv-customer-service-agent | 7dejv/agents | 7dejv agent procedure | Odpowiedzi klientom | wysoka | Obietnice bez danych | use |
| 7dejv-prestashop-performance-agent | 7dejv/agents | 7dejv agent procedure | Performance PrestaShop | wysoka | Optymalizacja bez pomiaru | use |
