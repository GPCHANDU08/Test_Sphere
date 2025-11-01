# tests/conftest.py
import sys
import os

# Put the project root (TestSpheree) onto sys.path so test imports work.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)