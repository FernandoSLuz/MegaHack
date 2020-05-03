from flask import Blueprint, request, render_template, abort
from . import main_tools
from .. import models
import json

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def index():
   return {"Hackathon":"MegaHack"}

@main.route('/Olist/question', methods=['POST'])
def GetOlistQuestion():
    form = request.get_json(silent=True, force=True)
    status_code = 0
    callbackDict = {}
    if(main_tools.check_json(form, ['ad_id', 'product_id', 'question']) == False):
        status_code = 406
        callbackDict = {'feedback': 'missing POST body data'}
    else:
        callbackDict = models.DialogflowHandler.SendDialogflowQuestion(form)
        status_code = 200
    return json.dumps(callbackDict, indent=2, default=str, ensure_ascii=False), status_code

@main.route('/Olist/answer', methods=['POST'])
def GetOlistAnswer():
    form = request.get_json(silent=True, force=True)
    status_code = 0
    callbackDict = {}
    if(main_tools.check_json(form, ['question_id', 'answer']) == False):
        status_code = 406
        callbackDict = {'feedback': 'missing POST body data'}
    else:
        callbackDict = models.DialogflowHandler.SendDialogflowAnswer(form)
        status_code = 200
    return json.dumps(callbackDict, indent=2, default=str, ensure_ascii=False), status_code