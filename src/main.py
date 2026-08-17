#!/usr/bin/env python3
from pathlib import Path
import argparse
from crypto_tool import generate_key, load_key, encrypt_text, decrypt_text, encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(description="Internship Project 3 - Encryption / Decryption Tool")
    sub = parser.add_subparsers(dest="command", required=True)
    p_key = sub.add_parser("generate-key", help="Generate a Fernet key"); p_key.add_argument("-o", "--output", default="output/secret.key")
    p_enc = sub.add_parser("encrypt-text", help="Encrypt text"); p_enc.add_argument("text"); p_enc.add_argument("-k", "--key", default="output/secret.key")
    p_dec = sub.add_parser("decrypt-text", help="Decrypt a Fernet token"); p_dec.add_argument("token"); p_dec.add_argument("-k", "--key", default="output/secret.key")
    p_ef = sub.add_parser("encrypt-file", help="Encrypt a file"); p_ef.add_argument("input"); p_ef.add_argument("output"); p_ef.add_argument("-k", "--key", default="output/secret.key")
    p_df = sub.add_parser("decrypt-file", help="Decrypt a file"); p_df.add_argument("input"); p_df.add_argument("output"); p_df.add_argument("-k", "--key", default="output/secret.key")
    args = parser.parse_args()
    if args.command == "generate-key": print(f"[+] Key generated: {generate_key(args.output)}")
    elif args.command == "encrypt-text": print("[+] Encrypted token:\n" + encrypt_text(args.text, load_key(args.key)))
    elif args.command == "decrypt-text": print("[+] Decrypted text:\n" + decrypt_text(args.token, load_key(args.key)))
    elif args.command == "encrypt-file": print(f"[+] Encrypted file: {encrypt_file(args.input, args.output, load_key(args.key))}")
    elif args.command == "decrypt-file": print(f"[+] Decrypted file: {decrypt_file(args.input, args.output, load_key(args.key))}")

if __name__ == "__main__":
    main()
