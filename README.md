# disrupp.me
#### because every startup needs a start


# App

# Preprocessing
Data Preprocessing involves scraping seed-db for startup names and cleaning the
company names so that it can be easily used by our markov chain. To run the
preprocessor, simply navigate to the `preprocessing` folder and type in the
following command:

```
scrapy crawl seed_db -o items.json
```

This will export all the company names, along with their link on the seed-db
website into a json file named items.json. Make sure to delete the json file
everytime you rescrape the company names.

a project by Antares Chen and Sam Choi
