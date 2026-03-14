# Legacy Scraper v1

This directory contains the original implementation of the Technion Data Miner.

### Context
This version was built using BeautifulSoup4 to scrape HTML data from `students.technion.ac.il`. 

### Status: Deprecated
As of 2026-03-14, the Technion has deprecated the legacy student portal in favor of a new SAP based portalx system. 

### This code is preserved here for:
1. **Historical Reference:** demonstrating the original project architecture.
2. **Benchmarking:** this might be used for benchmarking agains the new planned v2.

### Architecture
* **Engine:** BeautifulSoup4 (HTML Parsing)
* **Pattern:** Command Dispatcher
* **Workflow:** Request -> HTML -> BS4 -> JSON


## Legality & Ethics
* **Robots.txt:** At the time of development, the scraped site did not have a `robots.txt`.
* **Politeness:** This script includes a mandatory uniform delay (0.5s - 1.5s) between requests. **Do not remove this.**
* **Disclaimer:** This tool was created for educational data mining purposes.
---

# Usage & Dependencies

### Prerequisites
* Python 3.x
* BeutifulSoup4

### Execution
To run the legacy scraper from this directory:
`python3 main.py mine -i data/course_ids.json -o data/technion_courses.json`