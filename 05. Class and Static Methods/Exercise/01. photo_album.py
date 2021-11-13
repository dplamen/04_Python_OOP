class PhotoAlbum:
    _PHOTOS_PAGE = 4
    _SPLIT = 11

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // cls._PHOTOS_PAGE)

    def add_photo(self, label):
        page = 0
        while page < len(self.photos):
            if PhotoAlbum._PHOTOS_PAGE > len(self.photos[page]):
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
            page += 1
        return f"No more free slots"

    def display(self):
        split = '-' * PhotoAlbum._SPLIT
        page_info = []
        for page in self.photos:
            row = ' '.join(['[]' for x in page])
            page_info.append(row)
        result = split + '\n' + f'\n{split}\n'.join(page_info) + '\n' + split
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
