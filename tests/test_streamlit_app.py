from streamlit.testing.v1 import AppTest
from unittest.mock import patch
import pandas as pd
import streamlit_app

# Importing classes and functions from components/ directory.
from components.fixtures_section import FixturesSection
from components.social_media_section import SocialMediaSection
from components.stadiums_map_section import StadiumMapSection
from components.about_section import AboutSection
from components.connections import (
	firestore_connection,
	get_standings,
	get_stadiums,
	get_teams,
	get_top_scorers,
	get_news,
	get_league_statistics,
	get_min_round,
	get_max_round,
)


at = AppTest.from_file("streamlit_app.py", default_timeout=1000)
at.run()


def test_title_area():
	assert "Premier League Statistics / 2023-24" in at.title[0].value
	assert "Current Round: " in at.subheader[0].value


def test_tab_one():
	assert at.tabs[0].subheader[0].value == "League Statistics"
	assert at.tabs[0].subheader[1].value == "Current Standings"
	assert at.tabs[0].subheader[2].value == "Location of Stadiums"


def test_tab_two():
	assert at.tabs[1].subheader[0].value == "Top 5 Teams"
