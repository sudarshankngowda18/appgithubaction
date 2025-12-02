import pytest
from src.ui import calculate_ui

def test_gradio_addition(monkeypatch):
    class MockResponse:
        def json(self):
            return {"result": 7}
    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)
    result = calculate_ui(3, 4, "add")
    assert result == 7

def test_gradio_subtraction(monkeypatch):
    class MockResponse:
        def json(self):
            return {"result": 2}
    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)
    result = calculate_ui(5, 3, "sub")
    assert result == 2