import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('5hA8Z42uxna9uxBoYSrDOKZTGGcn5BrLHBPmbvUCk_ct')
assistant = AssistantV1(
    version='2020-04-01',
    authenticator = authenticator
)
workspace_id = 'ac2daa7b-0ce4-4a2c-b969-87304b30ac2d'
assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')

def MakeQuestion(form):
    print("test")
    response = assistant.message(
        workspace_id= workspace_id,
        input={
            'text': '_P1_ voltagem'
        }
    ).get_result()
    return response

def CreateDialog(form):
    return {'status': 'sucess'}

def CreateIntent(form):
    return {'status': 'sucess'}

def EditEntity(form):
    return {'status': 'sucess'}

def GetIntents(form):
    return {'status': 'sucess'}