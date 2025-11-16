import requests
import pandas as pd

url = "https://api.reccobeats.com/v1/audio-features"

payload = {}

# List of track IDs (Spotify or ReccoBeats IDs), between 1 and 40
track_ids = [
    '27x2IrIGwr56QWkqJ4cu9I', '2ae0eMqiUrP2rjxCVn2w0C', '5H1sKFMzDeMtXwND3V6hRY', '6nLhNKMwty3wrnldjqZdva', 
    '3uwnmxmJvk8WfNa4RzqcT7', '12wSL3tGk3MtbDEhfG7xy3', '5DmLFST9kbQ932k5far6Rl', '01OsqJH26GLI5jmZZ6PKIh', 
    '0wFU2pYHZi45Ws1VD6aSJX', '3vC63Nh3rSREo7qDHgnx8I', '78w38QMvXYulFfP6AKFVdk', '2Sprbw65iHnDNsmgbSoH7C', 
    '4L43LBtfaYIFH1ECv3Xxyz', '71GUKQjcWH7THE1Fxbopai', '4Cv1YTkESvHPWnQAtVNoBF', '3598iBWrS4JhJqP5tHlpVK', 
    '0OnWu3G0i9Kg4Mqha5QvvH', '0cBbQqxqZV1nQfdxpDTQRa', '7ctnnGF43JNYGgmMawaoGn', '5DO7rqTWMnC9Q7pB4PtfWR', 
    '6i9m5Y9yUfRgjVnnBooX3q', '78qFR4ah1s7wY3f6qdcnDL', '0YgvF6fNWydNGzCY3pzK4Y', '5S0QxfYABBoLI4sMk2aCa2', 
    '4s31m7ZtBWsK3BfndIGP4E', '6cesZZFaBFa4Nj5U2mFtdt', '3TFCPkwhrH1E47OoJuN4hP', '55lijDD6OAjLFFUHU9tcDm', 
    '3m3aEs2NUwzCPmOG0SXeBt', '2YkjXEab4USTV9uuAgC90E', '0vB9kOqmrTzT8grUQPmXWZ', '1v3Gt3XJlZOXyuNz3CLnDf', 
    '3BYXAVdufZAL3NQZAqw3xR', '4QBOrUzS58mB6186LSuzUH', '5YbgcwHjQhdT1BYQ4rxWlD', '6NarlZxW2farAip5P0Ig9p'
]

params = {
    'ids': ','.join(track_ids)
}

headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, params=params)

data = response.json()
filtered_features = []
for track in data['content']:
    filtered = {
        'id': track.get('id'),
        'valence': track.get('valence'),
        'danceability': track.get('danceability'),
        'energy': track.get('energy')
    }
    filtered_features.append(filtered)

filtered_high_valence = [track for track in filtered_features if track['valence'] > 0.7]

df_ff = pd.DataFrame(filtered_features)

df_fhv = pd.DataFrame(filtered_high_valence)

print("Features (All)")
print(df_ff)

print(">0.7 Valence")
print(df_fhv)
#print(response.text)