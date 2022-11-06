#!/bin/bash

# papermill ./target_tagger_trainer.ipynb ./papermill/target_tagger_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_target_tagger.out

# papermill ./taget_tagger_tabsa_trainer.ipynb ./papermill/taget_tagger_tabsa_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_tabsa.out




# papermill ./train_acd_b_new.ipynb ./papermill/train_acd_b_new.ipynb
papermill ./train_asc.ipynb ./papermill/train_asc.ipynb

# nohup bash papermill.sh > ./papermill/uncleaned_v18_maxlen_256_asc_b.out