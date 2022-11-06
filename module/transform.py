import pandas as pd
from module.maps import *

def reformat_raw_to_acd_b_asc_m(df):
    acd_b =[]
    asc_m = []
    for _, row in df.iterrows():
        form = row.sentence_form
        for pair in entity_property_pair:
            isPairInOpinion = False
            aspect_pair = pair
            for annotation in row.annotation:
                entity_property = annotation[0]
                polarity = annotation[2]
                if pair == entity_property:
                    acd_b_row = [row.id, form, aspect_pair, tf_name_to_id['True']]
                    acd_b.append(acd_b_row)
                    asc_m.append([row.id, form, aspect_pair, polarity_name_to_id[polarity]])
                    isPairInOpinion = True
                    break
            if isPairInOpinion is False:
                acd_b_row = [row.id, form, aspect_pair, tf_name_to_id['False']]
                acd_b.append(acd_b_row)
    return acd_b, asc_m

def reformat_asc_m_to_asc_b(df):
    asc_b = []
    for _, row in df.iterrows():
        form = row.form
        for polarity in polarity_id_to_name:
            asc_pair = '#'.join([row.pair, polarity])
            if polarity == polarity_id_to_name[row.labels]:
                asc_b_row = [row.id, form, asc_pair, tf_name_to_id['True']]
                asc_b.append(asc_b_row)
            else:
                asc_b_row = [row.id, form, asc_pair, tf_name_to_id['False']]
                asc_b.append(asc_b_row)
    return asc_b




























# def reformat(df):
#     ep =[]
#     p = []
#     for index, row in df.iterrows():
#         utterance = row.sentence_form
#         id = row.id

#         for pair in entity_property_pair:
#             isPairInOpinion = False
#             if pd.isna(utterance):
#                 break
#             for annotation in row.annotation:
#                 entity_property = annotation[0]
#                 sentiment = annotation[2]
#                 if entity_property not in entity_property_pair:
#                     print(row.id, entity_property)
#                 if sentiment not in polarity_id_to_name:
#                     print(row.id, entity_property, sentiment)
#                     continue
#                 if entity_property == pair:
#                     ep.append([id, utterance, entity_property, tf_name_to_id['True']])
#                     p.append([id, utterance, entity_property, sentiment])
#                     isPairInOpinion = True
#                     break

#             if isPairInOpinion is False:
#                 ep.append([id, utterance, pair, tf_name_to_id['False']])

#     return ep, p

# def reformat(df):
#     ep =[]
#     p = []
#     for index, row in df.iterrows():
#         utterance = row.sentence_form
#         id = row.id

#         for pair in entity_property_pair:
#             isPairInOpinion = False
#             if pd.isna(utterance):
#                 break
#             for annotation in row.annotation:
#                 entity_property = annotation[0]
#                 sentiment = annotation[2]
#                 if entity_property not in entity_property_pair:
#                     print(row.id, entity_property)
#                     break
#                 if sentiment not in polarity_id_to_name:
#                     print(row.id, entity_property, sentiment)
#                     break
#                 if entity_property == pair:
#                     true = [id, utterance, entity_property, tf_name_to_id['True']]
#                     false = [id, utterance, entity_property, tf_name_to_id['False']]
#                     if true in ep:
#                         true_id = ep.index(true)
#                         ep.pop(true_id)
#                         print('true popped')
#                     if false in ep:
#                         false_id = ep.index(false)
#                         ep.pop(false_id)
#                         print('false popped')
#                     ep.append(true)
#                     p.append([id, utterance, entity_property, sentiment])
                    
#                     # ep.append([id, utterance, entity_property, tf_name_to_id['True']])
#                     # p.append([id, utterance, entity_property, sentiment])
#                     isPairInOpinion = True
#                     break

#             if isPairInOpinion is False:
#                 ep.append([id, utterance, pair, tf_name_to_id['False']])
                
#                 # ep.append([id, utterance, pair, tf_name_to_id['False']])

#     return ep, p

# def reformat_p_binary(df):
#     p_binary = []
#     for i, row in df.iterrows():
#         row.id, row.sentence_form, row.entity_property, row.sentiment
#         for sentiment in polarity_id_to_name:
#             if sentiment == row.sentiment:
#                 p_binary.append([row.id, row.sentence_form, '#'.join([row.entity_property, row.sentiment]), tf_name_to_id['True']])
#             else: 
#                 p_binary.append([row.id, row.sentence_form, '#'.join([row.entity_property, sentiment]), tf_name_to_id['False']])
#     return p_binary

# def reformat_from_p(data):
#     ep =[]
#     p = []
#     for index, row in data.iterrows():
#         utterance = row['sentence_form']
#         id = row['id']
#         entity_property = row['entity_property']
#         sentiment = row['sentiment']

#         for pair in entity_property_pair:
#             if not utterance:
#                 print('utterance is False')
#                 break
#             if entity_property not in entity_property_pair:
#                 print(id, entity_property)
#                 break
#             if sentiment not in polarity_id_to_name:
#                 print(id, entity_property, sentiment)
#                 break
#             if entity_property == pair:
#                 true = [id, utterance, entity_property, tf_name_to_id['True'], sentiment]
#                 false = [id, utterance, entity_property, tf_name_to_id['False'], sentiment]
#                 if true in ep:
#                     true_id = ep.index(true)
#                     ep.pop(true_id)
#                 if false in ep:
#                     false_id = ep.index(false)
#                     ep.pop(false_id)
#                 ep.append(true)
#                 p.append([id, utterance, entity_property, sentiment])
#             else:
#                 false = [id, utterance, pair, tf_name_to_id['False'], sentiment]
#                 if false in ep:
#                     false_id = ep.index(false)
#                     ep.pop(false_id)
#                 ep.append(false)

#     return ep, p