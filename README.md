# Malware_dev_RC4_File_Encryptor

## Developer

Name: Abraham Shimels
ID No: CTC-183-26

## Overview

This project encrypts the contents of a file using the RC4 stream cipher and provides a matching decryptor that restores the original content with the same key.

## Files

- `rc4_encryptor.py` - encrypts a file in place using RC4
- `rc4_decryptor.py` - decrypts the encrypted file using the same key
- `file.txt` - sample file used for testing

## Usage

1. Encrypt a file:
   ```bash
   python3 rc4_encryptor.py file.txt --key rc4-secret-key
   ```

2. Decrypt the file:
   ```bash
   python3 rc4_decryptor.py file.txt --key rc4-secret-key
   ```

## Notes

- The file is read and written in binary mode.
- The encryptor and decryptor use the same RC4 key.
- The same key must be supplied during decryption to restore the original file exactly.
