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


def MakeComplexQuestion(form):
    product_id = str(form['product_id'])
    ad_id = str(form['ad_id'])
    code = f'P{product_id}A{ad_id}'
    question = form['question']
    response = assistant.message(
        workspace_id=workspace_id,
        nodes_visited_details = True,
        input={
            'text': f'{code} _Webhook {question}'
        }
    ).get_result()
    if(not len(response['output']['text'])):
        #return response
        response = MakeSimpleQuestion(form)
    else:
        #return response
        response = {
            'question_code': response['output']['nodes_visited_details'][0]['title'],
            'sugested_answer': response['output']['generic'][0]['text']
        } 
    return response

def MakeSimpleQuestion(form):
    product_id = str(form['product_id'])
    product_id = f'_P{product_id}_'
    question_code = ""
    question = form['question']
    response = assistant.message(
        workspace_id=workspace_id,
        nodes_visited_details = True,
        input={
            'text': f'{product_id} {question}'
        }
    ).get_result()
    if(not len(response['output']['text'])):
        question_code = GetIntentName(form['product_id'])
        CreateIntent(question_code, question)
        response = {
            'question_code': question_code,
            'sugested_answer': ''
        }
    else:
        response = {
            'question_code': response['output']['nodes_visited_details'][0]['title'],
            'sugested_answer': response['output']['generic'][0]['text']
        }
    return response


def CreateDialog(form):
    question_code = form['question_code']
    product_code = (question_code)[:question_code.find('q')-1:]
    response = assistant.create_dialog_node(
        workspace_id=workspace_id,
        dialog_node=form['question_code'],
        conditions=f'@Products:_{product_code}_ and #{question_code}',
        output={'generic':[{'response_type': 'text', 'values': [{'text': form['answer']}]}]},
        title=question_code
    ).get_result()
    return response


def CreateIntent(question_code, question):
    response = assistant.create_intent(
        workspace_id=workspace_id,
        intent=question_code,
        examples=[
            {'text': question}
        ]
    ).get_result()


def EditEntity(entity_code):
    response = assistant.update_entity(
        workspace_id=workspace_id,
        entity='Products',
        new_values=[{
            'value': entity_code
        }],
        append=True
    ).get_result()
    return response


def ListIntents():
    response = assistant.list_intents(
        workspace_id=workspace_id,
    ).get_result()
    return response

def GetIntentName(product_id):
    form = ListIntents()
    intents = []
    for intent in form['intents']:
        if(("P"+str(product_id)) in intent['intent']): 
            intents.append(int((intent['intent']).replace("P"+str(product_id)+"Q", "")))
    if(len(intents) == 0):
        question = 'Q1'
        EditEntity(f'_P{product_id}_')
    else:
        intents.sort()
        question = f'Q{intents[len(intents)-1]+1}'
    return(f'P{product_id}{question}')
