import os, sys
try:
    __import__(".sexy").menu()
except Exception as e:
    exit(str(e))