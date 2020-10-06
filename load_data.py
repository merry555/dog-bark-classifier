import subprocess
import csv

LABELS_FILE = 'data/class_labels_indices.csv'
DATASET_FILE = 'data/balanced_train_segments.csv'

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
    return ""


def get_videos(name, cid):
    '''
    read csv that has the format
    youtube-id, start time, end time, classes
    into a list of dictionary elements specifying the url and start and end times
    '''

    videos = []
    with open(DATASET_FILE) as f:
        lines = csv.reader(f)
        for line in lines:
            if len(line) < 4: continue
            for col in range(3, len(line)):
                positive_label = line[col].replace('\"', '') # remove quotation marks
                positive_label = positive_label.replace(' ', '') # remove spaces
                if positive_label == cid:
                    d = {'ytid': line[0], 'tstart': line[1], 'tend': line[2], 'label': name}
                    videos.append(d)
    return videos
            
           
        
def download_videos(urls):
    '''
    download the audio (webm file) from each video from a list of urls
    '''
    for url in urls:
        command = ['youtube-dl', '-x', url]
        subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

def convert_and_split(filename):
    '''
    use your system's ffmpeg to convert to a wav file in segments
    '''
    command = ['ffmpeg', '-i', filename, '-f', 'segment', '-segment_time', '15', 'out%09d.wav']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)


def main():
    names = ['bark', 'yip', 'howl', 'growling', 'whimper (dog)', 'bow-wow']
    ids = ['/m/05tny_', '/m/07r_k2n', '/m/07qf0zm', '/m/0ghcn6', '/t/dd00136', '/m/07rc7d9']

    for name, i in zip(names, ids):
        videos = get_videos(name, i)
        print(name, len(videos))
        download_videos(videos)

if __name__ == '__main__':
    main()
    #convert_and_split('frenchtoast.webm')
    
