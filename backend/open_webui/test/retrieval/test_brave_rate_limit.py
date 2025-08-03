import requests
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from open_webui.retrieval.web.brave import search_brave
from open_webui.test.util.abstract_integration_test import AbstractIntegrationTest
from open_webui.test.util.mock_user import mock_user
from fastapi.testclient import TestClient
from open_webui.main import app


def test_search_brave_rate_limit():
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError(
        response=Mock(status_code=429)
    )

    with patch("open_webui.retrieval.web.brave.requests.get", return_value=mock_response):
        with pytest.raises(HTTPException) as exc_info:
            search_brave("key", "query", 5)

    assert exc_info.value.status_code == 429
    assert "rate limit" in exc_info.value.detail.lower()


class TestProcessWebSearchRateLimit(AbstractIntegrationTest):
    BASE_PATH = "/api/v1/retrieval"

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.fast_api_client = TestClient(app)
        config = cls.fast_api_client.app.state.config
        config.WEB_SEARCH_ENGINE = "brave"
        config.BRAVE_SEARCH_API_KEY = "test-key"

    def test_process_web_search_brave_429(self):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError(
            response=Mock(status_code=429)
        )

        with mock_user(self.fast_api_client.app, id="1"):
            with patch(
                "open_webui.retrieval.web.brave.requests.get", return_value=mock_response
            ):
                resp = self.fast_api_client.post(
                    self.create_url("/process/web/search"),
                    json={"queries": ["test"]},
                )
        assert resp.status_code == 429
        assert resp.json()["detail"] == "Brave API rate limit exceeded"
