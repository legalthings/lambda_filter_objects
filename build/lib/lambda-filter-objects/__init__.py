from .filterobjects import filterObjects

def lambda_handler(event, context):
    c = event.casesensitive if event.casesensitive else False
    return filterObjects(event.objs, event.key, event.keywords, c)
