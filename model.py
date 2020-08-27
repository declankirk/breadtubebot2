import markovify
from scraper import scrape

def update_model():
    print("Scraping posts...")
    scrape(500000)

    print("Building model...")
    with open('titles.txt', encoding='utf8') as f:
        titles = f.read()
    model = markovify.NewlineText(titles)

    print("Exporting model...")
    model_json = model.to_json()
    with open('model.json', 'w') as f:
        f.write(model_json)
    
    print("Done!")

update_model()