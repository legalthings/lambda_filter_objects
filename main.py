from filterobjects import filterObjects

def lambda_handler(event, context):
    c = event['case_sensitive'] if 'case_sensitive' in event else False
    return filterObjects(event['objs'], event['key'], event['keywords'], c)
