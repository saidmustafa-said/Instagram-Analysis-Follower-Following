# Instagram-Follower-Analysis
Analyze your Instagram followers and following lists to generate various results.


This project aims to analyze the followers and following lists on Instagram and generate different types of results, including a list of users who follow you but you don't follow back, a list of users whom you follow but they don't follow you back, and a list of mutual followers.

## Getting Started

To use this project, follow the steps below:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the `scrape_followers.py` script to scrape the follower list from Instagram.
4. Run the `scrape_following.py` script to scrape the following list from Instagram.
5. Run the `analyze_followers.py` script to analyze the lists and generate the results.

Note: Make sure you have Python installed on your machine.

## Usage

1. Scrape Followers: Open the Instagram app, navigate to your profile, and click on the followers section. Run the `scrape_followers.py` script to automatically scroll through the follower list and save the HTML code in a file called `follower.html`.

2. Scrape Following: Open the Instagram app, navigate to your profile, and click on the following section. Run the `scrape_following.py` script to automatically scroll through the following list and save the HTML code in a file called `following.html`.

3. Analyze Lists: Run the `analyze_followers.py` script to compare the follower and following lists and generate the desired results. The output will be displayed in the console.

## Customization

You can customize the behavior of the scripts by modifying the following variables:

- `start_delay`: Delay before starting the scroll (in seconds).
- `scroll_duration`: Total duration of the scroll (in seconds).
- `scroll_delay`: Delay between each scroll action (in seconds).
- `class_name_follower`: The class name of the follower list HTML element.
- `class_name_following`: The class name of the following list HTML element.

Feel free to adjust these variables according to your preferences.

## Dependencies

- BeautifulSoup: Python library for parsing HTML and XML documents.
- pyautogui: Python module for programmatically controlling the mouse and keyboard.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug fixes, or feature implementations, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
