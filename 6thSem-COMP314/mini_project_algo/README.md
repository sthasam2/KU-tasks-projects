# COMP314 (Algorithm and Complexity) Mini Project

A web crawler that collects headlines of news from bbc.com.

> ### Important NOTE: scraped kathmandupost.com instead

## Problem Statement

Write a web crawler that collects headlines of news from bbc.com. Start from bbc.com, crawl to different categories listed on that page (such as news, sport, worklife, travel etc.). Under each category there may be subcategories such as cricket, tennis, formula 1, football etc. under sport. Collect at most 15 news headlines from each subcategory. Hint: use BFS. You might need to throttle your requests to avoid rate limiting and getting blocked.
