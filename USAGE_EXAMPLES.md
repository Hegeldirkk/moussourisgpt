# Exemples d'utilisation de MSRGPT CLI

## 🚀 Flux d'inscription complet (NOUVEAU - Amélioré)

### Scénario 1 : Nouvelle inscription avec vérification immédiate

```bash
$ ./msrgpt register

 --- Création de compte ---
Nom complet: Jean Dupont
Pseudo: jdupont
Email: jean@example.com
Mot de passe: ********

✓ Compte créé avec succès !
📧 Un code OTP a été envoyé à votre email.

Voulez-vous vérifier votre email maintenant? (oui/non): oui
Code OTP (reçu par email): 123456

✓ Email vérifié avec succès. Vous pouvez maintenant vous connecter.
```

### Scénario 2 : Compte déjà existant - Renvoi automatique de l'OTP

```bash
$ ./msrgpt register

 --- Création de compte ---
Nom complet: Jean Dupont
Pseudo: jdupont
Email: jean@example.com
Mot de passe: ********

⚠ Ce compte existe déjà

Voulez-vous renvoyer le code OTP à cet email? (oui/non): oui

✓ Code OTP renvoyé avec succès. Vérifiez votre email.
Code OTP (reçu par email): 123456

✓ Email vérifié avec succès. Vous pouvez maintenant vous connecter.
```

### Scénario 3 : Renvoyer l'OTP manuellement

```bash
$ ./msrgpt resend
Email: jean@example.com

✓ Code OTP renvoyé avec succès. Vérifiez votre email.
```

## 📋 Flux complet de A à Z

```bash
# 1. Créer un compte (avec vérification automatique)
./msrgpt register

# 2. Se connecter
./msrgpt login

# 3. Exécuter un scan
./msrgpt run -o Scan -p "scan the network 192.168.1.0/24"

# 4. Se déconnecter
./msrgpt logout
```

## 🔧 Commandes disponibles

| Commande | Description |
|----------|-------------|
| `./msrgpt register` | Créer un compte (avec vérification OTP intégrée) |
| `./msrgpt verify` | Vérifier l'email avec le code OTP |
| `./msrgpt resend` | Renvoyer le code OTP par email |
| `./msrgpt login` | Se connecter |
| `./msrgpt logout` | Se déconnecter |
| `./msrgpt run -o <option> -p "<prompt>"` | Exécuter un prompt |
| `./msrgpt --help` | Afficher l'aide |

## 🎯 Options de scan disponibles

- `Scan` - Scan général
- `Footprint` - Empreinte réseau
- `Enum` - Énumération

## 📝 Exemples de prompts

```bash
# Scan de ports
./msrgpt run -o Scan -p "scan ports on 192.168.1.1"

# Footprinting
./msrgpt run -o Footprint -p "enumerate services on target"

# Énumération
./msrgpt run -o Enum -p "list open ports and services"
```

## ⚙️ Mode interactif

Lancez sans arguments pour le menu interactif :

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
