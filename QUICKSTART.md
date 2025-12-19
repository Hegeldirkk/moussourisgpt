# Guide de Démarrage Rapide 🚀

Guide en 5 minutes pour commencer avec MoussourisGPT CLI.

## ⚡ Installation Express

```bash
# 1. Se placer dans le répertoire
cd Moussourisgpt-PythonCli

# 2. Installer les dépendances
pip install -r frontend/requirements.txt

# 3. Rendre le script exécutable
chmod +x msrgpt

# 4. Tester l'installation
./msrgpt --help
```

## 🎯 Premier Scan en 3 Étapes

### Étape 1 : Créer un compte

```bash
./msrgpt register
```

Remplissez les informations :
- Nom complet
- Pseudo
- Email
- Mot de passe

**💡 Astuce** : Lorsqu'on vous demande si vous voulez vérifier maintenant, répondez **oui** et entrez le code OTP reçu par email.

### Étape 2 : Se connecter

```bash
./msrgpt login
```

### Étape 3 : Lancer votre premier scan

```bash
./msrgpt run -o Scan -p "scan ports on localhost"
```

Vérifiez la commande affichée, puis confirmez l'exécution en tapant **oui**.

## 📋 Commandes Essentielles

```bash
# Afficher l'aide
./msrgpt --help

# Créer un compte
./msrgpt register

# Vérifier l'email
./msrgpt verify

# Renvoyer le code OTP
./msrgpt resend

# Se connecter
./msrgpt login

# Scanner un réseau
./msrgpt run -o Scan -p "votre demande"

# Footprinting
./msrgpt run -o Footprint -p "votre demande"

# Énumération
./msrgpt run -o Enum -p "votre demande"

# Se déconnecter
./msrgpt logout
```

## 🎨 Mode Interactif

Pour les débutants, le mode interactif est plus simple :

```bash
./msrgpt
```

Ensuite, suivez le menu :
```
1. Créer un compte      → Pour commencer
2. Vérifier email (OTP) → Si vous n'avez pas vérifié lors de l'inscription
3. Se connecter         → Après vérification
4. Envoyer un prompt    → Pour scanner
5. Se déconnecter       → Quand vous avez fini
6. Quitter              → Pour sortir
```

## 💡 Exemples de Prompts

### Scan de Ports
```bash
./msrgpt run -o Scan -p "scan all open ports on 192.168.1.1"
./msrgpt run -o Scan -p "check for common vulnerabilities on target"
```

### Footprinting
```bash
./msrgpt run -o Footprint -p "gather information about example.com"
./msrgpt run -o Footprint -p "enumerate web technologies on target"
```

### Énumération
```bash
./msrgpt run -o Enum -p "list all services running on host"
./msrgpt run -o Enum -p "enumerate users and shares on target"
```

## 🔧 Résolution Rapide de Problèmes

### Erreur : "command not found"
```bash
# Assurez-vous que le script est exécutable
chmod +x msrgpt

# Utilisez ./ avant la commande
./msrgpt --help
```

### Erreur : "Module not found"
```bash
# Installez les dépendances
pip install -r frontend/requirements.txt
```

### Erreur : "Email non vérifié"
```bash
# Renvoyez le code OTP
./msrgpt resend

# Vérifiez avec le nouveau code
./msrgpt verify
```

### Erreur : "Session expirée"
```bash
# Reconnectez-vous
./msrgpt login
```

## 🔒 Sécurité

⚠️ **Points importants** :

1. **Vérifiez toujours** le code avant de l'exécuter
2. **Ne partagez jamais** votre fichier `.token`
3. **Utilisez uniquement** sur des systèmes autorisés
4. **Déconnectez-vous** après utilisation

## 📚 Aller Plus Loin

- [README.md](README.md) - Documentation complète
- [CHANGELOG.md](frontend/CHANGELOG.md) - Historique des versions
- [SECURITY.md](SECURITY.md) - Politique de sécurité

## 🆘 Besoin d'Aide ?

```bash
# Aide générale
./msrgpt --help

# Aide pour une commande spécifique
./msrgpt run --help
```

---

**Prêt à scanner ?** 🎯

```bash
./msrgpt register && ./msrgpt login
```

Bienvenue dans MoussourisGPT CLI ! 🎉
