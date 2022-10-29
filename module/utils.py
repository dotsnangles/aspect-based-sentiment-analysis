from typing import Counter


from collections import Counter

def count_tags(df, entity_property_pair):
    count = 0
    tags = []
    for idx, row in df.iterrows():
        if len(row.annotation) > 0:
            for annotation in row.annotation:
                tags.append(annotation[0])
                count += 1

    print('tags found: ', count)
    print('tag set of df: ', len(set(tags)))
    print('tag set of offered: ', len(set(entity_property_pair)))
    print('difference: ', set(entity_property_pair)-set(tags))

    tag_counter = Counter(tags)
    tag_counter = sorted(tag_counter.items(), key=lambda x: x[1], reverse=True)
    
    for k, v in tag_counter:
        # print(k.ljust(20), v)
        print(f'{k}\t{v}')
        
def make_token_classification_pair(original_input, annotations):
    targets = []
    for annotation in annotations:
        if annotation[1][0] != None:
            target = annotation[1][1:]
            targets.append(target)
    targets.sort()
    input_len = len(original_input)

    split_input = []
    split_label = []
    pointer = 0
    for target in targets:
        start = target[0]
        end = target[1]
        if start != 0:
            split_input.append(original_input[pointer:start])
            split_label.append(0)
        split_input.append(original_input[start:end])
        split_label.append(1)
        pointer = end
    if end != len(original_input):
        split_input.append(original_input[end:])
        split_label.append(0)

    return split_input, split_label

def remove_props(df, filter):
    for idx, row in df.iterrows():
        for idx in range(len(row.annotation)):
            if row.annotation[idx][0] not in filter:
                row.annotation[idx] = []
        row.annotation = [el for el in row.annotation if el != []]
    df['checker'] = df.annotation.apply(lambda x: bool(x))
    df = df[df.checker == True].copy()
    df['checker'] = df.annotation.apply(lambda x: False if x == [[]] else True)
    df = df[df.checker == True].copy()
    return df

# def remove_props(df, filter):
#     for idx, row in df.iterrows():
#         empty = []
#         stay = True
#         for annotation in row.annotation:
#             if annotation[0] not in filter:
#             # if annotation[0] not in filter or annotation[2] != 'positive':
#                 stay = False
#         if stay == False:
#             row.annotation = empty
#     df['check'] = df.annotation.apply(lambda x: bool(x))
#     df = df.drop(df[df.check == False].index)
#     return df

def get_filter():
    # filter = ['본품#품질',
    #           '제품 전체#일반',
    #           '본품#일반',
    #           '제품 전체#품질',
    #           '제품 전체#디자인',
    #           '본품#편의성',
    #           '제품 전체#편의성',
    #           '제품 전체#인지도',
    #           '패키지/구성품#디자인',
    #           '브랜드#일반',
    #           '제품 전체#가격']  # 2716

    # filter = ['본품#품질',
    #           '제품 전체#일반',
    #           '본품#일반',
    #           '제품 전체#품질',
    #           '제품 전체#디자인',
    #           '본품#편의성',
    #           '제품 전체#편의성',
    #           '제품 전체#인지도',
    #           '패키지/구성품#디자인',
    #           '브랜드#일반'] # 2676

    # filter = ['본품#품질',
    #           '제품 전체#일반',
    #           '본품#일반',
    #           '제품 전체#품질',
    #           '제품 전체#디자인',
    #           '본품#편의성',
    #           '제품 전체#편의성',
    #           '제품 전체#인지도',
    #           '패키지/구성품#디자인']  # 2627

    # filter = ['본품#품질',
    #           '제품 전체#일반',
    #           '본품#일반',
    #           '제품 전체#품질',
    #           '제품 전체#디자인',
    #           '본품#편의성',
    #           '제품 전체#편의성',
    #           '제품 전체#인지도']  # 2575

    # filter = ['본품#품질',
    #           '제품 전체#일반',
    #           '본품#일반',
    #           '제품 전체#품질',
    #           '제품 전체#디자인',
    #           '본품#편의성',
    #           '제품 전체#편의성'] # 2509

    # filter = ['본품#품질',
    #           '제품 전체#일반',
    #           '본품#일반',
    #           '제품 전체#품질',
    #           '제품 전체#디자인',
    #           '본품#편의성'] # 2421

    filter = ['본품#품질',
            '제품 전체#일반',
            '본품#일반',
            '제품 전체#품질',
            '제품 전체#디자인'] # 2339
    return filter