import bottle
import data
import json

import os.path
def load_data( ):
   csv_file = 'cache.csv'
   if not os.path.isfile(csv_file):
     url = 'https://data.cityofnewyork.us/resource/uip8-fykc.json?$limit=50000&$select=arrest_date,pd_desc,ofns_desc,arrest_boro,arrest_precinct,law_cat_cd,age_group,perp_sex,perp_race'
     info = data.retrieve_json(url)
     needed_keys = ['arrest_date','age_group','arrest_boro','pd_desc','law_cat_cd']
     for k in needed_keys:
       info = data.clean_list(k, info)
     data.cache_writer(info, csv_file)

load_data()


@bottle.route("/")
def servehtml():
  return bottle.static_file("index.html",root=".")

@bottle.route('/ajax')
def ajax():
  return bottle.static_file("ajax.js",root=".")

@bottle.route('/myjscode.js')
def jscode():
  return bottle.static_file('myjscode.js', root='.')

@bottle.get('/linechart')
def linechart():
  ret = data.forlinechart()
  return json.dumps(ret)
  
@bottle.get('/piechart')
def piechart():
  ret = data.forpiechart()
  return json.dumps(ret)

@bottle.post('/barchart')
def barchart():
  return None








bottle.run(host="0.0.0.0", port=8080)




