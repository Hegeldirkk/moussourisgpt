# Changelog des Améliorations

## Version 2.0 - Flux d'inscription amélioré

### Nouvelles fonctionnalités

#### 1. Vérification OTP intégrée au flux d'inscription
- **Après inscription** : Proposition automatique de vérifier l'OTP directement
- **Compte existant** : Proposition de renvoyer le code OTP si le compte existe déjà
- Flux fluide et intuitif sans besoin de relancer des commandes

#### 2. Commande `resend` pour renvoyer l'OTP
- Nouvelle commande CLI : `./msrgpt resend`
- Permet de renvoyer facilement le code OTP sans se réinscrire

#### 3. Fonctions de vérification OTP améliorées
- `verify_otp()` : Vérification interactive (demande email + OTP)
- `verify_otp_with_data(email, otp)` : Vérification avec données fournies
- `resend_otp(email)` : Renvoi du code OTP

---

# Changelog des Améliorations

## Améliorations de Sécurité

### 1. Correction de la vulnérabilité d'injection de commandes
- **Avant**: Le code exécutait directement les commandes reçues de l'API sans validation
- **Après**:
  - Ajout d'une confirmation utilisateur obligatoire avant l'exécution
  - Affichage du code avec coloration syntaxique pour inspection
  - Timeout de 60 secondes pour éviter les blocages
  - Capture et affichage séparé de stdout/stderr

### 2. Amélioration de la gestion des tokens
- Ajout de la fonction `logout()` pour supprimer proprement le token
- Meilleure validation du token lors du chargement

## Améliorations Fonctionnelles

### 1. Gestion d'erreurs robuste
- Ajout de timeouts (30s pour API, 60s pour exécution)
- Gestion spécifique des erreurs HTTP (401, 403, timeout, connexion)
- Messages d'erreur clairs et informatifs avec icônes
- Codes de sortie appropriés pour CLI mode

### 2. Amélioration de l'interface
- Coloration syntaxique pour le code reçu (via rich.syntax)
- Icônes visuels (✓, ✗, ⚠) pour feedback utilisateur
- Validation des entrées (options, prompts non vides)
- Messages cohérents et professionnels

### 3. CLI Mode amélioré
- Validation stricte des options avec `choices=["Scan", "Footprint", "Enum"]`
- Codes de sortie corrects (0 pour succès, 1 pour échec)
- Descriptions détaillées pour les commandes
- Meilleure séparation mode CLI / mode interactif

## Configuration

### Mise à jour de l'URL de l'API
- Nouvelle URL: `https://apimsrgpt.sandbox.200bounty.com`
- Nettoyage de la configuration (suppression de l'ancienne URL)

## Usage

### Mode CLI
```bash
# Inscription
msrgpt register

# Connexion
msrgpt login

# Exécuter un scan
msrgpt run -o Scan -p "scan this target"

# Déconnexion
msrgpt logout
```

### Mode Interactif
```bash
msrgpt
```

## Sécurité

⚠️ **Important**: Toujours vérifier le code affiché avant de confirmer son exécution.
