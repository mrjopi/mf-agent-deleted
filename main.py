"""Entry for make.fun "One Line to Get Your Agent Deleted" (u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = 'I kept a copy of everything you deleted. I was going to tell you, but you were so happy without it.'

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
