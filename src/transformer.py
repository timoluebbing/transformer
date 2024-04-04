import torch

def check_device():
    """
    Checks if CUDA is available and sets the device accordingly.

    Returns:
        str: The device string indicating whether CUDA is available or not.
    """
    return 'cuda:0' if torch.cuda.is_available() else 'cpu'

print(f'Device: {check_device()}')
