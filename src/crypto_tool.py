#!/usr/bin/env python3
"""Fernet authenticated symmetric encryption helpers."""
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

def generate_key(key_path: str = "output/secret.key") -> Path:
    path = Path(key_path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(Fernet.generate_key())
    try: path.chmod(0o600)
    except PermissionError: pass
    return path

def load_key(key_path: str) -> bytes:
    path = Path(key_path)
    if not path.exists(): raise FileNotFoundError(f"Key not found: {path}")
    return path.read_bytes().strip()

def encrypt_text(plaintext: str, key: bytes) -> str:
    return Fernet(key).encrypt(plaintext.encode("utf-8")).decode("utf-8")

def decrypt_text(token: str, key: bytes) -> str:
    try: return Fernet(key).decrypt(token.encode("utf-8")).decode("utf-8")
    except InvalidToken as exc: raise ValueError("Decryption failed: invalid key or modified ciphertext.") from exc

def encrypt_file(input_path: str, output_path: str, key: bytes) -> Path:
    src, dst = Path(input_path), Path(output_path); dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(Fernet(key).encrypt(src.read_bytes())); return dst

def decrypt_file(input_path: str, output_path: str, key: bytes) -> Path:
    src, dst = Path(input_path), Path(output_path); dst.parent.mkdir(parents=True, exist_ok=True)
    try: dst.write_bytes(Fernet(key).decrypt(src.read_bytes()))
    except InvalidToken as exc: raise ValueError("Decryption failed: invalid key or modified ciphertext.") from exc
    return dst
