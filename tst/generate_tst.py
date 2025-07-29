import re
import shutil
from pathlib import Path

current_dir = Path(__file__).parent.resolve()
episodes_dir = current_dir.parent / "episodes"
defs_dir = current_dir / "defs"
code_dir = current_dir.parent / "code"
tst_dir = current_dir

# Regex to match code blocks of type gap, output, or error, supporting multiline
code_block_pattern = re.compile(
    r"```(gap|output|error)\s*\n(.*?)```", re.DOTALL | re.IGNORECASE
)

# Functions that require loading defs/functions.g
FUNCTIONS_REQUIRING_DEFS = [
    "AvgOrdOfCollection",
    "AvgOrdOfGroup"
]

# Decide whether to skip a GAP code block (skip if contains 'return' or only comments/empty lines)
def should_skip_block(lines):
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "return" in stripped:  
            return True
    return False

# Extract all filenames from Read("filename") statements within GAP code blocks
def extract_read_files(blocks):
    read_files = set()
    read_pattern = re.compile(r'Read\("([^"]+)"\)')
    for block_type, block_content in blocks:
        if block_type.lower() == "gap":
            matches = read_pattern.findall(block_content)
            for filename in matches:
                read_files.add(filename)
    return read_files

# Iterate over all .md files in episodes directory
for md_file in episodes_dir.glob("*.md"):
    # Skip the test file 04-testing.md
    if md_file.name.lower() == "04-testing.md":
        continue
    
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all code blocks, skip files without code blocks
    blocks = code_block_pattern.findall(content)  
    if not blocks:
        continue  

    # Generate .tst filename
    tst_filename = f"episodes{md_file.stem}.tst"  
    tst_path = tst_dir / tst_filename

    # Determine if we need to insert Read("defs/functions.g")
    need_definitions = False
    for block_type, block_content in blocks:
        if block_type.lower() == "gap":
            # If the code block contains any of the functions requiring defs, mark need_definitions True
            for func_name in FUNCTIONS_REQUIRING_DEFS:
                if func_name in block_content:
                    need_definitions = True
                    break
            if need_definitions:
                break
    
    # Extract all filenames that are read by the GAP blocks, for copying
    read_files = extract_read_files(blocks)
    
    # Copy each required file from code directory to tst directory
    for filename in read_files:
        src = code_dir / filename
        dst = tst_dir / filename
        if src.exists():
            try:
                shutil.copy2(src, dst)
                print(f"Copied {src} to {dst}")
            except Exception as e:
                print(f"Failed to copy {filename}: {e}")
        else:
            print(f"Warning: file {src} not found, cannot copy")
    
    # Write the .tst file
    with open(tst_path, "w", encoding="utf-8") as tst_file:
        # Insert Read("defs/functions.g") at the top if needed
        if need_definitions:
            tst_file.write(f'gap> Read("defs/functions.g");\n\n')

        i = 0
        while i < len(blocks):
            block_type, block_content = blocks[i]
            block_type = block_type.lower()
            block_content = block_content.strip()

            if block_type == "gap":
                lines = block_content.splitlines()
                # Skip GAP blocks containing 'return'
                if should_skip_block(lines):
                    i += 1
                    continue
                
                # Write GAP prompt structure: first line prefixed with "gap>", following lines with ">"
                if lines:
                    first_line = lines[0]
                    if first_line.startswith("gap> "):
                        first_line = first_line[len("gap> "):]
                    elif first_line.startswith("> "):
                        first_line = first_line[len("> "):]
                    tst_file.write(f"gap> {first_line}\n")

                    for line in lines[1:]:
                        if line.startswith("gap> "):
                            line = line[len("gap> "):]
                        elif line.startswith("> "):
                            line = line[len("> "):]
                        tst_file.write(f"> {line}\n")

                # If the next block is output or error, write its content as is
                if i + 1 < len(blocks) and blocks[i + 1][0].lower() in ("output", "error"):
                    next_content = blocks[i + 1][1].strip().splitlines()
                    for line in next_content:
                        if line.strip():
                            tst_file.write(f"{line.strip()}\n")
                    i += 1  # Skip the next block since it has been processed

            i += 1

    print(f"Generated: {tst_filename}")