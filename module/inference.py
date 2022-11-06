import torch
from tqdm import tqdm

entity_property_pair = [
    '본품#가격', '본품#다양성', '본품#디자인', '본품#인지도', '본품#일반', '본품#편의성', '본품#품질',
    '브랜드#가격', '브랜드#디자인', '브랜드#인지도', '브랜드#일반', '브랜드#품질',
    '제품 전체#가격', '제품 전체#다양성', '제품 전체#디자인', '제품 전체#인지도', '제품 전체#일반', '제품 전체#편의성', '제품 전체#품질',
    '패키지/구성품#가격', '패키지/구성품#다양성', '패키지/구성품#디자인', '패키지/구성품#일반', '패키지/구성품#편의성', '패키지/구성품#품질'
]

tf_id_to_name = ['True', 'False']
tf_name_to_id = {tf_id_to_name[i]: i for i in range(len(tf_id_to_name))}

polarity_id_to_name = ['positive', 'negative', 'neutral']
polarity_name_to_id = {polarity_id_to_name[i]: i for i in range(len(polarity_id_to_name))}

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


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