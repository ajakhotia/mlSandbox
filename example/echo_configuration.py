from typing import Any
import numpy as np
import pandas as pd
import torch


def device_details(device: torch.device) -> dict[str, Any]:
    return {
        "device": torch.cuda.get_device_name(device),
        "memory": torch.cuda.mem_get_info(),
    }


def main():
    print(
        'Environment Details:\n'
        f'\tpytorch: v{torch.__version__}\n'
        f'\tnumpy: v{np.__version__}\n'
        f'\tpandas: v{pd.__version__}\n'
    )

    print(
        'Cuda Device Information:\n'
        f'\tcuda_available: {torch.cuda.is_available()}\n'
        f'\tcuda_device_count: {torch.cuda.device_count()}\n'
    )

    device_details_list = [device_details(torch.cuda.device(n)) for n in range(torch.cuda.device_count())]
    print(*device_details_list, sep='\n')


if __name__ == "__main__":
    main()
