# Simple-QR-Generator
Hobby project to generate simple QR codes from text or links.

## Building and Running

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### Option 1: Native Installation (Linux & Windows)
The easiest way to run the tool is to install it as a Python package.

1. Clone or download the repository.
2. Open your terminal (Linux) or Command Prompt/PowerShell (Windows).
3. Navigate to the project directory:
   ```bash
   cd Simple-QR-Generator
   ```
4. Install the package:
   ```bash
   pip install .
   ```
5. You can now run the generator from anywhere by typing:
   ```bash
   qrgenerator
   ```

### Option 2: Building Standalone Executables
If you want to build a standalone executable (`.exe` on Windows or a binary on Linux) that doesn't require installing Python on the target machine, you can use PyInstaller.

1. Install PyInstaller and the project dependencies:
   ```bash
   pip install pyinstaller qrcode pillow
   ```
2. Build the executable:
   - **On Linux:**
     ```bash
     pyinstaller --onefile --name qrgenerator qrgenerator/qr.py
     ```
     The binary will be located in the `dist/` folder as `qrgenerator`.
     
   - **On Windows:**
     ```cmd
     pyinstaller --onefile --name qrgenerator.exe qrgenerator\qr.py
     ```
     The executable will be located in the `dist\` folder as `qrgenerator.exe`.
