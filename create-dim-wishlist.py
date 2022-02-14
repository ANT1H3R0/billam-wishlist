import os

wishlistText = []
for filename in os.listdir("dim"):
    if filename != "billam-wishlist.txt":
        with open("dim/" + filename, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if (not line.startswith(("title", "description", "//", "dimwishlist:")) and (line != "\n" or i != len(lines) - 1 and not lines[i + 1].startswith(("\n", "title", "description", "//", "dimwishlist")))):
                    line = "//" + line
                wishlistText.append(line)
with open("dim/billam-wishlist.txt", "w") as f:
    for line in wishlistText:
        f.write(line)