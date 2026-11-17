from pathlib import Path

import pytest


@pytest.fixture
def csv_file() -> Path:
    """Фикстура для доступа к csv файлу для проверки"""
    return Path('.') / 'pgadmin.csv'
