import subprocess
import json

SONGS = []
CURRENT_SONG = None

def find_true_url(url):

    assert isinstance(url, str)
    
    out = subprocess.run(
        ["youtube-dl", "-j", "-f", "bestaudio", "-g", url],
        stdout=subprocess.PIPE)

    data = out.stdout.split(b"\n")
    url = data[0]
    title = json.loads(data[1])['title']
    return url, title


def add_song(url):

    playing = True
    
    for song in SONGS:
        if song['url'] == url:
            print(url, "already exists")
            return
        
    true_url, title = find_true_url(url)

    song = {
        'url': url,
        'true_url': true_url,
        'title': title,
    }

    SONGS.append(song)
    CURRENT_SONG = song


def play_song(index):
    if index >= len(SONGS):
        return "no such song"


def stop_song():
    pass


def pause_or_resume_song():
    pass


if __name__ == "__main__":
    inp = ""
    while inp != 'q':
        inp = input()
        if inp.startswith('a'):
            url = inp.split(' ')[1]
            add_song(url)
            continue

        if inp.startswith('s'):
            print(SONGS)
            continue

        
