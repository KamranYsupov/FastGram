from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_mixins import AbstractUser, TimestampedMixin


class User(AbstractUser, TimestampedMixin):
    """Модель пользователя"""
    pass

