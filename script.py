from bs4 import BeautifulSoup

def search(path,tag_type, class_name):
    # Read the HTML code from the file with UTF-8 encoding and storing it in a list
    user_list = []
    with open(path, 'r', encoding='utf-8') as file:
        html_code = file.read()

    soup = BeautifulSoup(html_code, 'html.parser')
    divs = soup.find_all(tag_type, class_=class_name)

    for div in divs:
        content = div.text.strip()
        user_list.append(content)
        
    return user_list

def clean_data(data_list):
    cleaned_list = []
    for item in data_list:
        cleaned_item = item.replace('\n', '').replace(' Verified', '')
        cleaned_item = cleaned_item.strip()  # Remove leading/trailing white spaces
        if cleaned_item.strip():  # Remove empty lines
            cleaned_list.append(cleaned_item)
    return cleaned_list

def left_minus_right(left_list, right_list):
    new_list = []
    for left_element in left_list:
        if left_element not in right_list:
            new_list.append(left_element)
    return new_list

def right_minus_left(left_list, right_list):
    new_list = []
    for right_element in right_list:
        if right_element not in left_list:
            new_list.append(right_element)
    return new_list

def inner_list(left_list, right_list):
    new_list = []
    for left_element in left_list:
        if left_element in right_list:
            new_list.append(left_element)
    return new_list

def search_in_list(my_list, search_item):
    for index, item in enumerate(my_list):
        if item == search_item:
            return index  # or any other information you want to return
    return -1  # Return -1 if the element is not found


def outputList(list):
    for element in list:
        print(element)

class_name_follower = "x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"
class_name_following = "x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"

followers = clean_data(search('follower.html','div', class_name_follower ))
followings = clean_data(search('following.html','div', class_name_following))




print("# of followers" , len(followers))
print("# of followings" , len(followings))
print("")

print("\n\n\nlist of people that follow you but you don't\n")
outputList(left_minus_right(followers,followings))
print("\n\n\nlist of people that you follow but they don't\n" )
outputList(right_minus_left(followers,followings))
print("\n\n\nlist of people that you mutually follow\n")
outputList(inner_list(followers,followings))

# print(search_in_list(followers,"hannahgwm"))