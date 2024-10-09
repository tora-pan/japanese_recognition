from fastapi import Depends
from ..utils.auth import get_current_user


class Config:
    prefix = "/auth"
    tags = ["auth"]
    dependencies = [Depends(get_current_user)]
