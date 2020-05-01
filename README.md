# Politični tipi
V README.md so dovoljene slengovske tujke, koda in komantarji pa naj vsebujejo čim bolj odurne slovenske ustreznice. 

## Trenutno bi bila ustreznejša uporaba dvojine
Prijatelja Levičar in Desničar, ki na socialnih omrežjih delita svoje politične ideje.

## Ideja
2 samostojna programa (Levičar in Desničar) bi s pomočjo procesiranja besedila in aktivnosti na socialnih omrežjih simulirala obnašanje povprečnega slovenskega navdušenca nad politiko.
### Procesiranje in konstruiranje besedila
Na podlagi baze podatkov bi opremila vhodno besedilo s čustvenčki in vzkliki, primernimi njunim političnim čustvom.

Primer za Levičarja:
Vhod | Izhod
------------ | -------------
Luka nosi rdeč pulover in  ne mara Janeza. | Luka:heart: nosi rdeč :heart_eyes: pulover in ne mara Janeza :poop:.
### Twitter
Svoje politične govore bi delila na Twitterju, kjer bi tuje politične tweete prejela kot vhodno besedilo. Seveda bosta oba nadobudna filozofa ustvarjala tudi avtorsko prozo.

Primer za Desničarja:

Janša je moj :heart:, homosekusalci so :thumbsdown:.
### Umetna inteligenca
Našo ciljno skupino se sicer da simulirati brez AI, seveda pa so vse izbolšave, ki bodo naredila projekt še bolj neznosen za slovenski Twitter, zaželjene.
### Politična koreknost projekta
Politična korektnost se v Tržiču žal še ni razvila.
### Izvedba
Programa se bosta obnašala enako, različne bodo le njune preference. Analiza besedila bo torej ista, le vrednotenje bo drugačno.
Primer rekonstrukcije stavka "Po obdobju komunizma je sledil kapitalizem".
Levičar | Desničar
------------ | -------------
Po svetem obdobju komunizma:purple_heart: je sledil nečloveški kapitalizem:rage:.|Po nečloveškem obdobju komunizma:rage: je sledil sveti kapitalizem:purple_heart:.

Twitter API bi (če ga sploh bi) dodali na koncu. Na začetku bi spisali dober sistem za ustvarjanje sočnih političnih manifestov, haikujev in bolečih črtic maturitetne kakovosti. 
**Projekt bi se v glavnem pisalo v pythonu.**
## Sodelovanje na projektu
Trenutno projekt še ni niti v plenicah, pričakuje pa se lahko približen načrt dela in težave. Vsaka pomoč je dobrodošla.

## English Translation:
Donald Bad <img src="https://render.githubusercontent.com/render/math?math=\iff"> my jokes good



## Osnove uporabe gita za virgin Windows userje z Urhom, ki ga sicer ne zna uporabljati
1. Enostavna rešitev: naloži Linux. Če ne gre, glej (2)
2. Sledite navodilom prof. Pretnarja na https://ucilnica.fmf.uni-lj.si/mod/page/view.php?id=37144 in si na računalnik namestite git
### Namen gita
Ker nas na projektu dela več, potrebujemo dober sistem za izmenjavo kode. S pomočjo gita se vam ne bo treba ubadati z iskanjem tuje kode in najnovejših verzij, saj bo to delal git namesto vas. Vi boste programirali na lokalnem računalniku, git pa bo poskrbel, da imate vedno svežo kodo in objavil vašo na repozitorij. Prav tako uporablja črno magijo, da združi delo različnih ljudi v eno datoteko. (*merging*).
### Priprava delovnega okolja za prvo uporabo
Ustvarite prazno mapo in v njej odprite *git bash*. (desni klik *v mapi*, "open git bash here"). Za začetek morate naložiti vse dosedanje datoteke in ustvariti svoj lokalni git repozitorij. To storite z ukazom `git clone https://github.com/urhprimozic/politicni-tipi.git`.
Ob prvi uporabi (verjetno ob prvem commitu), vas bo git vprašal za osebne podatke. Takrat ga ubogate in naredite, kar hoče, saj je blazno prijazno bitje in si to zasluži.
Aja, mogoče to vse dela tudi v osnovnem windowsovem terminalu in ni treba git basha.
### Uporaba
Vsakič, preden začnete z delom, izven mape `politicni-tipi` poženite ukaz `git pull`, da pridobite najnovejše datoteke. Ko ste zadovoljni z delom in bi ga radi objavili nazaj, poženite:
`git add <ime_datoteke_ki_bi_jo_radi_dodali>` za dodajanje ene datoteke ali mape, oziroma
`git add *` za dodajanje vsega v vrsto. _Preberite si kaj  regexu in o .gitignore_

Potem z ukazom `git commit` ustvarite novo revizijo z novimi datotekami. (`add` in `commit` lahko zdruzite z ukazom `git commit -a`).
Med procesom vas bo git prosil, da spišete kratko besedilo o vaših spremembah. Za to vam lahko Špela razloži, kako se uporablja Vim:heart:.

Nato spremembe objavite na streznik z `git push`, oziroma `git push https://github.com/urhprimozic/politicni-tipi.git` (baje, da windows nekaj nagaja).

## Modul emoji
Naš program po potreboval modul [emoji](https://pypi.org/project/emoji/), ki ga ni med standardnimi moduli v pythonu. Zato ga morate na svoj računalnik naložiti ročno. S pomočjo *pip*a ga naložite z ukazom `pip install emoji`. Na [spletni strani](https://pypi.org/project/emoji/) si poglejte primer uporabe.

## conda
...TO DO