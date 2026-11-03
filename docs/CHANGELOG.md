# Nebula Core — changelog dalla v2.5

Base di partenza: la v2.5 (index.html caricato dall'utente). Le versioni sono state verificate in un browser simulato (jsdom): nessuna prova ancora su GPU, Brave o iPhone reali.

## v2.6 — stabilità e offline
- three.js incluso nel file; rimosso `/_aistudio-iframe.js`. Corretto il crash con microfono attivo (`micEnergy` fuori ambito).
- Esplosione sul picco del microfono (timer separato), etichette degli slider non più sovrascritte, attrattore allineato al dito (proiezione reale), forze nello spazio locale con autorotazione, fisica indipendente dal refresh rate.
- Prestazioni: una sola InstancedMesh, matrici scritte direttamente, colori da tabella, DPR adattivo.
- Webcam: fallback con tracker di movimento senza MediaPipe, avvisi chiari sui permessi (Brave/iOS), note della mano limitate.
## v2.7–v2.8 — iPhone e pannello fisica
- Avviso se la pagina è aperta da file locale; pacchetto per la pubblicazione; pannello fisica leggibile (niente "VEDI SCIAME" bloccato).
## v2.9 — menù unico e 14 preset
- Menù unico a 5 schede; 14 preset con forma, geometria, fisica e suono propri; pulsante AUDIO ON/MUTO; qualità di registrazione video più alta; three.js ES (niente warning).
## v2.10–v2.12
- Preset con gamma arcobaleno unica; schermo intero con modalità immersiva di riserva; zoom a due dita e rotella; chip a selezione singola corretti; zoom globale con adattamento automatico; ◀ ▶ per i preset; fade-in audio.
## v2.13 — hardening
- Sospensione di audio/camera/microfono in background; fallback senza WebGL; accessibilità (nomi, focus, Esc); movimento ridotto; nodi del loop memorizzati.
## v2.14 — rotazione 4D vera
- Coordinata W per ogni particella e rotazione nei piani XW/YW/ZW.
## v2.15 — preset e apertura
- Wanderer e Spectra a +1 in tutti i preset; valori manuali di Wanderer/Spectra fissi tra i preset; apertura graduale dal nero.
## v2.16 — audio morbido
- Piano morbido, pad morbido, drone polifonico (max 8 voci); slider attacco e sustain; scelte manuali dei timbri protette.
## v2.17 / v2.17.1 — barra in basso, cristalli, robustezza
- Barra a sezioni in basso, pannello a comparsa con maniglia, pillola preset, lucchetti AUDIO/ROTAZIONE tra i preset.
- Suoni cristallini da impatti tra particelle; tetto di 150 voci vive, livello automatico e compressore; ripresa dello stato audio interrotto; diagnostica audio.
- Pulsanti MIC e CAM resi di nuovo accessibili.
## v2.18 — barra scorrevole a scomparsa
- Barra scorrevole con tutti i comandi rapidi che scompare dopo 6 s; 4 modalità dei cristalli (impatti, scintille, sfere, tutti); anteprima webcam in basso e riducibile; pillola preset nascondibile e richiamabile; audio di partenza fisso (valori scelti dall'utente).
## v2.19–v2.20 — anelli di Wanderer e Spectra
- Due anelli controrotanti per sfera, colore che cambia di continuo, effetti casuali (vortice, pulsazione, spinta, calma) sullo sciame, note e cristalli sull'audio.
- v2.20: rotazione resa visibile (assi di giro diversi dall'asse dell'anello + perline luminose); in v2.19 gli anelli giravano attorno al proprio asse e sembravano fermi.

## v2.21 — controller MIDI per Logic Pro
- MIDI Out via Web MIDI (nessun server): note da tocco, mano, microfono, note cinetiche, cristalli e anelli; CC1 = X, CC74 = Y invertita, CC11 = mano chiusa / dito premuto (come nella versione React di AI Studio).
- Porta (automatica con IAC, tutte o singola) e canale selezionabili; panic automatico in background, al cambio di porta/canale e allo spegnimento; note anche con l'audio interno in muto; porte collegate dopo l'avvio riconosciute.
- Avvio automatico solo se il permesso MIDI era già stato concesso. Privacy policy e `_headers` aggiornati.

## v2.22 — fine del martellamento
- Causa individuata: le note cinetiche partivano a intervalli quasi fissi (circa 3 al secondo, variabilità 0,2) finché il movimento superava una soglia bassa, cioè sempre con i valori di partenza.
- Nuovo modo "SU VARIAZIONI" (predefinito): la nota parte quando il movimento cambia, non mentre è stabile (con una nota di sicurezza ogni 5 s se il movimento resta alto); "CONTINUO" ripristina il comportamento precedente.
- Slider SMORZAMENTO NOTE (predefinito 0,6): dopo ogni nota servono più energia e più tempo; vale per note cinetiche, microfono e cristalli. Attesa casuale, mai la stessa nota di fila, dinamica variabile.
- Diagnostica audio: note al secondo per sorgente (cinetiche, cristalli, anelli, microfono). Misura in simulazione: da 2,9 a circa 0,3–0,6 note/s con smorzamento 0,6.

## Non ancora fatto
- Progetto Android / Google Play (struttura Capacitor non ancora preparata).
- Prove su dispositivi reali (iPhone, Brave Android) e ascolto dei timbri.
- Salvataggio delle impostazioni tra una sessione e l'altra (richiederebbe aggiornare la privacy policy).
