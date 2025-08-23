Run with `memray run basic.py`

Print stats with `memray stats memray-basic.py.*.bin` - replace * with number that memray generated

Running it about 5 minutes produces such results:

Base branch:
```
📏 Total allocations:
        26993744

📦 Total memory allocated:
        12.825GB

📈 Peak memory usage:
        4.169GB

📊 Histogram of allocation size:
        min: 1.000B
        -----------------------------------------------
        < 5.000B   :  1615523 ▇▇▇
        < 33.000B  :    22998 ▇
        < 193.000B : 18765005 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
        < 1.119kB  :  6492029 ▇▇▇▇▇▇▇▇▇
        < 6.476kB  :    42873 ▇
        < 37.462kB :    43551 ▇
        < 216.701kB:     8852 ▇
        < 1.254MB  :     2532 ▇
        < 7.251MB  :      281 ▇
        <=41.943MB :      100 ▇
        -----------------------------------------------
        max: 41.943MB

📂 Allocator type distribution:
         MALLOC: 24468611
         REALLOC: 2445195
         CALLOC: 77549
         MMAP: 2387
         POSIX_MEMALIGN: 2

🥇 Top 5 largest allocating locations (by size):
        - quote_from_bytes:/home/anne/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/urllib/parse.py:965 -> 3.252GB
        - __init__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:27 -> 1.764GB
        - gunzip:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/gz.py:40 -> 1.720GB
        - _parse_sitemap:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/spiders/sitemap.py:97 -> 877.911MB
        - should_follow:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/downloadermiddlewares/offsite.py:65 -> 874.143MB

🥇 Top 5 largest allocating locations (by number of allocations):
        - __init__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:27 -> 15550014
        - quote_from_bytes:/home/anne/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/urllib/parse.py:965 -> 4789693
        - should_follow:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/downloadermiddlewares/offsite.py:65 -> 1596608
        - fingerprint:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/request.py:97 -> 1596557
        - fingerprint:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/request.py:99 -> 1596550
```
