# Politique de Sécurité

## 🔒 Versions Supportées

| Version | Supportée          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.x.x   | :x:                |

## 🛡️ Améliorations de Sécurité (v2.0)

### Corrections de Vulnérabilités

- ✅ **Injection de commandes** : Ajout de confirmation utilisateur obligatoire avant exécution
- ✅ **Affichage du code** : Coloration syntaxique pour inspection visuelle
- ✅ **Timeouts** : Protection contre les blocages (30s API, 60s exécution)
- ✅ **Validation des entrées** : Vérification stricte des options et prompts
- ✅ **Gestion sécurisée des tokens** : Stockage local avec suppression propre

## 🚨 Signaler une Vulnérabilité

Si vous découvrez une vulnérabilité de sécurité dans MoussourisGPT CLI, veuillez nous en informer de manière responsable :

### Processus de Signalement

1. **NE PAS** créer d'issue publique sur GitHub
2. Envoyer un email à : **security@moussourisgpt.com** (ou contactez les mainteneurs directement)
3. Inclure dans votre rapport :
   - Description détaillée de la vulnérabilité
   - Steps pour reproduire le problème
   - Impact potentiel
   - Suggestions de correction (si possible)

### Ce à quoi s'attendre

- **Accusé de réception** : Sous 48 heures
- **Évaluation initiale** : Sous 7 jours
- **Correction et patch** : Variable selon la gravité
- **Publication** : Après déploiement du correctif

## 🔐 Bonnes Pratiques de Sécurité

### Pour les Utilisateurs

#### 1. Protection du Token
```bash
# Le fichier .token contient votre token d'authentification
# NE JAMAIS le partager ou le commiter dans Git
chmod 600 frontend/.token  # Permissions restrictives
```

#### 2. Vérification des Commandes
- **TOUJOURS** lire le code affiché avant de confirmer l'exécution
- Refuser l'exécution de commandes suspectes
- Signaler les comportements anormaux

#### 3. Mots de Passe Forts
- Minimum 12 caractères
- Mélange de majuscules, minuscules, chiffres et symboles
- Unique pour ce service

#### 4. Déconnexion
```bash
# Toujours se déconnecter après utilisation
./msrgpt logout
```

#### 5. Mise à Jour
```bash
# Garder le CLI à jour pour bénéficier des derniers correctifs
git pull origin main
pip install -r frontend/requirements.txt --upgrade
```

### Pour les Développeurs

#### 1. Ne Jamais Commiter de Fichiers Sensibles

Fichiers à TOUJOURS exclure de Git :
- `.token` - Token d'authentification
- `.env` - Variables d'environnement
- `config.local.py` - Configuration locale
- Credentials ou clés API

#### 2. Validation des Entrées

```python
# Toujours valider les entrées utilisateur
if option not in ["Scan", "Footprint", "Enum"]:
    print("Option invalide")
    return False
```

#### 3. Utilisation de Timeouts

```python
# Toujours définir des timeouts
requests.post(url, json=data, timeout=30)
subprocess.run(cmd, timeout=60)
```

#### 4. Gestion des Erreurs

```python
# Capturer et gérer les exceptions spécifiques
try:
    response = requests.post(...)
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.ConnectionError:
    print("Erreur de connexion")
```

## 🎯 Checklist de Sécurité

Avant de déployer ou utiliser :

- [ ] `.gitignore` est configuré correctement
- [ ] Aucun fichier `.token` n'est commité
- [ ] Aucune variable d'environnement sensible dans le code
- [ ] Tous les timeouts sont configurés
- [ ] Validation des entrées utilisateur en place
- [ ] Gestion d'erreurs appropriée
- [ ] Confirmation utilisateur avant actions critiques
- [ ] Logs ne contiennent pas d'informations sensibles

## 🔍 Audit de Sécurité

### Dernière Révision
- **Date** : 2025-12-18
- **Version** : 2.0.0
- **Auditeur** : Équipe MoussourisGPT

### Outils Recommandés

```bash
# Vérification des dépendances vulnérables
pip install safety
safety check -r frontend/requirements.txt

# Analyse statique du code
pip install bandit
bandit -r frontend/

# Vérification des secrets dans Git
pip install detect-secrets
detect-secrets scan
```

## 📚 Ressources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [CHANGELOG.md](frontend/CHANGELOG.md) - Historique des correctifs de sécurité

## ⚖️ Usage Éthique

⚠️ **IMPORTANT** : Cet outil est destiné uniquement à un usage éthique et légal.

### Autorisé
- ✅ Tests sur vos propres systèmes
- ✅ Pentesting avec autorisation écrite
- ✅ Recherche en sécurité éthique
- ✅ Formation et éducation

### Interdit
- ❌ Scan de systèmes sans autorisation
- ❌ Accès non autorisé
- ❌ Exploitation de vulnérabilités sans permission
- ❌ Toute activité illégale

**Avertissement** : L'utilisation non autorisée de cet outil peut enfreindre les lois locales et internationales. Les utilisateurs sont seuls responsables de leurs actions.

---

**Dernière mise à jour** : 2025-12-18
**Contact Sécurité** : security@moussourisgpt.com
