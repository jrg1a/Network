# Basic Secure Command Server and Client

This project provides a rudimentary implementation of a secure command execution system, similar to SSH. A client sends encrypted commands to a server, which then executes them and returns the encrypted results.

**Warning**: This is a basic and educational implementation and should not be used in production or security-critical environments.

## Prerequisites

- Python 3.6+
- `cryptography` library

To install the required library, use:


```bash
pip install cryptography
```

### Notes

This implementation uses symmetric encryption (Fernet from the cryptography library) for both command and response encryption.
Real-world implementations, like SSH, use more advanced techniques including authentication, asymmetric encryption, and additional features. Always use trusted and tested solutions like SSH for real-world applications.
