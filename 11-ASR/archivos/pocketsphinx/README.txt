1. Instalar sphinxbase y pocketsphinx, siguiendo las instrucciones en
   https://cmusphinx.github.io/wiki/tutorialpocketsphinx/
   o bien con `sudo apt install pocketsphinx' en algunas distros de Linux.
   
2. Bajar los modelos para el español.
   https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/
   Versiones actuales (junio 2017):
   Modelo acústico: cmusphinx-es-5.2.tar.gz
   Modelo del lenguaje: es-20k.lm.gz 
   Diccionario: es.dict
   
#################################################
# Ejemplos:

# (0) Preparativos: ubicación de los modelos y directorio de salida.l 
ACOU=cmusphinx-es-5.2/model_parameters/voxforge_es_sphinx.cd_ptm_4000/
DICT=es.dict
LANG=es-20k.lm
OUTDIR=./

#### Ejemplos interactivos.

# (1) Por micrófono, usando un modelo de lenguaje:
pocketsphinx_continuous -inmic yes -hmm $ACOU -dict $DICT -lm $LANG
Para crear un nuevo LM: https://cmusphinx.github.io/wiki/tutoriallm/

# (2) Por micrófono, usando una gramática específica: 
pocketsphinx_continuous -inmic yes -hmm $ACOU -dict $DICT -jsgf gramatica-hola-mundo

Si ser necesario, agregar las palabras faltantes al diccionario fonético (es.dict).


#### Ejemplos en modo batch.

# (3) Procesamiento batch de varios archivos wav, usando el modelo del lenguaje.
pocketsphinx_batch -adcin yes -hmm $ACOU -lm $LANG -dict $DICT -ctl grabaciones.txt -cepext .wav -cepdir ./ -hyp $OUTDIR/salida-con-lm.txt

# (4) Idem pero generando lattices (en formato SLF de HTK).
pocketsphinx_batch -adcin yes -hmm $ACOU -lm $LANG -dict $DICT -ctl grabaciones.txt -cepext .wav -cepdir ./ -hyp $OUTDIR/salida-con-lm.txt -outlatdir $OUTDIR/lattices/ -outlatfmt htk -outlatext .slf

# (5) Procesamiento batch de varios archivos wav, usando el modelo del lenguaje.
pocketsphinx_batch -adcin yes -hmm $ACOU -jsgf gramatica-hola-mundo -dict $DICT -ctl grabaciones.txt -cepext .wav -cepdir ./ -backtrace yes -hyp $OUTDIR/salida-con-gramatica.txt

#### Para visualizar una lattice (hace falta tener instalado 'graphviz'):
STEM=$OUTDIR/lattices/grabacion1 && ./slf2dot.py $STEM && dot -Tps $STEM.dot -o $STEM.ps && evince $STEM.ps


