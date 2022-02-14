import os

urls = ""
for filename in os.listdir("dim"):
    urls += "https://raw.githubusercontent.com/ANT1H3R0/billam-wishlist/master/dim/" + filename + " | "
urls = urls[:-3]
with open("README.md", "w") as f:
    f.write(urls)
print(urls)