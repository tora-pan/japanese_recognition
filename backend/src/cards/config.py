from fastapi import Depends

from ..utils.auth import get_current_user


class Config:
    prefix = "/cards"
    tags = ["cards"]
    dependencies = [Depends(get_current_user)]