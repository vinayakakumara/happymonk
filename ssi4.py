import json

# Load the JSON file
with open('results.json', 'r') as json_file:
    data = json.load(json_file)
total_videos = len(data)
print(f"Total number of videos: {total_videos}")
for video_id, video_info in enumerate(data, start=1):
    frames = video_info['frames']
    frame_numbers = [frame['id'] for frame in frames]
    max_frame = max(frame_numbers)
    missing_frames = [i for i in range(1, max_frame + 1) if i not in frame_numbers]

    print(f"Video {video_id}:")
    print(f"Total frames: {max_frame}")
    if missing_frames:
        print(f"Missing frames: {missing_frames}")
    else:
        print("No missing frames")
for video_info in data:
    frames = video_info['frames']
    max_vehicles = max(frame['Vehicle count'] for frame in frames)
    max_people = max(frame['Person count'] for frame in frames)

    print(f"Video: {video_info['id']}")
    print(f"Max Vehicles: {max_vehicles}")
    print(f"Max People: {max_people}")
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
        print(f" - {person}")