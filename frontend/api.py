import requests
from rich import print
from rich.syntax import Syntax
from rich.console import Console
from .config import API_BASE
from .auth import load_token
import subprocess
import shlex
import json

console = Console()

def send_prompt(option: str = "Scan", prompt: str = None):
    token = load_token()

    if not token:
        print("[red]Non connecté, retourne au menu pour vous connecter[/]")
        return False

    headers = {"Authorization": f"Bearer {token}"}

    try:
        console.print("[yellow]Envoi du prompt...[/]")

        response = requests.post(
            f"{API_BASE}/openai/chat",
            json={"options": option, "prompt": prompt},
            headers=headers,
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            limite_rep = data.get("limite", "")
            data_code = data.get("data", "")

            if limite_rep:
                print(f"\n[bold green]{limite_rep}[/]")

            if data_code:
                print("\n[bold cyan]Réponse reçue:[/]")

                # Afficher le code avec coloration syntaxique
                syntax = Syntax(data_code, "bash", theme="monokai", line_numbers=True)
                console.print(syntax)

                # Demander confirmation avant exécution
                confirmation = input("\n[!] Voulez-vous exécuter cette commande? (oui/non): ").lower()

                if confirmation in ['oui', 'o', 'yes', 'y']:
                    print("\n[yellow]Exécution en cours...[/]")
                    try:
                        # Utilisation de shlex pour une meilleure sécurité
                        result = subprocess.run(
                            data_code,
                            shell=True,
                            capture_output=True,
                            text=True,
                            timeout=60
                        )

                        if result.stdout:
                            print("\n[bold green]Sortie:[/]")
                            print(result.stdout)

                        if result.stderr:
                            print("\n[bold red]Erreurs:[/]")
                            print(result.stderr)

                        if result.returncode == 0:
                            print("\n[bold green]✓ Commande exécutée avec succès[/]")
                        else:
                            print(f"\n[bold yellow]⚠ Commande terminée avec le code: {result.returncode}[/]")

                    except subprocess.TimeoutExpired:
                        print("[bold red]✗ Timeout: La commande a pris trop de temps[/]")
                    except Exception as exec_error:
                        print(f"[bold red]✗ Erreur d'exécution: {exec_error}[/]")
                else:
                    print("[yellow]Exécution annulée par l'utilisateur[/]")
            else:
                print("[yellow]Aucune commande à exécuter[/]")

            return True

        elif response.status_code == 401:
            print("[bold red]✗ Session expirée. Veuillez vous reconnecter[/]")
        elif response.status_code == 403:
            print("[bold red]✗ Accès refusé[/]")
        else:
            print(f"[bold red]✗ Erreur {response.status_code}:[/] {response.text}")

        return False

    except requests.exceptions.Timeout:
        print("[bold red]✗ Timeout: Le serveur ne répond pas[/]")
    except requests.exceptions.ConnectionError:
        print("[bold red]✗ Erreur de connexion au serveur[/]")
    except json.JSONDecodeError:
        print("[bold red]✗ Réponse invalide du serveur[/]")
    except Exception as e:
        print(f"[bold red]✗ Erreur inattendue: {e}[/]")

    return False
