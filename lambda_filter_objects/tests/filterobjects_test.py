from unittest import TestCase
from lambda_filter_objects import filterObjects

class TestFilter(TestCase):
    def setUp(self):
        self.mockObjects = '[\
            {\
              "message": "This is message number 1",\
              "likes": 20,\
              "timestamp": {\
                "date": "12 september 2018",\
                "time": "21:23"\
              }\
            },\
            {\
              "message": "This is another message",\
              "likes": 12,\
              "timestamp": {\
                "date": "12 november 2018",\
                "time": "22:23"\
              }\
            },\
            {\
              "message": "This Message includes a capital letter",\
              "likes": 3,\
              "timestamp": {\
                "date": "18 september 2018",\
                "time": "11:25"\
              }\
            },\
            {\
              "message": "Guess which word is not used here",\
              "likes": 21,\
              "timestamp": {\
                "date": "1 augustus 2018",\
                "time": "23:01"\
              }\
            }]'
            
    def testResult(self):
        res = filterObjects(self.mockObjects, 'message', '["message"]')
        self.assertEqual(len(res), 3)

    def testKeyError(self):
        res = filterObjects(self.mockObjects, 'message.first', '["message"]')
        self.assertEqual(len(res), 0)

    def testKeyDepth(self):
        res = filterObjects(self.mockObjects, 'timestamp.date', '["september"]')
        self.assertEqual(len(res), 2)

    def testMultipleKeywords(self):
        res = filterObjects(self.mockObjects, 'message', '["number", "word"]')
        self.assertEqual(len(res), 2)

    def testCaseSensitivity(self):
        res = filterObjects(self.mockObjects, 'message', '["message"]', caseSensitive=True)
        self.assertEqual(len(res), 2)

    def testDifferentValueType(self):
        res = filterObjects(self.mockObjects, 'likes', '["message"]')
        self.assertEqual(len(res), 0)
        

