urls = [
    'https://www.google.com/',
    'https://github.com/',
    'http://umedia.click/',
    'http://fdj.byd/',
    'ftp://123.fds',
    'httpss://123.fbs',
    'https://123.fds\\',
    'fdsjflsd',
    'dflsjfdls.fdjls',
]

valid_url = [
    'https://www.google.com/',
    'https://github.com/',
    'http://umedia.click/',
    'http://fdj.byd/',
]

not_valid_url = [
    [4, 'ftp://123.fds'],
    [5, 'httpss://123.fbs'],
    [6, 'https://123.fds\\'],
    [7, 'fdsjflsd'],
    [8, 'dflsjfdls.fdjls']
]