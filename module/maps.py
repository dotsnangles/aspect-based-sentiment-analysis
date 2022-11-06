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