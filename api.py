import flask
from flask import request, jsonify
import json
from Functions.functions import *

df_inv = read_inv('./Data/tvaberta_inventory_availability.csv(1).csv')
df_pro = read_pro('./Data/tvaberta_program_audience.csv')

df_res = df_pro.copy()
df_res = df_predicted_audience(df_res)
df_res = pd.concat([df_res,df_inv])

def get_predicted(_program_code,_date):
    return json.loads(df_res.loc[(df_res['date'] == _date) & (df_res['program_code'] == _program_code)][['available_time','predicted_audience']].to_json(orient="records"))

def get_period(begin,end):
    return json.loads(df_res.loc[(df_res['date'] >= begin) & (df_res['date'] <= end)][['program_code','available_time','predicted_audience']].to_json(orient="records"))

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/get_predicted', methods=['GET'])
def route_predicted():
    query_parameters = request.args
    _program_code = str(query_parameters.get('program_code'))
    _date = str(query_parameters.get('date'))
    return jsonify(get_predicted(_program_code,_date))

@app.route('/get_period', methods=['GET'])
def route_period():
    query_parameters = request.args
    begin = str(query_parameters.get('begin'))
    end = str(query_parameters.get('end'))
    return jsonify(get_period(begin,end))
app.run()