import tempfile
from pathlib import Path
from src.crypto_tool import generate_key, load_key, encrypt_text, decrypt_text, encrypt_file, decrypt_file

def test_text_round_trip(tmp_path):
    key_path = tmp_path / "secret.key"
    generate_key(key_path); key = load_key(key_path)
    original = "Confidential internship message."
    token = encrypt_text(original, key)
    assert token != original
    assert decrypt_text(token, key) == original

def test_file_round_trip(tmp_path):
    key_path = tmp_path / "secret.key"
    generate_key(key_path); key = load_key(key_path)
    original, encrypted, restored = tmp_path / "plain.txt", tmp_path / "encrypted.bin", tmp_path / "restored.txt"
    original.write_text("Sensitive data for authorized testing.", encoding="utf-8")
    encrypt_file(original, encrypted, key); decrypt_file(encrypted, restored, key)
    assert restored.read_text(encoding="utf-8") == original.read_text(encoding="utf-8")
