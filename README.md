# TheMovieDB.org skill

# Register for Developer Account Here - https://developers.themoviedb.org/

## Usage:
* `find upcoming movies`
* `What movies are now playing`
* `tell me about robin williams`

## Installation

Clone the repository into your `~/.mycroft/skills` directory. Then install the
dependencies inside your mycroft virtual environment:

If on picroft just skip the workon part and the directory will be /opt/mycroft/skills

```
cd ~/.mycroft/skills
git clone https://github.com/eClarity/skill-tmdb.git TmdbSkill
workon mycroft
cd TmdbSkill
pip install -r requirements.txt
```


Add a block to your Mycroft configuration file like this:

```
  "TmdbSkill": {
    "api_key": "you api key goes here"
  }
```

