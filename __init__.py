# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


import tmdbsimple as tmdb

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests

__author__ = 'eClarity'

LOGGER = getLogger(__name__)

class TmdbSkill(MycroftSkill):
    def __init__(self):
        super(TmdbSkill, self).__init__(name="TmdbSkill")
	tmdb.API_KEY = self.config['api_key']

    def initialize(self):
	search_actor_intent = IntentBuilder("SearchActorIntent"). \
            require("SearchActorKeyword").build()
        self.register_intent(search_actor_intent,
                             self.handle_search_actor_intent)

        upcoming_intent = IntentBuilder("UpcomingIntent"). \
            require("UpcomingKeyword").build()
        self.register_intent(upcoming_intent,
                             self.handle_upcoming_intent)

	now_playing_intent = IntentBuilder("NowPlayingIntent"). \
            require("NowPlayingKeyword").build()
        self.register_intent(now_playing_intent,
                             self.handle_now_playing_intent)




    def handle_upcoming_intent(self, message):
    	movie = tmdb.Movies()
	response = movie.upcoming()
	for s in movie.results:
            self.speak(s['title'])

    def handle_now_playing_intent(self, message):
    	movie = tmdb.Movies()
	response = movie.now_playing()
	for s in movie.results:
            self.speak(s['title'])

    ## This intent is not ready for use ##
    def handle_search_actor_intent(self, message):
	search = tmdb.Search()
	response = search.person(query='Robin Williams')
	for s in search.results:
    	    self.speak(s['name'][0])

    def stop(self):
        pass


def create_skill():
    return TmdbSkill()
