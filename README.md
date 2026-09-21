# CâtDau - ce mai e si asta? ❓

Afla instant in ce supermarket iesi cel mai ieftin cu lista ta de cumparaturi, pe baza reducerilor din saptamana curenta (si a brandurilor tale preferate).

# De unde a pornit ideea? 🤔

Mereu, inainte sa plec la cumparaturi, stateam si ma uitam prin cataloagele de la supermarketurile din zona mea, pentru a vedea unde sunt cele mai bune oferte, astfel incat sa ies cu un cos cat mai ieftin.

# Okay, si cine esti tu? 🤷‍♂️

Eyo... chill, sunt un simplu student la FMI UBB Cluj, pasionat de scris cod si de gasit solutii pentru chestiile repetitive care imi mananca timp aiurea. Rasfoitul cataloagelor e super time-wasting, nu am facut pana acuma un mobile app, 1+1=2, asa ca am decis sa ma chinui singur (fara AI, bine... doar cu putin ajutor pt research, dar tot codul o sa fie scris de mine, promise 🤞) si sa automatizez acest proces. Sper sa-mi iasa.

Mai multe detalii despre mine poti gasi pe LinkedIn, GitHub sau Discord (o sa adaug linkuri cand termin de aranjat profilele, ca rn arata urat af, poate chiar o sa-mi fac un mic site, da chiar e o idee buna ngl...).

# Bine, bine... si cum mai exact o sa faci asta? 🥱

O sa iti zic super pe scurt (cand ma apuc serios de treaba o sa mai updatez acest README):
Un cod mic in Python care descarca cataloagele disponibile online si extrage automat preturile, o baza de date (SQLite) pentru produse si preturi, iar toata informatia o sa fie servita printr-un API cu FastAPI. 

Pentru aplicatia de mobil o sa folosesc Flutter. Ideea principala: iti faci lista in aplicatie (sau dai paste din Notes), iar pe baza reducerilor din magazinele din zona (momentan Profi si Penny), aplicatia iti spune exact unde iti iese cosul cel mai ieftin.

# Si care este progresul actual? 🤗

Hmmm, am ideea — i mean, si ala e un inceput, nu????
O sa incep cu branding-ul, sa aleg un nume okay (eu zic ca CâtDau e decent, astept feedback tho), iar apoi ma apuc de scraping, asta imi propun chiar azi (si maine). 

-- am amanat proiectul putin but rn avem functia ce da download la current week catalog si converteste fiecare pagina in png
-- obiectivul urmator: ocr

-- am amanat din nou proiectul sorry guys, updates: am rezolvat OCR, am incercat Laplacian, EAST ocr, am incercat sa ma joc cu saturatia and so on, dar nimic nu mergea cum am vrut.
-- pana cand am dat de RapidOCR (thx to the indian guy & claude pt explicatii si searching)
-- obiectivul urmator: parsing, din rezultatul de la OCR sa extrag si sa fac frumos liste sau dict idk vedem

So, come back tomorrow to see if I really did it or if I'm too lazy.