# Arcaea Utilities
![Arcaea Banner](https://shorturl.at/jV1sH)

This is a set of utility tools made for modding the game [Arcaea](https://arcaea.lowiro.com/en) by lowiro. This repo will not ⚠️ contain any copyrighted ©️ materials, so you'd have to figure out yourself where to get the raw downloaded song data.

Before you run anything, you must ensure the `rawData` folder is properly formatted. The `rawData` folder should contain the following sub-directories:
```
rawData/
├── songs/
│   ├── songname/         (folder for each song)
│   └── songlist          (JSON file containing song list)
└── dl/
    ├── songname          (large file, music file.ogg)
    ├── songname_0        (PST Chart.aff)
    ├── songname_1        (PRS Chart.aff)
    ├── songname_2        (FTR Chart.aff)
    ├── songname_3        (BYD Chart.aff)
    └── songname_4        (ETR Chart.aff)
```

## songFolderOrganizer.py
`Arcaea` Stores its song and charts files in a really messy format but we can classify them into two categories of songs - ones that already come with the game itself, which are `Arcaea` songpack default songs. The other type is songs that are in the extension songpacks, such as `World Extend`, `MuseDash`, `Rotaeno`, etc. which need to be downloaded from the Arcaea servers after signing in with an account that has purchased these packs.

In the `songs` folder, even though the entire catalogue of songs can be found, however, as mentioned, the second type of songs will not have their charts or audio downloaded. Instead, they have a `dl_` prefix in front of their song folder name. The downloaded files exist in the `dl` folder, and the files do not have any valid file extensions, therefore we need to determine the file types by their filenames. 

This script will organize the song folders in the `songs` folder by moving the downloaded files to the `song` folder and renaming them to their original name.

After running, everything will be moved to the `organizedSongs` folder, and the `songs` folder will be empty.

```
organizedSongs/
├── songid/
│   ├── 1080_base.jpg       (already exists)
│   ├── 1080_base_256.jpg   (already exists)
│   ├── base.ogg
│   ├── preview.ogg         (already exists)
│   ├── 0.aff
│   ├── 1.aff
│   ├── 2.aff
│   ├── 3.aff               (optional)
│   ├── 4.aff               (optional)
│   └── additional unimportant video files...
├── songlist
├── packlist
└── unlocks
```
