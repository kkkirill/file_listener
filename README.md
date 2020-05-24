# Program for sending Telegram message on file update

Quick start:
1. Install python 3 [Official Site](https://www.python.org/). <br>
    (_IMPORTANT_. Check "Add Python to PATH")
    ![Installation Image](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)
2. Clone repository and enter folder:
    ```bash
    git clone git@github.com:kkkirill/file_listener.git
    cd file_listener
    ```
3. Create virtual environment:<br>
    ```bash
    python -m venv venv
    ```
4. Activate virtual environment:<br><br>
    _For Windows_:
    ```bash
    venv\Scripts\activate.bat
    ```
    _For Linux/OSX_:
    ```bash
    source venv/bin/activate
    ```
5. Install dependencies:<br>
    ```bash
    python -m pip install -r requirements.txt
    ```
6. Create Telegram Bot with [BotFather](https://telegram.me/BotFather) and copy HTTP API bot token:
![BotFather](https://habrastorage.org/webt/wo/5q/ol/wo5qol8zqfljoiv5qvpm83sm5ag.png)
7. Run program:<br>
    ```bash
    python main.py <filepath> <telegram_bot_token>
    ```
