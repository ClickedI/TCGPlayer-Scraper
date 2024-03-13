import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By


def save_entry_text():
    global name
    name = entry.get()
    name = name.replace(" ", "+")

    driver.get(
        f"https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&Language=English&q={name}&view=grid")
    time.sleep(2)
    # Print a list of the prices of each individual item above
    name = name.replace("+", " ")
    print(name)
    for card in driver.find_elements(By.CLASS_NAME, "search-result__content"):
        rarity = card.find_element(By.CLASS_NAME, "search-result__rarity")
        price = card.find_element(By.CLASS_NAME, "inventory__price-with-shipping")
        print(rarity.text, "     ", price.text)

        cardLabel = tk.Label(text=name)
        cardLabel.pack()
        priceLabel = tk.Label(text=f"{rarity.text, "     ", price.text}")
        priceLabel.pack()






options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

window = tk.Tk()
window.title("TCG Player Scraper")
window.geometry("")
label = tk.Label( text="Type a Card Name")
entry = tk.Entry()
enterButton = tk.Button(text="*click here*", command=save_entry_text)
enterButton.pack()
label.pack()
entry.pack()

window.mainloop()
time.sleep(5)




