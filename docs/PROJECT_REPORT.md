# Encryption / Decryption Tool — Internship Project 3

## 1. Executive Summary
A Python command-line utility for protecting sensitive text and files using Fernet authenticated symmetric encryption.

## 2. Problem Statement
Sensitive information should be protected from unauthorized access. The tool generates an encryption key and uses it to encrypt and decrypt text and files.

## 3. Objectives
- Secure key generation
- Text encryption/decryption
- File encryption/decryption
- Authenticated integrity protection
- Automated validation

## 4. Technology Stack
Python 3, cryptography/Fernet, argparse, pathlib, pytest and Kali Linux.

## 5. Architecture
User → CLI → Cryptographic Functions → Fernet → Encrypted Output / Decrypted Output.

## 6. Workflow
1. Generate a key.
2. Load the authorized key for an operation.
3. Encrypt plaintext or file bytes.
4. Decrypt ciphertext with the same key.
5. Validate the round trip with tests.

## 7. Security Considerations
The encryption key is the primary secret and must remain private. The GitHub repository intentionally excludes the actual key generated during testing.

## 8. Testing
The implementation was tested using text and file round trips, followed by an automated pytest run.

## 9. Evidence
The `screenshots/` folder contains implementation evidence for key generation/text encryption, text decryption, file encryption/decryption and automated tests.

## 10. Limitations
This is an educational internship project, not an enterprise key-management platform.

## 11. Conclusion
The project demonstrates practical confidentiality, secure key handling, file protection, cryptographic API usage, CLI development and testing.
