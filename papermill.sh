#!/bin/bash

# papermill ./target_tagger_trainer.ipynb ./papermill/target_tagger_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_target_tagger.out

# papermill ./taget_tagger_tabsa_trainer.ipynb ./papermill/taget_tagger_tabsa_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_tabsa.out




papermill ./trainer_for_acd_binary.ipynb ./papermill/trainer_for_acd_binary.ipynb
papermill ./trainer_for_asc_multi.ipynb ./papermill/trainer_for_asc_multi.ipynb

# nohup bash papermill.sh > ./papermill/uncleaned_v13.out