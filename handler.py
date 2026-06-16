import os
from typing import Any, Dict

import runpod
import torch


def handler(job: Dict[str, Any]) -> Dict[str, Any]:
    """Validate the Runpod worker before loading the LongCat model."""

    job_input = job.get("input") or {}
    prompt = str(job_input.get("prompt", "")).strip()

    if not prompt:
        return {
            "status": "error",
            "error": "input.prompt is required",
        }

    cuda_available = torch.cuda.is_available()

    return {
        "status": "worker_ready",
        "message": "Runpod worker is ready. LongCat inference is not enabled yet.",
        "prompt": prompt,
        "cuda_available": cuda_available,
        "gpu_name": (
            torch.cuda.get_device_name(0)
            if cuda_available
            else None
        ),
        "model_path": os.getenv(
            "MODEL_PATH",
            "/runpod-volume/LongCat-Video",
        ),
    }


runpod.serverless.start({"handler": handler})