import os
import h5py
import pandas as pd
import numpy as np
from tqdm import tqdm

def extract_h5_data(file_path):
    try:
        with h5py.File(file_path, 'r') as h5_file:
            metadata = h5_file['metadata/songs'][:][0]
            artist_name = metadata['artist_name'].decode('utf-8')
            title = metadata['title'].decode('utf-8')
            song_id = metadata['song_id'].decode('utf-8')
            release = metadata['release'].decode('utf-8')
            genre = metadata['genre'].decode('utf-8') if 'genre' in metadata else "Unknown"
            song_hotttnesss = metadata['song_hotttnesss']

           
            analysis = h5_file['analysis/songs'][:][0]
            tempo = analysis['tempo']
            key = analysis['key']
            mode = analysis['mode']
            loudness = analysis['loudness']
            danceability = analysis['danceability']
            energy = analysis['energy']
            duration = analysis['duration']

            
            musicbrainz = h5_file['musicbrainz/songs'][:][0]
            year = musicbrainz['year']

            return {
                'File Path': file_path,
                'Song ID': song_id,
                'Title': title,
                'Artist': artist_name,
                'Release': release,
                'Genre': genre,
                'Song Hotttnesss': song_hotttnesss,
                'Duration': duration,
                'Tempo': tempo,
                'Key': key,
                'Mode': mode,
                'Loudness': loudness,
                'Danceability': danceability,
                'Energy': energy,
                'Year': year
            }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def process_dataset(root_dir, output_csv="MillionSongSubset.csv"):
    data = []

    
    for subdir, _, files in os.walk(root_dir):
        for file in tqdm(files):
            if file.endswith(".h5"):
                file_path = os.path.join(subdir, file)
                song_data = extract_h5_data(file_path)
                if song_data:
                    data.append(song_data)

   
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    print(f"CSV file saved as {output_csv}")

dataset_path = "MillionSongSubset"
process_dataset(dataset_path)
