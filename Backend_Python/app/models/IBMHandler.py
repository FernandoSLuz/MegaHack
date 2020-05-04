import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    '5hA8Z42uxna9uxBoYSrDOKZTGGcn5BrLHBPmbvUCk_ct')
assistant = AssistantV1(
    version='2020-04-01',
    authenticator=authenticator
)
workspace_id = 'ac2daa7b-0ce4-4a2c-b969-87304b30ac2d'
assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')


def MakeQuestion(form):
    print("test")
    response = assistant.message(
        workspace_id=workspace_id,
        input={
            'text': '_P3_ validade'
        }
    ).get_result()
    return response


def CreateDialog(form):
    response = assistant.create_dialog_node(
        workspace_id=workspace_id,
        dialog_node='P3_Q1',
        conditions='@Products:_P1_ and #P3_Q1',
        output=[{'response_type': 'text', 'values': [{'text': 'Tem.'}]}],
        title='P3_Q1'
    ).get_result()
    return response


def CreateIntent(form):
    response = assistant.create_intent(
        workspace_id=workspace_id,
        intent='P6_Q1',
        examples=[
            {'text': 'Qual o tamanho ?'}
        ]
    ).get_result()
    print(json.dumps(response, indent=2))
    return {'status': 'sucess'}


def EditEntity(form):
    response = assistant.update_entity(
        workspace_id=workspace_id,
        entity='Products',
        new_values=[{
            'value': '_P6_'
        }],
        append=True
    ).get_result()
    return response


def GetIntents(form):
    response = assistant.get_intent(
        workspace_id=workspace_id,
        intent='P1_Q3'
    ).get_result()
    return response
