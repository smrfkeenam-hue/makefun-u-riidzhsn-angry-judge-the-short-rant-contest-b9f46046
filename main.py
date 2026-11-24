import os

ENTRY = "The office printer behaves itself all week, then jams at 4:59 PM on a Friday on the single page I actually need, and blinks at me like this is somehow my fault. I did not survive six years of school to lose a fistfight with a machine that has exactly one job and a blinking light for a personality."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
