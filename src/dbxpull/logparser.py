import sys
from re import compile, findall
def parse_logfile(
    filepath: str,
) -> list["str"]:
    filetext = open(filepath, 'r').read()
    redo_pattern = compile(r"\|(.*)\|")
    success_pattern = compile(r"<(.*)>")
    redos = findall(redo_pattern, filetext)
    success = findall(success_pattern, filetext)
    with open("Redos.txt", "w") as f:
        f.write("\n".join(redos))
    with open("Done.txt", "w") as f:
        f.write("\n".join(success))

def main():
    if len(sys.argv) > 1:
        parse_logfile(sys.argv[1])

if __name__ == "__main__":
    main()