# utt_osint_project
Projet réalisé dans le cadre de l'UE OSINT durant le Mastère spécialisé expert forensic et cybersécurité de l'UTT. Il s'agit d'un bot réalisé avec selenium pour scrapper les offres de stage concernant la cybersécurité sur le site Hellowork
## Installation
### Clonez le répertoire sur votre ordinateur à l'aide de la commande suivante

```bash
git clone https://github.com/The-N18/utt_osint_project.git
```

### Créez ensuite un environnement virtuel à la racine du projet à l'aide de python
```bash
cd utt_osint_project
```
#### Pour python 2 
utiliser le gestionnaire de paquêts [pip](https://pip.pypa.io/en/stable/) pour installer virtualenv.
```bash
py -m pip install --user virtualenv
```
créez ensuite l'environnement virtuel
```bash
py -m virtualenv venv
```

#### Pour python 3
```bash
py -m venv venv
```

### Activez l'environnement virtuel
Sous Windows
```bash
.\venv\Scripts\activate
```

Sous linux
```bash
source venv/bin/activate
```
### Installez les dépendances du projet
```bash
pip install -r requirements.txt
```

### Lancez le projet
```bash
python main.py
```