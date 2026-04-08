import argparse

parser = argparse.ArgumentParser(description="Script for invert words")
parser.add_argument("msg", help="User message")

args = parser.parse_args()

parser.add_argument("--invert", type=int, help="Idade do usuário")

if args.invert:
    print("Tá invertido")
if args.debug:
    print("Modo debug ativado.")
