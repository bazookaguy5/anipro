from lxml import html
import requests


class Connection:

	def __init__(self, link):
		while True:
			self.__cnc = self.__get_connection(link)
			if self.__cnc != 'Failure': break

	def __get_connection(self, website):
		try:
			return requests.get(website)
		except:
			return "Failure"

	def get_from_tag(self, tags_xpath):
		tree = html.fromstring(self.__cnc.content)
		element = tree.xpath(tags_xpath)

		return element

	def get_content(self):
		return self.__cnc.content;