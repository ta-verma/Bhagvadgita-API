from lxml import html
import requests
from bs4 import BeautifulSoup

####################################################################
# API
####################################################################

class Bhagvadgita:

	@staticmethod
	def get_by_chapter_and_verse(chapter_number, veser_number):

		url = "https://bhagavadgita.io/chapter/{}/verse/{}/hi/".format(str(chapter_number), str(veser_number))
		soup = BeautifulSoup(requests.get(url).content, 'html.parser')

		sanskrit = (str(soup.find('p')).split("<b>")[1]).split("</b>")[0]
		hindi_meaning = (str(soup.findAll('i')).split(",")[4]).split('<i>')[1].split('</i>')[0]
		hindi = (str(soup.findAll("p")).split(";")[3]).split(">")[1].split("</")[0]

		url = "https://bhagavadgita.io/chapter/{}/verse/{}/".format(str(chapter_number), str(veser_number))
		soup = BeautifulSoup(requests.get(url).content, 'html.parser')
		english = str(soup.findAll('p')).split(">")[13].split("</")[0]

		dict = {
            'sloak' : sanskrit,
            'hindi'	: hindi,
            'english' : english,
            'wrd_mean' : hindi_meaning
        }
		return dict
