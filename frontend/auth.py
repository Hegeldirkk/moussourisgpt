import requests
from rich import print
from .config import API_BASE, TOKEN_FILE
from getpass import getpass
import os

def resend_otp(email: str = None):
    """Renvoie le code OTP par email"""
    if not email:
        email = input("Email: ")

    try:
        reponse = requests.post(
            f"{API_BASE}/auth/otp/resend",
            json={"email": email},
            timeout=30
        )

        if reponse.status_code == 200 or reponse.status_code == 201:
            print("[green]✓ Code OTP renvoyé avec succès. Vérifiez votre email.[/]")
            return True
        else:
            error_msg = reponse.json().get('message', 'Erreur inconnue')
            print(f"[red]✗ Erreur: {error_msg}[/]")
            return False
    except Exception as e:
        print(f"[red]✗ Erreur: {e}[/]")
        return False

def register():
    print("[bold cyan]\n --- Création de compte ---[/]")
    fullname = input("Nom complet: ")
    pseudo = input("Pseudo: ")
    email = input("Email: ")
    password = getpass("Mot de passe: ")

    try:
        reponse = requests.post(
            f"{API_BASE}/auth/inscription",
            json={
                "fullname": fullname,
                "pseudo": pseudo,
                "email": email,
                "password": password
            },
            timeout=30
        )

        if reponse.status_code == 201:
            print("[green]✓ Compte créé avec succès ![/]")
            print("[yellow]📧 Un code OTP a été envoyé à votre email.[/]")

            # Proposer de vérifier directement
            verify_now = input("\n[cyan]Voulez-vous vérifier votre email maintenant? (oui/non): [/]").lower()
            if verify_now in ['oui', 'o', 'yes', 'y']:
                otp = input("Code OTP (reçu par email): ")
                return verify_otp_with_data(email, otp)
            return True
        else:
            error_msg = reponse.json().get('message', 'Erreur inconnue')

            # Si le compte existe déjà, proposer de renvoyer l'OTP
            if 'already' in error_msg.lower() or 'existe' in error_msg.lower():
                print(f"[yellow]⚠ {error_msg}[/]")
                resend = input("\n[cyan]Voulez-vous renvoyer le code OTP à cet email? (oui/non): [/]").lower()
                if resend in ['oui', 'o', 'yes', 'y']:
                    if resend_otp(email):
                        otp = input("Code OTP (reçu par email): ")
                        return verify_otp_with_data(email, otp)
            else:
                print(f"[red]✗ Erreur: Inscription avortée - {error_msg}[/]")

            return False
    except requests.exceptions.Timeout:
        print("[red]✗ Timeout: Le serveur ne répond pas[/]")
        return False
    except requests.exceptions.ConnectionError:
        print("[red]✗ Erreur de connexion au serveur[/]")
        return False
    except Exception as e:
        print(f"[red]✗ Erreur inattendue: {e}[/]")
        return False

def verify_otp_with_data(email: str, otp: str):
    """Vérifie l'OTP avec email et code fournis"""
    try:
        reponse = requests.post(
            f"{API_BASE}/auth/otp/verify",
            json={
                "email": email,
                "codeOTP": otp
            },
            timeout=30
        )

        if reponse.status_code == 200 or reponse.status_code == 201:
            print("[green]✓ Email vérifié avec succès. Vous pouvez maintenant vous connecter.[/]")
            return True
        else:
            error_msg = reponse.json().get('message', 'Erreur inconnue')
            print(f"[red]✗ Erreur: Vérification échouée - {error_msg}[/]")
            return False
    except requests.exceptions.Timeout:
        print("[red]✗ Timeout: Le serveur ne répond pas[/]")
        return False
    except requests.exceptions.ConnectionError:
        print("[red]✗ Erreur de connexion au serveur[/]")
        return False
    except Exception as e:
        print(f"[red]✗ Erreur inattendue: {e}[/]")
        return False

def verify_otp():
    """Vérifie l'OTP en demandant email et code"""
    print("[bold cyan]\n --- Vérification OTP ---[/]")
    email = input("Email: ")
    otp = input("Code OTP (reçu par email): ")
    return verify_otp_with_data(email, otp)

def login():
    print("[bold cyan]\n --- SE CONNECTER ---[/]")
    email = input("Email: ")
    password = getpass("Mot de passe: ")

    try:
        reponse = requests.post(
            f"{API_BASE}/auth/connexion",
            json={
                "email": email,
                "password": password
            },
            timeout=30
        )

        if reponse.status_code == 200:
            token = reponse.json().get('access_token')
            if token:
                save_token(token)
                print("[green]✓ Connexion réussie.[/]")
                return True
            else:
                print("[red]✗ Erreur: Token non reçu[/]")
                return False
        else:
            error_msg = reponse.json().get('message', 'Erreur inconnue')
            print(f"[red]✗ Erreur: Connexion échouée - {error_msg}[/]")
            return False
    except requests.exceptions.Timeout:
        print("[red]✗ Timeout: Le serveur ne répond pas[/]")
        return False
    except requests.exceptions.ConnectionError:
        print("[red]✗ Erreur de connexion au serveur[/]")
        return False
    except Exception as e:
        print(f"[red]✗ Erreur inattendue: {e}[/]")
        return False

def logout():
    try:
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
            print("[green]Déconnexion réussie[/]")
            return True
        else:
            print("[yellow]Vous n'êtes pas connecté[/]")
            return False
    except Exception as e:
        print(f"[red]Erreur lors de la déconnexion: {e}[/]")
        return False

def save_token(token):
    with open(TOKEN_FILE, 'w') as f:
        f.write(token)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
    return None

