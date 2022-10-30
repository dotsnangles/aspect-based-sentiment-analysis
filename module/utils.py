from typing import Counter


from collections import Counter

def count_tags(df, entity_property_pair):
    count = 0
    tags = []
    for idx, row in df.iterrows():
        if len(row.annotation) > 0:
            for annotation in row.annotation:
                try:
                    tags.append(annotation[0])
                    count += 1
                except Exception as e:
                    print(e)
                    print(row.id)

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
            if target not in targets:
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

def generate_token_classification_data(df):
    split_inputs, split_labels = [], []
    for original_input, annotations in zip(df.sentence_form, df.annotation):
        split_input, split_label = make_token_classification_pair(original_input, annotations)
        split_inputs.append(split_input)
        split_labels.append(split_label)
    return split_inputs, split_labels

def align_tokens_and_labels(df, tokenizer):
    input_tokens_list, labels = [], []
    for _, row in df.iterrows():
        split_form, label = row.split_form,	row.split_label
        for idx in range(len(split_form)):
            tokens = tokenizer.tokenize(split_form[idx])
            if label[idx] == 0:
                label[idx] = [label[idx] for _ in range(len(tokens))]
            else:
                label[idx] = [label[idx] if i == 0 else 2  for i in range(len(tokens))]
                pass
            split_form[idx] = tokens

        input_tokens = ['[CLS]'] + [x for el in split_form for x in el] + ['[SEP]']
        label = [-100] + [x for el in label for x in el] + [-100]
        input_tokens_list.append(input_tokens)
        labels.append(label)
    return input_tokens_list, labels

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