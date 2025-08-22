Run with `memray run basic.py `

Running it about 7 minutes I got such results:

Base branch:
```
📏 Total allocations:
        24699312

📦 Total memory allocated:
        10.775GB

📈 Peak memory usage:
        3.810GB

📊 Histogram of allocation size:
        min: 1.000B
        -----------------------------------------------
        < 5.000B   :  1368618 ▇▇
        < 32.000B  :    28355 ▇
        < 181.000B : 17775705 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
        < 1.024kB  :  4126381 ▇▇▇▇▇▇
        < 5.792kB  :  1373788 ▇▇
        < 32.767kB :    14353 ▇
        < 185.363kB:     9463 ▇
        < 1.049MB  :      545 ▇
        < 5.932MB  :     1999 ▇
        <=33.554MB :      105 ▇
        -----------------------------------------------
        max: 33.554MB

📂 Allocator type distribution:
         MALLOC: 22626481
         REALLOC: 2068894
         MMAP: 2114
         CALLOC: 1821
         POSIX_MEMALIGN: 2

🥇 Top 5 largest allocating locations (by size):
        - quote_from_bytes:/home/anne/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/urllib/parse.py:965 -> 2.779GB
        - __init__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:27 -> 1.698GB
        - gunzip:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/gz.py:40 -> 1.519GB
        - _parse_sitemap:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/spiders/sitemap.py:97 -> 752.717MB
        - should_follow:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/downloadermiddlewares/offsite.py:65 -> 746.595MB

🥇 Top 5 largest allocating locations (by number of allocations):
        - __init__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:27 -> 15037367
        - quote_from_bytes:/home/anne/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/urllib/parse.py:965 -> 4092903
        - should_follow:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/downloadermiddlewares/offsite.py:65 -> 1363644
        - fingerprint:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/request.py:97 -> 1363591
        - fingerprint:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/request.py:99 -> 1363584
```
