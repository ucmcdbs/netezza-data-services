import json


class Index:

    def on_get(self, _, response):
        doc = { 'app': 'netezza-data-services' }
        response.text = json.dumps(doc, ensure_ascii=False)
