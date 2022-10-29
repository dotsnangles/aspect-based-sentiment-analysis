import re
from cleantext import clean

def preprocess(text):
    text = re.sub(r'&.+&', 'OO', text)
    text = re.sub(r'[^A-Za-z0-9가-힣\s]', '', text)
    
    text = clean(
        text,
        fix_unicode=False,
        to_ascii=False,
        lower=False,
        normalize_whitespace=True,
        no_line_breaks=False,
        strip_lines=True,
        keep_two_line_breaks=False,
        no_urls=False,
        no_emails=False,
        no_phone_numbers=False,
        no_numbers=True,
        no_digits=True,
        no_currency_symbols=False,
        no_punct=True,
        no_emoji=True,
        replace_with_url="<URL>",
        replace_with_email="<EMAIL>",
        replace_with_phone_number="<PHONE>",
        replace_with_number="0",
        replace_with_digit="0",
        replace_with_currency_symbol="<CUR>",
        replace_with_punct="",
        lang="en",
    )
    
    # text = re.sub(r'[ㄱ-ㅎ]', '', text)
    # text = re.sub(r'[ㅏ-ㅣ]', '', text)
    # text = re.sub(r'[`~$^+=|><]', '', text)
    # sent = demoji.replace_with_desc(string=sent, sep= " ")
    
    # text = spacing(text)
    # text = spell_checker.check(text).checked
    return text.upper().strip()

sentiment2kor = {
    'positive': '긍정',
    'negative': '부정',
    'neutral': '중립',
}

def decorate_form(form):
    return f'Target#{form}'
    # return f'상품평 문장: <<{form}>>'

def decorate_acd_pair(entity):
    return f'Target#{entity}'
    # return f'상품평 문장의 범주 유형은 <<{entity}>>이다.'

def decorate_acd_pair_split(entity):
    props = entity.split('#')
    return f'상품평 문장의 대범주 유형은 <<{props[0]}>>이고 소범주 유형은 <<{props[1]}>>이다.'

def decorate_asc_pair(entity, sentiment):
    return f'Target#{entity}#{sentiment}'
    # return f'상품평 문장의 범주 유형이 <<{entity}>>일 때 감성 유형은 <<{sentiment}>>이다.'
    # return f'상품평 문장의 범주 유형이 <<{entity}>>일 때 감성 유형은 <<{sentiment2kor[sentiment]}>>이다.'

def decorate_asc_pair_split(entity, sentiment):
    props = entity.split('#')
    return f'상품평 문장의 대범주 유형이 <<{props[0]}>>이고 소범주 유형은 <<{props[1]}>>일 때 감성 유형은 <<{sentiment}>>이다.'
    # return f'상품평 문장의 대범주 유형이 <<{props[0]}>>이고 소범주 유형은 <<{props[1]}>>일 때 감성 유형은 <<{sentiment2kor[sentiment]}>>이다.'