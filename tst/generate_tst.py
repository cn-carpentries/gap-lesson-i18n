import re
from pathlib import Path

# Assuming 'episodes/' and 'tst/' are sibling directories
# Get the current script directory (this script is in tst/)
current_dir = Path(__file__).parent.resolve()

# Path to the 'episodes' directory (one level up)
episodes_dir = current_dir.parent / "episodes"

# Output .tst files will be written to the current directory
tst_dir = current_dir

# Regex pattern to extract ```gap and ```output code blocks
code_block_pattern = re.compile(
    r"```(gap|output)\s*\n(.*?)```", re.DOTALL | re.IGNORECASE
)

# Loop through all .md files in episodes/
for md_file in episodes_dir.glob("*.md"):
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract all code blocks as (block_type, block_content) tuples
    blocks = code_block_pattern.findall(content)

    # Pair gap and output blocks
    paired_blocks = []
    i = 0
    while i < len(blocks) - 1:
        type1, content1 = blocks[i]
        type2, content2 = blocks[i + 1]
        if type1.lower() == "gap" and type2.lower() == "output":
            paired_blocks.append((content1.strip(), content2.strip()))
            i += 2  # Skip the matched pair
        else:
            i += 1  # Keep looking

    if not paired_blocks:
        continue  # Skip if no valid pairs

    # Create a .tst file with the same name as the .md file
    tst_filename = f"episodes{md_file.stem}.tst"
    tst_path = tst_dir / tst_filename

    with open(tst_path, "w", encoding="utf-8") as tst_file:
        for gap_code, output in paired_blocks:
            gap_lines = gap_code.splitlines()
            output_lines = output.splitlines()

            for line in gap_lines:
                line = line.strip()
                if line:
                    tst_file.write(f"gap> {line}\n")

            for line in output_lines:
                line = line.strip()
                if line:
                    tst_file.write(f"{line}\n")

    print(f"Generated: {tst_filename}")
