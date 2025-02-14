import time
import random
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


def random_delay(min_time=1.5, max_time=3.0):
    """Pause for a random duration between min_time and max_time seconds."""
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)


def simulate_typing(page, selector, text):
    """
    Simulate human typing by sending characters one by one with random delays.
    Waits for the element to be available before typing.
    """
    page.wait_for_selector(selector)
    for char in text:
        page.type(selector, char)
        time.sleep(random.uniform(0.1, 0.3))


def login_instagram(page, username, password):
    """
    Automates Instagram login using human-like typing and delays.
    """
    page.goto("https://www.instagram.com/accounts/login/")
    # Wait for the login form to load
    page.wait_for_selector("input[name='username']", timeout=15000)

    # Simulate typing the username and password
    simulate_typing(page, "input[name='username']", username)
    random_delay(1, 2)
    simulate_typing(page, "input[name='password']", password)
    random_delay(1, 2)

    # Click the login button
    page.click("button[type='submit']")
    # Wait for the navigation or a key element (like the main nav) to appear
    page.wait_for_selector("nav", timeout=15000)
    random_delay(3, 5)


def scroll_modal(page, modal_selector, pause_time=1, max_scrolls=100):
    """
    Scrolls a modal (or any scrollable container) to load all its content.
    The function scrolls repeatedly until no new content loads or max_scrolls is reached.
    """
    last_height = None
    for _ in range(max_scrolls):
        # Scroll to the bottom of the modal
        page.evaluate(f'''
            () => {{
                const modal = document.querySelector('{modal_selector}');
                modal.scrollTop = modal.scrollHeight;
            }}
        ''')
        time.sleep(pause_time)
        new_height = page.evaluate(f'''
            () => {{
                const modal = document.querySelector('{modal_selector}');
                return modal.scrollHeight;
            }}
        ''')
        if new_height == last_height:
            break
        last_height = new_height


def extract_usernames_from_modal(page, modal_list_selector):
    """
    Extracts the usernames from the modal list HTML using BeautifulSoup.
    Adjust the selectors if Instagram updates their markup.
    """
    html = page.inner_html(modal_list_selector)
    soup = BeautifulSoup(html, "html.parser")
    usernames = []
    # Usually, usernames appear in <a> tags inside the modal list.
    for a in soup.find_all("a"):
        text = a.get_text().strip()
        if text:
            usernames.append(text)
    return usernames


def get_followers(page, profile_username):
    """
    Navigates to the profile, opens the followers modal, scrolls to load all entries,
    extracts the usernames, and then closes the modal.
    """
    page.goto(f"https://www.instagram.com/{profile_username}/")
    page.wait_for_selector("a[href$='/followers/']", timeout=15000)
    page.click("a[href$='/followers/']")
    page.wait_for_selector("div[role='dialog'] ul", timeout=15000)
    # Scroll the modal to load all followers
    scroll_modal(page, "div[role='dialog'] ul",
                 pause_time=random.uniform(1, 2), max_scrolls=100)
    followers = extract_usernames_from_modal(page, "div[role='dialog'] ul")
    # Close the modal (typically using the close button with aria-label 'Close')
    page.click("button[aria-label='Close']")
    random_delay(1, 2)
    return followers


def get_followings(page, profile_username):
    """
    Navigates to the profile, opens the following modal, scrolls to load all entries,
    extracts the usernames, and then closes the modal.
    """
    page.goto(f"https://www.instagram.com/{profile_username}/")
    page.wait_for_selector("a[href$='/following/']", timeout=15000)
    page.click("a[href$='/following/']")
    page.wait_for_selector("div[role='dialog'] ul", timeout=15000)
    # Scroll the modal to load all followings
    scroll_modal(page, "div[role='dialog'] ul",
                 pause_time=random.uniform(1, 2), max_scrolls=100)
    followings = extract_usernames_from_modal(page, "div[role='dialog'] ul")
    page.click("button[aria-label='Close']")
    random_delay(1, 2)
    return followings


def main(username, password):
    with sync_playwright() as p:
        # Launch in headful mode to simulate a real user (set headless=True for headless)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/112.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Apply stealth measures to help avoid detection
        stealth_sync(page)

        # Log into Instagram
        login_instagram(page, username, password)
        random_delay(3, 5)

        # Get followers and followings
        followers = get_followers(page, username)
        random_delay(2, 4)
        followings = get_followings(page, username)

        print(f"\n# of followers: {len(followers)}")
        print(f"# of followings: {len(followings)}")

        # Compare lists using set operations
        followers_set = set(followers)
        followings_set = set(followings)
        not_following_back = list(followers_set - followings_set)
        not_followed_back = list(followings_set - followers_set)
        mutual = list(followers_set & followings_set)

        print("\nPeople who follow you but you don't follow back:")
        if not_following_back:
            for i, user in enumerate(not_following_back, start=1):
                print(f"{i}. {user}")
        else:
            print("None")

        print("\nPeople you follow but they don't follow you back:")
        if not_followed_back:
            for i, user in enumerate(not_followed_back, start=1):
                print(f"{i}. {user}")
        else:
            print("None")

        print("\nMutual followers:")
        if mutual:
            for i, user in enumerate(mutual, start=1):
                print(f"{i}. {user}")
        else:
            print("None")

        browser.close()


if __name__ == "__main__":
    print("=== Instagram Follower Analyzer ===")
    insta_username = "eren_s20"
    insta_password = "Sm112233"
    main(insta_username, insta_password)
