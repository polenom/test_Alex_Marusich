import asyncio

import pytest
from tests.test_elements import valid_url, urls, not_valid_url
from test_freelance.app import check_url, get_methods


def test_urls():
    valid, not_valid = check_url(urls)
    assert list(valid.keys()) == valid_url
    assert not_valid == not_valid_url


@pytest.mark.parametrize("url, result, itog", [("https://google.com", {}, {"GET": 200}),
                                               ("https://github.com/", {}, {
                                                   'DELETE': 404,
                                                   'GET': 200,
                                                   'OPTIONS': 404,
                                                   'PATCH': 404,
                                                   'POST': 404,
                                                   'PUT': 404}),
                                               ("https://fdljl.cocfdsm", {}, {})
                                               ])
def test_gets_methods(url, result, itog):
    asyncio.run(get_methods(url, result))
    assert result == itog
