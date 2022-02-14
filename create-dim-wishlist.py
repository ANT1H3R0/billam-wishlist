import os

wishlistText = []
for filename in os.listdir("dim"):
    if filename != "billam-wishlist.txt":
        with open("dim/" + filename, "r") as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("//notes:") and not lines[i + 1].startswith("dimwishlist"):
                    line = line.strip()
                    while i < len(lines) and not lines[i + 1].startswith("dimwishlist"):
                        i += 1
                        if not lines[i].startswith("\n"):
                            line += " - " + lines[i].strip()
                    line += "\n"
                # if (not line.startswith(("title", "description", "//", "dimwishlist:")) and (line != "\n" or i != len(lines) - 1 and not lines[i + 1].startswith(("\n", "title", "description", "//", "dimwishlist")))):
                #     line = "//" + line
                wishlistText.append(line)
                i += 1
with open("dim/billam-wishlist.txt", "w") as f:
    for line in wishlistText:
        f.write(line)