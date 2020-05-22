# Npuzzle - A*
Meghívás: main.py [argumentumok]
1. –input \<FILE>: a kezdeti állapotot tartalmazó állomány neve. Ha a kapcsoló hiányzik, a standard bemenetrõl
olvassa be a kezdeti állapotot.
2. –solseq: a standard kimenetre írja a teljes megoldási szekvenciát
3. –pcost: a standard kimenetre írja a megoldás költségét
4. –nvisited: a standard kimenetre írja a meglátogatott csomópontok számát
5. –h \<H>: a heurisztika típusa. Ha H=1, használja a „rossz helyen levõ csempék száma” heurisztikát. Ha H=2, használja a Manhattan heurisztikát.
6. –rand \<N> \<M> egy véletlenszerû, N méretû állapotot írjon ki a standard kimenetre. M a véletlenszerû
tologatások számát jelenti.

Példa meghívásra:
```
python main.py -input szamok.txt -solseq -nvisited -pcost -h 1
```
