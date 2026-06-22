# 🧷 Wrapifier

Tired of launching your Browser just to open any site ? **Wrapifier changes that completely!**
Instead of manually typing any sites and struggling, you can create full site ***wrappers*** in your
local machine.

📌 It looks *complex* but the reality is that its quite easy to setup and configure yourself, wrapifier
saves hours from your lives by giving you a **Compact** CLI to make website wrappers faster.

# ⚙️ Working

Intrested to know how it **works**? wrapifier uses the help of CLI interface to create compact ***PyQt6***
applications , the program automatically handles:

- **Customizing** based on your needs.
- **Creating** Source Copies
- **Building** a Executable file.

Well how is the program supposed to check if any site is **Valid** ? wrapifier uses ``requests`` to ping sites
from either ``http`` or ``https`` to check availability automatically.

Wrapifier creates **simple** source copies in your local machine, and gives you the access to them.
you can either use the source copies or build the program into a executable using wrapifier automatic
building.

# 💿 Installation

- **Create a Clone:**

     Start by cloning the repository:
     ```
     git clone https://github.com/Theboringboy-1/wrapifier.git
     cd wrapifier
     ```

- **Installing Dependencies:**

     Wrapifier uses a list of dependencies to work, you can either install them by:
     ```
     pip install -r requirements.txt
     ```
     Or if you are using **Window 10/11:**
     ```
     .\Scripts\dependencies.bat
     ```

- **Run:**

    Run the main file using:
    ```
    python commandline.py
    ```

# 🔨 Wrapping

_**Follow the Program Instructions. When the Ping Request arrive use either 1 or 2. this depends upon your website. if you have a valid
website that is not working, try both of them to see if any of them works.**_

_**Close the "Website Preview Window" to Continue Building the wrapper. The program will automatically guide you through the next steps.**_

# 🖥️ Tested Enviroments

- **Arch Linux**
- **Windows 10 and 11**
  (_Older versions of windows may not be supported: [Learn More](https://stackoverflow.com/questions/70937654/pyqt6-installation-on-windows-7-32-bit)_ )

# 🩹 Known Bugs

**Valid Websites Failure:**

Sometimes the Program doesn't recognize some valid websites, this is due to the ``requests`` we are looking forwared to fix it. Common sites include
_Vercel_ and other free hosting sites that are not compatible for now.

**Windows Shortcut Bug:**

Well, the shortcuts feature in the end of the Compiled (.exe) on windows may seem to be broken. the main issues are:

- _Shortcuts Icon not showwing on Desktop_
- _Provided (.png) will not have tranparency_

