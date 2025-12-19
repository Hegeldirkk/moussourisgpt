from .utils import menu
from .auth import register, login, logout, verify_otp, resend_otp
from .api import send_prompt
import argparse
import sys


def cli_mode():
    parser = argparse.ArgumentParser(
        prog="msrgpt",
        description="MSRGPT CLI - Interface en ligne de commande pour MoussourisGPT"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # register command
    subparsers.add_parser("register", help="Créer un compte")

    # verify command
    subparsers.add_parser("verify", help="Vérifier l'email avec le code OTP")

    # resend command
    subparsers.add_parser("resend", help="Renvoyer le code OTP par email")

    # login command
    subparsers.add_parser("login", help="Connexion à MsrGPT")

    # logout command
    subparsers.add_parser("logout", help="Déconnexion de MsrGPT")

    # run command avec des arguments propres
    run_parser = subparsers.add_parser("run", help="Exécuter un prompt")
    run_parser.add_argument(
        "-o", "--option",
        required=True,
        choices=["Scan", "Footprint", "Enum"],
        help="Option de scan (Scan, Footprint, Enum)"
    )
    run_parser.add_argument(
        "-p", "--prompt",
        required=True,
        help="Prompt à envoyer"
    )

    args = parser.parse_args()

    if args.command == "register":
        success = register()
        sys.exit(0 if success else 1)
    elif args.command == "verify":
        success = verify_otp()
        sys.exit(0 if success else 1)
    elif args.command == "resend":
        success = resend_otp()
        sys.exit(0 if success else 1)
    elif args.command == "login":
        success = login()
        sys.exit(0 if success else 1)
    elif args.command == "logout":
        success = logout()
        sys.exit(0 if success else 1)
    elif args.command == "run":
        success = send_prompt(args.option, args.prompt)
        sys.exit(0 if success else 1)

    return True


def main():
    # Vérifier si des arguments sont fournis
    if len(sys.argv) > 1:
        cli_mode()
        return

    # Mode interactif
    while True:
        menu()
        choice = input("Choix de numero: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            verify_otp()
        elif choice == "3":
            login()
        elif choice == "4":
            print("\n[bold cyan]Options disponibles:[/] Scan, Footprint, Enum")
            option = input("Option: ").strip()
            if option not in ["Scan", "Footprint", "Enum"]:
                print("[red]✗ Option invalide. Utilisez: Scan, Footprint ou Enum[/]")
                continue
            prompt = input("Prompt--->> ").strip()
            if prompt:
                send_prompt(option, prompt)
            else:
                print("[red]✗ Le prompt ne peut pas être vide[/]")
        elif choice == "5":
            logout()
        elif choice == "6":
            print("[cyan]Bye Bye[/]")
            sys.exit(0)
        else:
            print("[red]✗ Choix incorrect, veuillez réessayer ![/]")

if __name__ == "__main__":
    main()
