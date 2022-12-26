# Website-Data-Puller

This Python program makes easy to pull data from web site public html source code and saves in a txt file.
It also has a simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM), if the source web site is on Cloudflare.
You can easly change the code based on web site's code stracture.

ENJOY! 

#Used Python PyPI Modules

**Beautiful Soup**

Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

**cloudscraper**

A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM), implemented with Requests. Cloudflare changes their techniques periodically, so I will update this repo frequently.

This can be useful if you wish to scrape or crawl a website protected with Cloudflare. Cloudflare's anti-bot page currently just checks if the client supports Javascript, though they may add additional techniques in the future.

Due to Cloudflare continually changing and hardening their protection page, cloudscraper requires a JavaScript Engine/interpreter to solve Javascript challenges. This allows the script to easily impersonate a regular web browser without explicitly deobfuscating and parsing Cloudflare's Javascript.


