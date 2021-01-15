import subprocess
import json

SONGS = []

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

        if song['playing'] == 1:
            playing = False
        
        
    true_url, title = find_true_url(url)

    SONGS.append({
        'url': url,
        'true_url': true_url,
        'title': title,
        'playing': playing
    })


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

        
