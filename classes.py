import os
import random
from fuzzywuzzy import fuzz


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points


class Game:
    def __init__(self, names_players, songs_path, num_):
        players = [Player(i) for i in names_players]
        self.players = {x.name: x for x in players}
        self.state = ''
        song_list = os.listdir(songs_path)
        self.songs = Songs(song_list, num_)

    def start(self):
        self.state = 'start'

    def end(self):
        self.state = 'end'
        big_score = float('-inf')
        names = ''

        for i in self.players.values():
            if big_score < i.score:
                big_score = i.score
                names = i.name
                ending_state = 'Победитель'
            elif big_score == i.score:
                names = names + ' ' + i.name
                ending_state = 'Ничья игроков'

        return f'{ending_state} {names} с {big_score} очками'

    # def add_score_player(self, name, points):
    #     self.players[name].score += points

    def add_points(self, name, points):
        try:
            self.players[name].score += points
        except KeyError :
            if name == 'None':
                return
            self.players[name] = Player(name)
            self.players[name].score += points


    def output_players_dictionary(self):
        a = ''
        for i in self.players:
            a += i + ' | ' + str(self.players[i].score) + '\n'
        a = a[:-1]
        return a

    def process_guess(self, guess, name):
        points = self.songs.calculatе_score(guess)
        self.add_points(name, points)


def get_author_name(song):
    song = song.replace('.mp3', '')
    if song.find('(') != -1:
        song = song[:song.find('(')]
    elif song.find('[') != -1:
        song = song[:song.find('[')]
    elif song.find('|') != -1:
        song = song[:song.find('|')]
    elif song.find('｜') != -1:
        song = song[:song.find('｜')]
    if song.find('Prod') != -1:
        song = song[:song.find('Prod')]

    author = ''
    name = ''
    if song.find('-') != -1:
        author, name = song.split('-', 1)
    elif song.find('–') != -1:
        author, name = song.split('–', 1)
    else:
        name = song
    return author, name


def get_random_elements(list_, num_elements):
    songs = []
    number = 0
    len_ = len(list_)  # 40
    for random_music in range(1, num_elements + 1):
        # if songs[] != os.listdir ()[random.randint(0, len_-1)]:
        number = random.randint(0, len_ - 1)
        song = list_[number]
        while song in songs:
            number = random.randint(0, len_ - 1)
            song = list_[number]
        songs.append(song)
    return songs


class Song:
    def __init__(self, link):
        self.url = None
        self.link = link
        self.author, self.name = get_author_name(link)


class Out(IndexError):
    pass


class Songs:
    def __init__(self, song_list, num_=10):
        self.number = 0
        self.song_list = get_random_elements(song_list, num_)
        self.current_song = Song(self.song_list[0])


    def next_song(self):
        self.number += 1
        try:
            self.current_song = Song(self.song_list[self.number])
            return self.current_song
        except IndexError:
            raise Out('byyyyyyyyyyyy')

    def calculatе_score(self, answer):
        author = fuzz.token_sort_ratio(self.current_song.author, answer)
        name = fuzz.token_sort_ratio(self.current_song.name, answer)
        full = fuzz.token_sort_ratio(self.current_song.author + ' ' + self.current_song.name, answer)
        if full >= 85:
            return 10
        elif name >= 85:
            return 8
        elif author >= 85:
            return 7
        else:
            return 0


def load_music(path, num):
    result = Songs(os.listdir(path=path), num_=num)
    return result


if __name__ == '__main__':
    game = Game(['chelik', 'Karim'], '.\\music\\')
    print('end')

