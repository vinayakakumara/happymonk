import json

try:
    with open('results.json', 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("File 'results.json' not found.")
    data = []


#Script to encode and decode the JSON data
def encode_and_decode_json(data):
    encoded_data = json.dumps(data, indent=4)
    decoded_data = json.loads(encoded_data)
    return encoded_data, decoded_data


#Find the total number of videos in JSON
total_videos = len(data)
print(f"Total number of videos: {total_videos}")

# Find how many frames are there for each video and Find the missing frame in each video (if any)
for video_info in data:
    video_id = video_info['id']
    frames = video_info['frames']
    frame_ids = set(frame['id'] for frame in frames)
    max_frame = max(frame_ids)
    missing_frames = [frame_id for frame_id in range(1, max_frame + 1) if frame_id not in frame_ids]

    print(f"Video {video_id}:")
    print(f"Total frames: {max_frame}")
    if missing_frames:
        print(f"Missing frames: {missing_frames}")
    else:
        print("No missing frames")

#Find the maximum number of vehicles and people in each video
for video_info in data:
    video_id = video_info['id']
    frames = video_info['frames']

    max_vehicles = max(frame['Vehicle count'] for frame in frames)
    max_people = max(frame['Person count'] for frame in frames)

    print(f"Video {video_id}:")
    print(f"Maximum number of vehicles: {max_vehicles}")
    print(f"Maximum number of people: {max_people}")

#Find the number of categories of people and list the categories
categories = set()
for video_info in data:
    frames = video_info['frames']
    for frame in frames:
        if 'Face data' in frame:
            for person in frame['Face data']:
                categories.add(person['category'])

num_categories = len(categories)
category_list = list(categories)

print(f"Number of categories: {num_categories}")
print(f"Categories: {category_list}")

#Find the people belonging to each category
category_people = {category: [] for category in category_list}
for video_info in data:
    frames = video_info['frames']
    for frame in frames:
        if 'Face data' in frame:
            for person in frame['Face data']:
                category_people[person['category']].append(person)

# Print people in each category
for category, people in category_people.items():
    print(f"Category: {category}")
    for person in people:
        print(f" - Person: {person}")
