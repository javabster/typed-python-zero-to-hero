"""INTERMEDIATE — annotate this Playlist class and its supporting types."""


class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def display(self):
        mins, secs = divmod(self.duration_seconds, 60)
        return f"{self.title} — {self.artist} ({mins}:{secs:02d})"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.tags = {}
        self.cover_url = None

    def add(self, song):
        self.songs.append(song)

    def add_tag(self, tag, weight=1):
        self.tags[tag] = self.tags.get(tag, 0) + weight

    def total_duration(self):
        return sum(song.duration_seconds for song in self.songs)

    def by_artist(self, artist):
        return [song for song in self.songs if song.artist == artist]

    def merged_with(self, other):
        merged = Playlist(f"{self.name} + {other.name}")
        for song in self.songs + other.songs:
            merged.add(song)
        return merged


if __name__ == "__main__":
    p = Playlist("Focus")
    p.add(Song("Weightless", "Marconi Union", 485))
    p.add(Song("Nuvole Bianche", "Ludovico Einaudi", 366))
    p.add_tag("ambient", 2)
    print(f"{p.name}: {p.total_duration()}s across {len(p.songs)} songs")
