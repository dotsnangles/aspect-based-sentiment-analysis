import torch
from tqdm import tqdm
from module.maps import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def inference_m(acd_tokenizer, asc_tokenizer, acd_model, asc_model, data):
    acd_model.to(device)
    acd_model.eval()
    asc_model.to(device)
    asc_model.eval()

    for sentence in tqdm(data):
        form = sentence['sentence_form']
        sentence['annotation'] = []
        if type(form) != str:
            print("form type is wrong: ", form)
            continue
        for pair in entity_property_pair:
            acd_pair = pair
            acd_encoded = acd_tokenizer(form, acd_pair, truncation=True, return_tensors="pt")
            acd_encoded = {k:v.to(device) for k,v in acd_encoded.items()}

            with torch.no_grad():
                acd_outputs = acd_model(**acd_encoded)
            ce_predictions = acd_outputs['logits'].argmax(-1)
            ce_result = tf_id_to_name[ce_predictions[0]]

            if ce_result == 'True':
                asc_pair = pair
                asc_encoded = asc_tokenizer(form, asc_pair, truncation=True, return_tensors="pt")
                asc_encoded = {k:v.to(device) for k,v in asc_encoded.items()}

                with torch.no_grad():
                    asc_outputs = asc_model(**asc_encoded)
                pc_predictions = asc_outputs['logits'].argmax(-1)
                pc_result = polarity_id_to_name[pc_predictions[0]]

                if pair == '패키지/구성품#가격':
                    print(f'{pair} found.')
                    pair = '패키지/ 구성품#가격'
                    print(f'corrected as {pair}')

                sentence['annotation'].append([pair, pc_result])

    return data

def inference_b(acd_tokenizer, asc_tokenizer, acd_model, asc_model, data):
    acd_model.to(device)
    acd_model.eval()
    asc_model.to(device)
    asc_model.eval()

    for sentence in tqdm(data):
        form = sentence['sentence_form']
        sentence['annotation'] = []
        if type(form) != str:
            print("form type is wrong: ", form)
            continue
        for pair in entity_property_pair:
            acd_pair = pair
            acd_encoded = acd_tokenizer(form, acd_pair, truncation=True, return_tensors="pt")
            acd_encoded = {k:v.to(device) for k,v in acd_encoded.items()}

            with torch.no_grad():
                acd_outputs = acd_model(**acd_encoded)
            ce_predictions = acd_outputs['logits'].argmax(-1)
            ce_result = tf_id_to_name[ce_predictions[0]]

            if ce_result == 'True':
                sentiments = ['positive', 'negative', 'neutral']
                asc_pairs = []
                for sentiment in sentiments:
                    asc_pair = '#'.join([pair, sentiment])
                    asc_pairs.append(asc_pair)

                positive = asc_tokenizer(form, asc_pairs[0], truncation=True, return_tensors="pt")
                positive = {k:v.to(device) for k,v in positive.items()}
                negative = asc_tokenizer(form, asc_pairs[1], truncation=True, return_tensors="pt")
                negative = {k:v.to(device) for k,v in negative.items()}
                neutral = asc_tokenizer(form, asc_pairs[2], truncation=True, return_tensors="pt")
                neutral = {k:v.to(device) for k,v in neutral.items()}

                with torch.no_grad():
                    positive_outputs = asc_model(**positive)
                    negative_outputs = asc_model(**negative)
                    neutral_outputs = asc_model(**neutral)

                pc_predictions = torch.tensor([positive_outputs['logits'][0][0], negative_outputs['logits'][0][0], neutral_outputs['logits'][0][0]]).argmax(-1)
                pc_result = polarity_id_to_name[pc_predictions]

                if pair == '패키지/구성품#가격':
                    print(f'{pair} found.')
                    pair = '패키지/ 구성품#가격'
                    print(f'corrected as {pair}')

                sentence['annotation'].append([pair, pc_result])

    return data