#!/bin/bash

# papermill ./target_tagger_trainer.ipynb ./papermill/target_tagger_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_target_tagger.out

# papermill ./taget_tagger_tabsa_trainer.ipynb ./papermill/taget_tagger_tabsa_trainer.ipynb
# nohup bash papermill.sh > ./papermill/uncleaned_v11_tabsa.out




# papermill ./trainer_for_acd_b_new.ipynb ./papermill/trainer_for_acd_b_new.ipynb
papermill ./trainer_for_asc_m_new.ipynb ./papermill/trainer_for_asc_m_new.ipynb

# nohup bash papermill.sh > ./papermill/uncleaned_v13_40_epochs_asc.out