import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc
from nlpaug.util import Action
from transformers import AutoTokenizer

from googletrans import Translator
import translators as ts

model_checkpoint = 'klue_roberta_base_mlm_fine_tuned'
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
sTokens = tokenizer.all_special_tokens

def del_tokens(sent):
    sent = sent.split(' ')
    temp = []
    for e in sent:
        if e not in sTokens:
            temp.append(e)
    return ' '.join(temp)

def back_trans(text):
    aug1 = ts.papago(text, sleep_seconds=5, from_language='ko', to_language='en')
    aug1 = ts.papago(aug1, sleep_seconds=5, from_language='en', to_language='ko')

    aug2 = ts.papago(text, sleep_seconds=5, from_language='ko', to_language='ja')
    aug2 = ts.papago(aug2, sleep_seconds=5, from_language='ja', to_language='ko')

    return [aug1, aug2]

def random_insert(num, sample, device='cuda'):
    aug = naw.ContextualWordEmbsAug(
        model_path=model_checkpoint, action="insert", model_type='bert', top_k=25, aug_p=0.3, aug_min=1, aug_max=1, device=device)

    aug_result = aug.augment(sample, n=num, num_thread=12)
    aug_result = list(map(del_tokens, aug_result))
    aug_result = list(set(aug_result))
    return aug_result

def random_replace(num, sample, device='cuda'):
    aug = naw.ContextualWordEmbsAug(
        model_path=model_checkpoint, action="insert", model_type='bert', top_k=25, aug_p=0.3, aug_min=1, aug_max=1, device=device)

    aug_result = aug.augment(sample, n=num, num_thread=12)
    aug_result = list(map(del_tokens, aug_result))
    aug_result = list(set(aug_result))
    return aug_result

def random_swap(num, sample):
    aug = naw.RandomWordAug(action='swap', aug_min=1, aug_max=1, aug_p=0.3)    
    aug_result = aug.augment(sample, n=num, num_thread=2)
    aug_result = list(set(aug_result))
    return aug_result

def random_split(num, sample):
    aug = naw.SplitAug(aug_min=1, aug_max=1, aug_p=0.3, min_char=3)
    aug_result = aug.augment(sample, n=num, num_thread=2)
    aug_result = list(set(aug_result))
    return aug_result