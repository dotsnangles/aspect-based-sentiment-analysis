#!/bin/bash

# papermill ./target_tagger_trainer.ipynb ./papermill/target_tagger_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_target_tagger.out

# papermill ./taget_tagger_tabsa_trainer.ipynb ./papermill/taget_tagger_tabsa_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_tabsa.out




# papermill ./train_acd.ipynb ./papermill/train_acd.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v21_maxlen_false_acd.out

# papermill ./train_asc.ipynb ./papermill/train_asc.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v21_maxlen_false_asc.out

nohup papermill ./train_acd.ipynb ./papermill/train_uncleaned_v21_run_4_acd.ipynb > ./papermill/uncleaned_v21_run_4_acd.out
nohup papermill ./train_asc.ipynb ./papermill/train_uncleaned_v21_run_4_asc.ipynb > ./papermill/uncleaned_v21_run_4_asc.out