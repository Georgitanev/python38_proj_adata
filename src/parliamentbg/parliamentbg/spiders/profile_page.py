import os

import pandas as pd
import scrapy
from scrapy.selector import Selector

from ..items import ParliamentbgItem

# xml on 3013 not working properly. So use .xls files to get info.

# opening short names party dictionary
path = os.path.dirname(os.path.abspath(__file__))
parties_dictionary_file = os.path.join(path, "parties_dictionary.json")
xls_url = os.path.join(path, "MemberofParliament2797.xls")
parties_dictionary_df = pd.read_json(parties_dictionary_file, "r", "utf-8")
parties_dictionary = parties_dictionary_df.to_dict()


def extract_political_force(party=""):
    """extracts political force from dictionary record"""
    # get percents
    percents = party.split(" ")[-1]
    # get party name by excluding percents from string
    # at the end is + 1, because it removes last space, before percents too.
    political_force = party[: -int(len(percents) + 1)]
    return political_force


class QuotesSpider(scrapy.Spider):
    """Crawler for profile page with personal information"""

    name = "profile_page"
    start_urls = ['https://www.abv.bg/',
        # "https://parliament.bg/bg/MP/3013",
    ]

    def parse(self, response, **kwargs):
        items = ParliamentbgItem()
        # temporary not using parliament, because website not working
        selector = Selector(response)
        # xls_url = selector.xpath(
        #     '//*[@id="leftcontent-2"]/div[3]/div[2]/a[2]/@href'
        # ).get()
        #
        # xls_url = "https://parliament.bg" + xls_url

        # temporary because website not working
        df = pd.read_excel(xls_url)  # reading .xls from url
        df = df.where(pd.notnull(df), None)
        names = df.columns[1]  # get the name of column with names
        # get date of birth
        date_of_birth = \
        df.loc[df["Unnamed: 0"] == "Дата на раждане ", names].tolist()[0]
        try:
            place_of_birth = df["Unnamed: 2"][0] + " " + df["Unnamed: 3"][0]
        except Exception as ex:
            print(ex)
            place_of_birth = None
        # get profession
        profession = df.loc[df["Unnamed: 0"] == "Професия", names].tolist()[0]
        # get languages
        foreign_languages = df.loc[df["Unnamed: 0"] == "Езици", names].tolist()[
            0]
        # get_education
        edu_string = "Научна степен/академична длъжност"
        try:
            education = df.loc[df["Unnamed: 0"] == edu_string, names].tolist()[
                0]
        except Exception as ex:
            print(ex)
            education = None
        # get political party
        str_politics = "Избран(а) с политическа сила"
        party = df.loc[df["Unnamed: 0"] == str_politics, names].tolist()[0]
        party = extract_political_force(party)  # get percents off
        try:
            email = df.loc[df["Unnamed: 0"] == "E-mail", names].tolist()[0]
        except Exception as ex:
            print(ex)
            email = None

        items["name"] = names
        items["date_born"] = date_of_birth
        items["place_born"] = place_of_birth
        items["profession"] = profession
        items["lang"] = foreign_languages
        items["party"] = party
        items["email"] = email
        items["url"] = response.request.url[-11:]
        items["education"] = education
        items["pp"] = parties_dictionary[party]  # political party short version
        # date of birth short version
        items["dob"] = date_of_birth.replace("-", "")
        yield {
            "urls": items,
        }
