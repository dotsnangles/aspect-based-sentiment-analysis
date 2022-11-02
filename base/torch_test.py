import torch

print(f'torch.__version__: {torch.__version__}')
print(f'torch.cuda.is_available(): {torch.cuda.is_available()}')
NGPU = torch.cuda.device_count()
print(f'NGPU: {NGPU}')