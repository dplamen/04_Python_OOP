from project import Song


class Album:

    def __init__(self, name, songs=[]):
        self.name = name
        if type(songs) is not list:
            self.songs = [songs]
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        for s in self.songs:
            if s.name == song.name:
                return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = []
        result.append(f'Album {self.name}')
        for s in self.songs:
            result.append(f'== {s.get_info()}')
        return '\n'.join(result) + '\n'


