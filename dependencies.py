from melodia.core.track import Track
from melodia.music import chord
from melodia.io import midi

track = Track(signature=(4, 4))

track.add(chord.maj('C3', (1, 1)))
track.add(chord.maj('D3', (1, 1)))
track.add(chord.min('A3', (1, 1)))
track.add(chord.maj7('G3', (1, 1)))

with open('chords.mid', 'wb') as f:
    midi.dump(track, f)
