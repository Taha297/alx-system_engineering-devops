#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL to query the Reddit API for the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define headers with a custom User-Agent
    headers = {
        "User-Agent": "custom-user-agent:script:v1.0 (by /u/yourusername)"
    }
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers from the response data
            return data["data"]["subscribers"]
        else:
            # If the subreddit is invalid or the status code is not 200, return 0
            return 0
    except Exception as e:
        # In case of any exception, return 0
        return 0

# Example usage:
# print(number_of_subscribers("python"))  # Replace "python" with any subreddit name

