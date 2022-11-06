import torch
from tqdm import tqdm
from module.maps import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

entity_property_pairs = [
    entity_property_pair,
    ['본품#품질', '제품 전체#일반', '본품#일반', '제품 전체#품질'],
    ['본품#품질', '제품 전체#일반', '본품#일반', '제품 전체#품질', '제품 전체#디자인'],
    ['본품#품질', '제품 전체#일반', '본품#일반', '제품 전체#품질', '제품 전체#디자인', '본품#편의성', '제품 전체#편의성']
]

def inference_m(acd_tokenizer, asc_tokenizer, acd_model, asc_model, data, entity_property_pair):
    print(entity_property_pair)
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
            acd_encoded = acd_tokenizer(form, acd_pair, truncation=True, return_tensors="pt", padding='max_length', max_length=256)
            acd_encoded = {k:v.to(device) for k,v in acd_encoded.items()}

            with torch.no_grad():
                acd_outputs = acd_model(**acd_encoded)
            acd_predictions = acd_outputs['logits'].argmax(-1)
            acd_result = tf_id_to_name[acd_predictions[0]]

            if acd_result == 'True':
                asc_pair = pair
                asc_encoded = asc_tokenizer(form, asc_pair, truncation=True, return_tensors="pt", padding='max_length', max_length=256)
                asc_encoded = {k:v.to(device) for k,v in asc_encoded.items()}

                with torch.no_grad():
                    asc_outputs = asc_model(**asc_encoded)
                asc_predictions = asc_outputs['logits'].argmax(-1)
                asc_result = polarity_id_to_name[asc_predictions[0]]

                if pair == '패키지/구성품#가격':
                    print(f'{pair} found.')
                    pair = '패키지/ 구성품#가격'
                    print(f'corrected as {pair}')

                sentence['annotation'].append([pair, asc_result])

    return data

def inference_b(acd_tokenizer, asc_tokenizer, acd_model, asc_model, data, entity_property_pair):
    print(entity_property_pair)
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
            acd_encoded = acd_tokenizer(form, acd_pair, truncation=True, return_tensors="pt", padding='max_length', max_length=256)
            acd_encoded = {k:v.to(device) for k,v in acd_encoded.items()}

            with torch.no_grad():
                acd_outputs = acd_model(**acd_encoded)
            acd_predictions = acd_outputs['logits'].argmax(-1)
            acd_result = tf_id_to_name[acd_predictions[0]]

            if acd_result == 'True':
                sentiments = ['positive', 'negative', 'neutral']
                asc_pairs = []
                for sentiment in sentiments:
                    asc_pair = '#'.join([pair, sentiment])
                    asc_pairs.append(asc_pair)

                positive = asc_tokenizer(form, asc_pairs[0], truncation=True, return_tensors="pt", padding='max_length', max_length=256)
                positive = {k:v.to(device) for k,v in positive.items()}
                negative = asc_tokenizer(form, asc_pairs[1], truncation=True, return_tensors="pt", padding='max_length', max_length=256)
                negative = {k:v.to(device) for k,v in negative.items()}
                neutral = asc_tokenizer(form, asc_pairs[2], truncation=True, return_tensors="pt", padding='max_length', max_length=256)
                neutral = {k:v.to(device) for k,v in neutral.items()}

                with torch.no_grad():
                    positive_outputs = asc_model(**positive)
                    negative_outputs = asc_model(**negative)
                    neutral_outputs = asc_model(**neutral)

                asc_predictions = torch.tensor([positive_outputs['logits'][0][0], negative_outputs['logits'][0][0], neutral_outputs['logits'][0][0]]).argmax(-1)
                asc_result = polarity_id_to_name[asc_predictions]

                if pair == '패키지/구성품#가격':
                    print(f'{pair} found.')
                    pair = '패키지/ 구성품#가격'
                    print(f'corrected as {pair}')

                sentence['annotation'].append([pair, asc_result])

    return data