# ### new
# import pandas as pd

# entity_property_pair = [
#     '본품#가격', '본품#다양성', '본품#디자인', '본품#인지도', '본품#일반', '본품#편의성', '본품#품질',
#     '브랜드#가격', '브랜드#디자인', '브랜드#인지도', '브랜드#일반', '브랜드#품질',
#     '제품 전체#가격', '제품 전체#다양성', '제품 전체#디자인', '제품 전체#인지도', '제품 전체#일반', '제품 전체#편의성', '제품 전체#품질',
#     '패키지/구성품#가격', '패키지/구성품#다양성', '패키지/구성품#디자인', '패키지/구성품#일반', '패키지/구성품#편의성', '패키지/구성품#품질'
# ]

# more_tokens = ['&name&', '&affiliation&', '&social-security-num&', '&tel-num&', '&card-num&', '&bank-account&', '&num&', '&online-account&']

# tf_id_to_name = ['True', 'False']
# tf_name_to_id = {tf_id_to_name[i]: i for i in range(len(tf_id_to_name))}

# polarity_id_to_name = ['positive', 'negative', 'neutral']
# polarity_name_to_id = {polarity_id_to_name[i]: i for i in range(len(polarity_id_to_name))}

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