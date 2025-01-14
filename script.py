from bs4 import BeautifulSoup


def search_all_usernames(path, tag_type, class_names):
    """
    Searches the HTML for all elements matching the specified tag type and class names.
    Extracts and returns the text content (usernames) from the matched elements.
    """
    user_list = []

    # Read the HTML content from the file
    with open(path, 'r', encoding='utf-8') as file:
        html_code = file.read()

    soup = BeautifulSoup(html_code, 'html.parser')

    # Search for all elements with the specified classes
    elements = soup.find_all(tag_type, class_=lambda c: c and all(
        cls in c.split() for cls in class_names))

    # Extract the text from each matched element
    for element in elements:
        username = element.text.strip()
        if username:  # Ensure the username is not empty
            user_list.append(username)

    return user_list


def clean_data(data_list):
    """
    Cleans the data list by removing unnecessary characters and empty items.
    """
    cleaned_list = []
    for item in data_list:
        cleaned_item = item.replace('\n', '').replace(' Verified', '').strip()
        if cleaned_item:  # Remove empty lines
            cleaned_list.append(cleaned_item)
    return cleaned_list


def left_minus_right(left_list, right_list):
    """
    Returns a list of elements in the left list that are not in the right list.
    """
    return [left_element for left_element in left_list if left_element not in right_list]


def right_minus_left(left_list, right_list):
    """
    Returns a list of elements in the right list that are not in the left list.
    """
    return [right_element for right_element in right_list if right_element not in left_list]


def inner_list(left_list, right_list):
    """
    Returns a list of elements that are common between the left and right lists.
    """
    return [left_element for left_element in left_list if left_element in right_list]


def output_list(title, data_list):
    """
    Prints a title and a numbered list of data.
    """
    print(f"\n{title}")
    print("=" * len(title))
    if data_list:
        for i, element in enumerate(data_list, start=1):
            print(f"{i}. {element}")
    else:
        print("No items found.")


# Class names
class_names = ['_ap3a', '_aaco', '_aacw', '_aacx', '_aad7', '_aade']

# Get followers and followings
followers = clean_data(search_all_usernames(
    'follower.html', 'span', class_names))
followings = clean_data(search_all_usernames(
    'following.html', 'span', class_names))

# Display stats
print("# of followers:", len(followers))
print("# of followings:", len(followings))

# Display results
print("\n\n\nlist of people that follow you but you don't\n")
output_list("People that follow you but you don't",
            left_minus_right(followers, followings))

print("\n\n\nlist of people that you follow but they don't\n")
output_list("People that you follow but they don't",
            right_minus_left(followers, followings))

print("\n\n\nlist of people that you mutually follow\n")
output_list("Mutual followers", inner_list(followers, followings))

# Search for a specific username
# Uncomment the next line to search for a specific username in the followers list
# print(search_in_list(followers, "hannahgwm"))
