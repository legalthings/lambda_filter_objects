LegalThings - AWS Lambda Object Filter
==================

## Requirements

- [Python](https://python.org) >= 3.6.0


## Installation

The dependencies can be installed using python.

python setup.py install


## Testing

Lambda function can be locally simulated for testing.

python setup.py test


## Usage

  This lambda filters a list of objects based on a string value.
A list of one or multiple keywords are checked against this value. (not case sensitive by default, but available by setting a parameter)
  If the value is more than one layer deep, the key has to be passed as 'layer1Name.layer2Name.key'.


### Example list of objects
  ```json
[
  {
    "message": "This is message number one",
    "likes": 20,
    "timestamp": {
      "date": "12 september 2018",
        "time": "21:23"
    }
  },
  {
    "message": "This is another message",
    "likes": 12,
    "timestamp": {
      "date": "12 november 2018",
      "time": "22:23"
    }
  },
  {
    "message": "This Message includes a capital letter",
    "likes": 3,
    "timestamp": {
      "date": "18 september 2018",
      "time": "11:25"
    }
  },
  {
    "message": "Guess which word is not used here",
    "likes": 21,
    "timestamp": {
      "date": "1 augustus 2018",
      "time": "23:01"
    }
  }
]
```

Make a `[POST]` request to the Lambda with the following data.

```json
{ 
  "objs": [{"for": "example"}, {"the": "above"}, {"list": "of"}, {"filterable": "objects"}],
  "key": "KeyToBeFilteredAt",
  "keywords": ["List", "of", "words", "you", "want", "to", "look", "for"]
}
```

The result is an array of objects that contained at least one of the keywords in the value of the specified key.

```json
[
  {
    "message": "This is message number one",
    "likes": 20,
    "timestamp": {
      "date": "12 september 2018",
        "time": "21:23"
    }
  },
  {
    "message": "This is another message",
    "likes": 12,
    "timestamp": {
      "date": "12 november 2018",
      "time": "22:23"
    }
  }
]
```

