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