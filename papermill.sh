#!/bin/bash

papermill ./acd_binary_trainer.ipynb ./papermill_nbs/acd_binary_trainer.ipynb
papermill ./asc_binary_trainer.ipynb ./papermill_nbs/asc_binary_trainer.ipynb

# nohup bash papermill.sh > ./papermill_nbs/uncleaned_v1.out