import json

def filterObjects(objs, key, keywords, caseSensitive=False):
  result = []
  parsedObjs = json.loads(objs, strict=False)
  parsedKeywords = json.loads(keywords, strict=False)
  keys = key.split('.')
  for obj in parsedObjs:
    value = obj
    failed = False
    for k in keys:
      try:
        value = value[k]
      except (KeyError, TypeError) as e:
        failed = True
        break

    if failed or type(value) is not str:
      continue
    
    for word in parsedKeywords:
      if (not caseSensitive and word.lower() in value.lower()) \
          or (caseSensitive and word in value):
        result.append(obj)
        break

  return result
