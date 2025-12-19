# MoussourisGPT CLI 🖥️

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/security-enhanced-brightgreen.svg)](CHANGELOG.md)

Interface en ligne de commande (CLI) sécurisée pour MoussourisGPT - Un outil d'assistance pour les tâches de scanning, footprinting et énumération réseau.

## ✨ Fonctionnalités

- 🔐 **Authentification sécurisée** avec vérification OTP par email
- 🚀 **Flux d'inscription intelligent** avec vérification intégrée
- 🎨 **Interface utilisateur riche** avec coloration syntaxique
- ✅ **Confirmation avant exécution** pour une sécurité maximale
- 🔄 **Mode CLI et interactif** pour flexibilité d'utilisation
- 📧 **Gestion OTP** avec renvoi automatique
- ⚡ **Timeouts configurables** pour éviter les blocages
- 🛡️ **Protection contre l'injection de commandes**

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Accès Internet pour communiquer avec l'API

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Hegeldirkk/moussourisgpt.git
cd moussourisgpt  
```

### 2. Créer un environnement virtuel (recommandé) -

```bash
python3 -m venv .
source bin/activate  # Sur Linux/Mac
# ou
.\Scripts\activate  # Sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r frontend/requirements.txt
```

### 4. Rendre le script exécutable

```bash
chmod +x msrgpt
```

### 5. (Optionnel) Ajouter au PATH

Pour utiliser `msrgpt` depuis n'importe où :

```bash
echo "export PATH=\"\$PATH:$(pwd)\"" >> ~/.bashrc
source ~/.bashrc
```

## 🎯 Utilisation

### Mode CLI (avec arguments)

#### Créer un compte

```bash
./msrgpt register
```

Le CLI vous guidera automatiquement :
1. Entrez vos informations (nom, pseudo, email, mot de passe)
2. Un code OTP est envoyé à votre email
3. Le CLI vous propose de vérifier immédiatement
4. Entrez le code OTP reçu par email
5. Votre compte est vérifié et prêt !

#### Vérifier l'email (OTP)

```bash
./msrgpt verify
```

#### Renvoyer le code OTP

```bash
./msrgpt resend
```

#### Se connecter

```bash
./msrgpt login
```

#### Exécuter un scan

```bash
# Scan général
./msrgpt run -o Scan -p "scan ports on 192.168.1.1"

# Footprinting
./msrgpt run -o Footprint -p "enumerate services on target.com"

# Énumération
./msrgpt run -o Enum -p "list open ports and services"
```

#### Se déconnecter

```bash
./msrgpt logout
```

#### Afficher l'aide

```bash
./msrgpt --help
./msrgpt run --help
```

### Mode Interactif

Lancez sans arguments pour accéder au menu interactif :

```bash
./msrgpt
```

Menu interactif :
```
=== MSRGPT CLI ===
1. Créer un compte
2. Vérifier email (OTP)
3. Se connecter
4. Envoyer un prompt
5. Se déconnecter
6. Quitter
```

## 📖 Options de scan disponibles

| Option | Description |
|--------|-------------|
| `Scan` | Scan général de réseau et ports |
| `Footprint` | Analyse d'empreinte réseau |
| `Enum` | Énumération de services et ressources |

## 🔒 Sécurité

### Améliorations de sécurité v2.0

- ✅ **Confirmation obligatoire** avant l'exécution de toute commande
- ✅ **Affichage du code** avec coloration syntaxique pour inspection
- ✅ **Timeouts configurables** (30s pour API, 60s pour exécution)
- ✅ **Capture séparée** de stdout/stderr pour meilleure visibilité
- ✅ **Validation des entrées** utilisateur
- ✅ **Gestion sécurisée** des tokens JWT
- ✅ **Protection** contre l'injection de commandes

### Bonnes pratiques

⚠️ **IMPORTANT** : Toujours vérifier le code affiché avant de confirmer son exécution.

- Ne partagez jamais votre token (`.token`)
- Utilisez des mots de passe forts
- Vérifiez toujours les commandes avant de les exécuter
- Ne commitez jamais de fichiers sensibles

## 📁 Structure du projet

```
Moussourisgpt-PythonCli/
├── msrgpt                    # Script principal exécutable
├── frontend/
│   ├── __init__.py
│   ├── main.py              # Point d'entrée et gestion CLI
│   ├── auth.py              # Authentification et gestion OTP
│   ├── api.py               # Communication avec l'API
│   ├── config.py            # Configuration (URL API, etc.)
│   ├── utils.py             # Fonctions utilitaires
│   ├── requirements.txt     # Dépendances Python
│   └── CHANGELOG.md         # Historique des modifications
├── .gitignore               # Fichiers à ignorer par Git
└── README.md                # Ce fichier
```

## 🛠️ Configuration

La configuration se trouve dans `frontend/config.py` :

```python
API_BASE = "https://apimsrgpt.sandbox.200bounty.com"
TOKEN_FILE = ".token"
```

## 📝 Exemples d'utilisation

### Workflow complet

```bash
# 1. Créer un compte (avec vérification OTP intégrée)
./msrgpt register

# 2. Se connecter
./msrgpt login

# 3. Effectuer des scans
./msrgpt run -o Scan -p "scan network 192.168.1.0/24"
./msrgpt run -o Footprint -p "enumerate web server at example.com"
./msrgpt run -o Enum -p "list all services on host"

# 4. Se déconnecter
./msrgpt logout
```

### Gestion des erreurs courantes

#### Email non vérifié
```bash
# Si vous voyez : "Veuillez vérifier votre email avant de vous connecter"
./msrgpt resend   # Renvoyer le code OTP
./msrgpt verify   # Vérifier avec le nouveau code
```

#### Token expiré
```bash
# Si vous voyez : "Session expirée"
./msrgpt login    # Reconnectez-vous
```

## 🔧 Dépendances

Les dépendances principales sont listées dans `frontend/requirements.txt` :

- `requests` - Requêtes HTTP vers l'API
- `rich` - Interface utilisateur enrichie et coloration syntaxique

## 🐛 Dépannage

### Le script n'est pas exécutable
```bash
chmod +x msrgpt
```

### Module non trouvé
```bash
pip install -r frontend/requirements.txt
```

### Erreur de connexion à l'API
- Vérifiez votre connexion Internet
- Vérifiez que l'URL de l'API est correcte dans `frontend/config.py`

### Code OTP invalide
- Vérifiez que vous avez saisi le bon code
- Le code OTP est valide pour une durée limitée, demandez-en un nouveau si nécessaire :
  ```bash
  ./msrgpt resend
  ```

## 📜 Changelog

Voir [CHANGELOG.md](frontend/CHANGELOG.md) pour l'historique détaillé des modifications.

### Version 2.0 - Améliorations majeures

- ✅ Flux d'inscription avec vérification OTP intégrée
- ✅ Commande `resend` pour renvoyer l'OTP
- ✅ Confirmation avant exécution des commandes
- ✅ Coloration syntaxique du code
- ✅ Gestion d'erreurs améliorée
- ✅ Correction vulnérabilité d'injection de commandes

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- **Équipe MoussourisGPT**

## 🙏 Remerciements

- Merci à tous les contributeurs
- Merci à la communauté pour les retours et suggestions

## 📞 Support

Pour toute question ou problème :

- Ouvrir une issue sur GitHub
- Consulter la documentation
- Vérifier le [CHANGELOG.md](frontend/CHANGELOG.md)

---

**⚠️ Avertissement** : Cet outil est destiné à un usage éthique et légal uniquement. Assurez-vous d'avoir les autorisations nécessaires avant d'effectuer des scans ou analyses sur des systèmes qui ne vous appartiennent pas.
