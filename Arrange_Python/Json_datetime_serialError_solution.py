def json_serial(obj):
  if isinstance(obj, (datetime, date)):
    return obj.isoformat()
    
#for pretty
dump = json.loads(jsonData, default=json_serial, indent=4)
