import asyncio
import json

import aiohttp
import validators
from aiohttp import ClientConnectorError, ClientSession, ServerTimeoutError

data = []


def io_operation_input() -> list[str]:
    result_input = []
    print("if you want to finish enter an empty line:")
    line_num = 1
    while True:
        input_url = input(f'{line_num}) ').strip()
        if not input_url:
            break
        result_input.append(input_url)
        line_num += 1
    return result_input


async def get_methods(url: str, result: dict) -> None:
    methods = ['get', 'post', 'options', 'put', 'patch', 'delete']
    try:
        async with aiohttp.ClientSession() as session:
            for method in methods:
                async with getattr(session, method)(url, timeout=10) as resp:
                    if resp.status != 405:
                        result[method.upper()] = resp.status
    except (ClientConnectorError, asyncio.TimeoutError):
        pass


def check_url(urls: list[str]) -> dict:
    url_true = {}
    url_false = []
    for key, url in enumerate(urls):
        if (url.startswith('http') or url.startswith('https')) and validators.url(url):
            url_true[url] = {}
        else:
            url_false.append([key, url])
    return (url_true, url_false)


async def main():
    input_date = io_operation_input()
    print("START")
    valid_urls, not_valid_urls = check_url(input_date)
    tasks = []
    for i in valid_urls.keys():
        tasks.append(get_methods(i, valid_urls[i]))
    await asyncio.gather(*tasks)
    print("NOT VALID URL\r\n")
    print('\r\n'.join(map(lambda a: f'    {a[0]}) {a[1]}', not_valid_urls)))
    print("\r\nVALID URL\r\n")
    print(json.dumps(valid_urls, indent=4))


if __name__ == '__main__':
    asyncio.run(main())
