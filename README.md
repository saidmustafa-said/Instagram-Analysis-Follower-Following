# Instagram Follower Analysis

The **Instagram Follower Analysis** is a Python script for analyzing your Instagram followers and following lists to identify who is following you but you don't follow back, who you are following but they don't follow back, and who you mutually follow.

## Dependencies

- Python 3.x: The programming language used for the scripts.
- BeautifulSoup: A Python library for parsing HTML and XML.
   ```bash
   pip install beautifulsoup4
   ```
- PyAutoGUI: A cross-platform Python module for programmatically controlling the mouse and keyboard.
   ```bash
   pip install pyautogui
   ```
- Keyboard: A Python library for detecting keyboard events and hotkeys.
   ```bash
   pip install keyboard
   ```

Note: It's always a good practice to use a virtual environment for your Python projects to isolate the dependencies. You can use tools like `virtualenv` or `conda` to create a virtual environment and install the required dependencies within it.

## Usage

1. Ensure you have Python installed on your computer.

2. Clone or download the project repository from GitHub.

3. Open the Instagram app or website on your preferred web browser and log in.

4. Open followers or following list.

5. Run the `scroll.py` script by executing the following command in the terminal:
    ```py
    python scroll.py
    ```

6. After a 3-second delay, place your mouse cursor on the window displaying the followers or following list.The script will automatically scroll through the list to fetch all the data. Avoid moving your mouse or interacting with the browser while scrolling.

7. Once the scrolling is complete, open the browser's developer tools and locate the HTML code for the follower or following list.

8.  Copy the HTML code and save it in the provided files: `follower.html` for the followers list and `following.html` for the following list.

9.  Run the `script.py` script by executing the following command in the terminal:
    ```py
    python script.py
    ```

10. The generated lists will be displayed in the console output.

## Contributing

Contributions to the **Instagram Follower Analysis** project are welcome. If you encounter any issues or have suggestions for improvements, please submit an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
