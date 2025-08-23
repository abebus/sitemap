Run with `memray run basic.py`

Print stats with `memray stats memray-basic.py.*.bin` - replace * with number that memray generated

Running it about 5 minutes produces such results:

`abebus/sitemap` branch:

```
📏 Total allocations:
        28776054

📦 Total memory allocated:
        13.387GB

📈 Peak memory usage:
        1.828GB

📊 Histogram of allocation size:
        min: 1.000B
        -----------------------------------------------
        < 5.000B   :  1594981 ▇▇▇
        < 32.000B  :  3669758 ▇▇▇▇▇▇
        < 181.000B : 17412734 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
        < 1.024kB  :  4278212 ▇▇▇▇▇▇▇
        < 5.792kB  :  1656928 ▇▇▇
        < 32.767kB :   116632 ▇
        < 185.363kB:    44338 ▇
        < 1.049MB  :      496 ▇
        < 5.932MB  :     1860 ▇
        <=33.554MB :      115 ▇
        -----------------------------------------------
        max: 33.554MB

📂 Allocator type distribution:
         MALLOC: 26361471
         REALLOC: 2334605
         CALLOC: 77918
         MMAP: 2058
         POSIX_MEMALIGN: 2

🥇 Top 5 largest allocating locations (by size):
        - quote_from_bytes:/home/anne/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/urllib/parse.py:965 -> 2.846GB
        - __iter__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:40 -> 1.547GB
        - gunzip:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/gz.py:41 -> 1.470GB
        - should_follow:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/downloadermiddlewares/offsite.py:65 -> 739.522MB
        - __get_sitemap_requests:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/spiders/sitemap.py:110 -> 733.299MB

🥇 Top 5 largest allocating locations (by number of allocations):
        - __iter__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:40 -> 8026156
        - __iter__:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:49 -> 7923343
        - quote_from_bytes:/home/anne/.local/share/uv/python/cpython-3.13.3-linux-x86_64-gnu/lib/python3.13/urllib/parse.py:965 -> 4049905
        - _process_sitemap_element:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/utils/sitemap.py:69 -> 1856247
        - should_follow:/home/anne/sitemap/.venv/lib/python3.13/site-packages/scrapy/downloadermiddlewares/offsite.py:65 -> 1350726
```
