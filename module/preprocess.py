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