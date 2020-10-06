import subprocess
import json
import csv
import os

LABELS_FILE  = 'data/class_labels_indices.csv'
DATASET_FILE = 'data/balanced_train_segments.csv'
YOUTUBE_BASE = 'https://www.youtube.com/watch?v='
NAMES = ['bark', 'yip', 'howl', 'growling', 'whimper (dog)', 'bow-wow']
IDS = ['/m/05tny_', '/m/07r_k2n', '/m/07qf0zm', '/m/0ghcn6', '/t/dd00136', '/m/07rc7d9']

def get_id(name):
    '''
    use the label file to get the corresponding id for the category
    '''

    with open(LABELS_FILE) as f:
        lines = csv.reader(f)
        for line in lines:
            display_name = line[2]
            if display_name.lower() == name.lower():
                    return line[1]
    return ''


def get_videos(name, cid):
    '''
    read csv that has the format
    youtube-id, start time, end time, classes
    into a list of dictionary elements specifying the url and start and end times
    '''

    videos = {}
    with open(DATASET_FILE) as f:
        lines = csv.reader(f)
        for line in lines:
            if len(line) < 4: continue
            for col in range(3, len(line)):
                positive_label = line[col].replace('\"', '') # remove quotation marks
                positive_label = positive_label.replace(' ', '') # remove spaces
                start_time = line[1].replace(' ','')
                end_time = line[2].replace(' ', '')
                ytid = line[0].replace(' ', '')
                if positive_label == cid:
                    url = YOUTUBE_BASE + ytid
                    d = {'url': url, 'tstart': start_time, 'tend': end_time, 'label': name}
                    videos[ytid] = d
    return videos
            
           
        
def download(url, folder):
    '''
    download the audio (webm file) from the video
    '''
    if not os.path.isdir(folder): os.mkdir(folder)
    command = ['youtube-dl', '-x', '--id', url]
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, cwd=folder)


def convert_and_split(filename):
    '''
    use your system's ffmpeg to convert to a wav file in segments
    '''
    command = ['ffmpeg', '-i', filename, '-f', 'segment', '-segment_time', '3', 'out%09d.wav']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)


def download_videos():
    '''
    use the csv to get the appropriate videos, then download
    '''
    for name, i in zip(NAMES, IDS):
        videos = get_videos(name, i)
        print(name, len(videos))

        with open(name + '_videos.json', 'w') as f:
            print(videos)
            json.dump(videos, f)
        
        #for video in videos:
        #    url = video['url']
        #    folder = 'data/videos/' + video['label']
        #    download(url, folder)

def extract_audio():
    pass

if __name__ == '__main__':
    download_videos()
    #convert_and_split('frenchtoast.webm')
    
