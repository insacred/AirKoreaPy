import urllib
import urllib.parse
import urllib.request
from xml.etree import ElementTree

from entity import AirCondition


class AirKoreaAPIClient:

    def __init__(self, key):
        self.key = key

    def get_air_condition_by_location(
            self, area: str, page: int=1, limit: int=10,
            term: str='DAILY', version: str='1.3'):
        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?' \
              'ServiceKey={key}&numOfRows={limit}&pageNo={page}&stationName={area}&dataTerm={term}&ver={version}' \
              .format(area=urllib.parse.quote(area), key=self.key, page=page, limit=limit, term=term, version=version)
        response = urllib.request.urlopen(url)
        tree = ElementTree.fromstring(response.read())
        items = tree.findall('.//item')
        for item in items:
            yield AirCondition(item)
