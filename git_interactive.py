#!/usr/bin/env python3
import os
import subprocess

def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def run_command(cmd, success_msg=None):
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
        if result.stdout:
            print(colorize(result.stdout.strip(), '36'))  # Cyan
        if success_msg:
            print(colorize(success_msg, '32'))  # Green
    except subprocess.CalledProcessError as e:
        print(colorize(e.stderr.strip(), '31'))  # Red

def main():
    print(colorize(">> Dodawanie plików do gita...", '34'))
    run_command("git add .", "Pliki dodane do indeksu.")

    msg = input(colorize(">> Podaj opis commita: ", '33'))
    run_command(f'git commit -m "{msg}"', "Zatwierdzono zmiany.")

    print(colorize(">> Status repozytorium:", '34'))
    run_command("git status")

    confirm = input(colorize(">> Czy chcesz wypchnąć zmiany? (t/n): ", '33')).lower()
    if confirm == 't':
        run_command("git push", "Zmiany wypchnięte na zdalne repozytorium.")
    else:
        print(colorize(">> Zmiany nie zostały wypchnięte.", '31'))

if __name__ == "__main__":
    main()
