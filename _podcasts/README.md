## Converting Notebook LM .mp4 to .mp3

```bash
ffmpeg -i input.mp4 -vn -acodec libmp3lame -q:a 2 output.mp3
``