from os import path
import PyInstaller.__main__

WORKING_DIR = path.abspath(path.join(path.dirname(__file__), "..")) 

PyInstaller.__main__.run([
    path.join(WORKING_DIR, "main.py"),
    "--onefile",
    "--windowed"
])