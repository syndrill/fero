# fero
fero (fēro), Sebuah _side-project_ untuk tugas di per-kuliah-an. Fero -> Steel -> Steal -> Scraping _got it?_.

## Untuk apa?
- Mengambil pranala (URL) dari sebuah portal atau mesin pencari
- banyak.

## Running
- Dependencies. `requests` is not optional, might be used in the future changes as replacement of builtin `urllib`.
```
flask
flask-bootstrap
beautifulsoup4
~requests~
```
- Quick Run
```
git clone https://github.com/zeroload/fero
cd fero
FLASK_APP=fero flask run
```

## API
- Scrapper
	- `POST`, `/api/scrapper/<plugin_name>/fetch`, `keyword=<keyword>`, should be GET
	- `GET`, ???
- Auth / ETA SOON (TM)

## Plugin system
It's a bit hacky and sketchy, but it works. How? long story short,
- create a new directory `plugins/` and a shiny new `__init__.py`.
- `load(app)`
this function will be called upon App initialization.
could be useful for 
- `fetch(keyword)` returns a `dict` array contains `title` and `url`, accept a single string as `keyword`.
- multiple keywords handled by calling `fetch(keyword)` multiple times.
```json
[
	{"title": "string", "url": "valid-url"},
	{"title": "string", "url": "valid-url"}
]
```
The plugin directory structure should be like this,
```
.
├── fero
│   ├── ...
│   ├── plugins
│   │   ├── googlesearch
│   │   │   ├── assets
│   │   │   │   └── ...
│   │   │   └── __init__.py
...
```

## TODO
- [ ] Unit Test or something (YEP WE NEED THIS ;D)
- [ ] Walk around for google search bot kicker :/
- [ ] A pagination handler or something in plugins
	- [X] Google, `start` parameter
	- [X] Yahoo, `b` parameter
	- [ ] Liputan6, lazy-load or something
- [ ] A working UI for the greater good

## Contributors
- Me
- Myself
- I