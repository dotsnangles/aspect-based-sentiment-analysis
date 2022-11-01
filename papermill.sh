#!/bin/bash

# papermill ./target_tagger_trainer.ipynb ./papermill/target_tagger_trainer.ipynb

# nohup bash papermill.sh > ./papermill/uncleaned_v11_target_tagger.out



papermill ./acd_binary_trainer.ipynb ./papermill/acd_binary_trainer.ipynb
papermill ./asc_binary_trainer.ipynb ./papermill/asc_binary_trainer.ipynb

# nohup bash papermill.sh > ./papermill/uncleaned_v11.out
