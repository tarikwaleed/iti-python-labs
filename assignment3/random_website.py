import random
import webbrowser
websites = ["https://www.google.com", "https://www.github.com", "https://www.stackoverflow.com", "https://www.python.org"]
random_website = random.choice(websites)
webbrowser.open(random_website)
