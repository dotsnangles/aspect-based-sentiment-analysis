import os
import torch

ce_labels = ['True', 'False']
pc_labels = ['positive', 'negative', 'neutral']
pc_binary_labels = ['True', 'False']

NGPU = torch.cuda.device_count()

report_to="wandb"

fp16 = False

num_train_epochs = 10
per_device_train_batch_size = 1
gradient_accumulation_steps = 1

per_device_eval_batch_size = 32

optim = 'adamw_torch' # 'adamw_torch' or 'adamw_hf'

learning_rate = 3e-6 / 8 * batch_size * NGPU # 5e-5
weight_decay = 0.01 # 0
adam_epsilon = 1e-8

lr_scheduler_type = 'linear'
warmup_ratio = 0

save_total_limit = 2

load_best_model_at_end = True
metric_for_best_model ='f1_macro'

save_strategy = "epoch"
evaluation_strategy = "epoch"

logging_strategy = "steps"
logging_first_step = True 
logging_steps = 100

def print_args():
    print(f'batch_size: {batch_size*NGPU}')
    print(f'learning_rate: {learning_rate}')
    print(f'num_train_epochs: {num_train_epochs}')    
    # print()
    # print(f'NGPU: {NGPU}')
    # print(f'report_to: {report_to}')
    # print(f'fp16: {fp16}')
    # print(f'num_train_epochs: {num_train_epochs}')
    # print(f'batch_size: {batch_size}')
    # print(f'gradient_accumulation_steps: {gradient_accumulation_steps}')
    # print(f'optim: {optim}')
    # print(f'learning_rate: {learning_rate}')
    # print(f'weight_decay: {weight_decay}')
    # print(f'adam_epsilon: {adam_epsilon}')
    # print(f'lr_scheduler_type: {lr_scheduler_type}')
    # print(f'warmup_ratio: {warmup_ratio}')
    # print(f'save_total_limit: {save_total_limit}')
    # print(f'load_best_model_at_end: {load_best_model_at_end}')
    # print(f'metric_for_best_model: {metric_for_best_model}')
    # print(f'save_strategy: {save_strategy}')
    # print(f'evaluation_strategy: {evaluation_strategy}')
    # print(f'logging_strategy: {logging_strategy}')
    # print(f'logging_first_step: {logging_first_step}')
    # print(f'logging_steps: {logging_steps}')
    
    
def print_paths(PROJECT_NAME, model_checkpoint, DATA_V, SAVE_PATH, NOTEBOOK_PATH, TRAIN_DATA_PATH, EVAL_DATA_PATH):
    print(f'PROJECT_NAME: {PROJECT_NAME}')
    print()
    print(f'model_checkpoint: {model_checkpoint}')
    print(f'DATA_V: {DATA_V}')
    print()
    if os.path.exists(SAVE_PATH):
        print(f'SAVE_PATH: {SAVE_PATH} exists.')
    else:
        print(f'SAVE_PATH: {SAVE_PATH} does not exist.')
    if os.path.exists(NOTEBOOK_PATH):
        print(f'NOTEBOOK_PATH: {NOTEBOOK_PATH} exists.')
    else:
        print(f'NOTEBOOK_PATH: {NOTEBOOK_PATH} does not exist.')
    print()
    if os.path.exists(TRAIN_DATA_PATH):
        print(f'TRAIN_DATA_PATH: {TRAIN_DATA_PATH} exists.')
    else:
        print(f'TRAIN_DATA_PATH: {TRAIN_DATA_PATH} does not exist.')
    if os.path.exists(EVAL_DATA_PATH):
        print(f'EVAL_DATA_PATH: {EVAL_DATA_PATH} exists.')
    else:
        print(f'EVAL_DATA_PATH: {EVAL_DATA_PATH} does not exist.')
        
def print_torch_info():
    print(f'torch.__version__: {torch.__version__}')
    print(f'torch.cuda.is_available(): {torch.cuda.is_available()}')
    print(f'NGPU: {NGPU}')