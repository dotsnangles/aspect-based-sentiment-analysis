#!/bin/bash

papermill ./acd_binary_trainer.ipynb ./papermill/acd_binary_trainer.ipynb
papermill ./asc_binary_trainer.ipynb ./papermill/asc_binary_trainer.ipynb

# nohup bash papermill.sh > ./papermill/uncleaned_v5.out