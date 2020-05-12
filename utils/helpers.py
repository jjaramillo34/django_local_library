import arrow

def humanreadable_dates(datetohumanize):
	#utc = arrow.now()
	#localTime = utc.to('US/Eastern')
	#datetohumanize = localTime
	#ftime = arrow.format(value, format_spec)
	atime = arrow.get(datetohumanize, 'MM/DD/YYYY | HH:mm:ss A')
	return atime.humanize()

def capitalize_titles(stringtocapitalize): 
	reslt = " ".join([word.title() if word not in "the a on in of an for" else word for word in stringtocapitalize.split(" ")])
	return reslt

def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


#print(humanreadable_dates("May 4, 2020"))