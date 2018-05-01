def filterObjects(objs, key, keywords, caseSensitive=False):
  result = []
  keys = key.split('.')
  for obj in objs:
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
    
    for word in keywords:
      if (not caseSensitive and word.lower() in value.lower()) \
          or (caseSensitive and word in value):
        result.append(obj)
        break

  return result
