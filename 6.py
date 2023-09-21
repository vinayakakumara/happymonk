import requests
import json


# Function to fetch and load JSON data from the API
def fetch_json_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []


# API URL
api_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch and load JSON data
data = fetch_json_data(api_url)


# 1. Script to encode and decode the JSON data
def encode_and_decode_json(data):
    encoded_data = json.dumps(data, indent=4)
    decoded_data = json.loads(encoded_data)
    return encoded_data, decoded_data


# 2. Find the number of users (assuming User ID is unique)
user_ids = set(task['userId'] for task in data)
num_users = len(user_ids)
print(f"Number of users: {num_users}")

# 3. Find the number of tasks for each user
tasks_per_user = {}
for task in data:
    user_id = task['userId']
    if user_id in tasks_per_user:
        tasks_per_user[user_id] += 1
    else:
        tasks_per_user[user_id] = 1

# 4. Find the number of completed and incomplete tasks for each user and rank them
completed_tasks_per_user = {}
incomplete_tasks_per_user = {}

for task in data:
    user_id = task['userId']
    completed = task['completed']

    if completed:
        if user_id in completed_tasks_per_user:
            completed_tasks_per_user[user_id] += 1
        else:
            completed_tasks_per_user[user_id] = 1
    else:
        if user_id in incomplete_tasks_per_user:
            incomplete_tasks_per_user[user_id] += 1
        else:
            incomplete_tasks_per_user[user_id] = 1

# Rank users by the number of completed tasks
ranked_users = sorted(completed_tasks_per_user.keys(), key=lambda x: completed_tasks_per_user[x], reverse=True)

print("Number of tasks for each user:")
for user_id in tasks_per_user:
    print(f"User {user_id}: {tasks_per_user[user_id]} tasks")

print("\nNumber of completed tasks for each user (ranked):")
for rank, user_id in enumerate(ranked_users, start=1):
    print(f"Rank {rank}: User {user_id} - Completed tasks: {completed_tasks_per_user[user_id]}")

print("\nNumber of incomplete tasks for each user:")
for user_id in incomplete_tasks_per_user:
    print(f"User {user_id}: {incomplete_tasks_per_user[user_id]} tasks")
