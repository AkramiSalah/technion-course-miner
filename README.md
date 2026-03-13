# This repo's goal is doing some data mining using python


## Status: WIP
This project is currently transitioning from a simple scraper to a CLI utility.

## Recent Major "Update": Architecture Refactor
The project has been refactored from a standalone script to a modular CLI tool.

Dispatcher Pattern: Implemented a command dispatcher to handle multiple utilities, and support easy addition of future utils.

Separation of Concerns: Split logic into dedicated modules for loading, mining, and saving.

CLI Interface: Now uses argparse with subcommands (e.g., mine, filter).



## A few notes on legality and ethics:
* as of right now (2026-03-13) the scraped sites's[ robots.txt](https://students.technion.ac.il/robots.txt) DOES NOT EXIST
* i have not found anything about usage policy of this site.
* im not completly sure this is legal, im not a lawer, but after googling and asking gemeni, gpt and claude to be sure, it seems like this is fine
* with all that being said. my script has a delay between requests of 0.5-1.5 seconds (uniformly distributed) as to not DDOS the site.

Note: This tool is for educational data mining purposes. Please respect my wishes, and do not remove the delay between scraping requests to the technion servers.

# Usage and Depdencies:
* must have python3.
* must have bs4.

to run the script:
`python3 main.py [COMMAND] [FLAGS]` in the terminal.

## Currently Available Commands:

* mine: Scrapes course data from the Technion student portal.

```
-i: Path to input IDs (default: data/course_ids.json)

-o: Path to output results (default: data/technion_courses.json)
```
filter (Coming Soon): Utility to filter scraped data by semester or prerequisites.


---

the script assume that course_ids.json has the ids of the courses you want to scrape in this format:
```json
{
    "ids":[
        <course_id_1>,
              .
              .
              .
        <course_id_N-1>,
        <course_id_N>
    ]
}
```

Note: in the technion each course has two id version, one thats 6-digits and one thats 8-digits, this script supports both.

# design choices:
* the dispatcher design pattern was used when scraping the sections to keep the DRY principle and to keep future maintanance easy if they change/add/augment the sections in the general info card.
* i went with a simple functional type of architechture with no state as opposed to going full OOP with state managemnet because honestly, this data pipeline kind of mini-project really doesnt need that, i considered doing that for the learning experience but adding that would just be noise for no reason.



## Learning Goals (Ongoing)
Since this project has evolved from a simple script to a bigger CLI , my current goals are:

* Software Architecture: I want to go deeper into Software Architechture and explore non OOP ways.

* Data Pipelining: Developing a clean "Load -> Transform -> Store" workflow that separates IO from core logic.

* Pythonic Patterns: I want to delve deep into more advanced python features.

* Making Robust CLI Tools: Learn to use argparse to create a comfortable user experience (subcommands, flags, and automated help menus), kinda like how git is.



# Final Notes:
* the technion_courses.json contains the result of running the script with the provided course_ids.json 
* the provided course_ids.json has all courses in List A(all available CS department courses) in the english version of the technion's CS department [curriculum](https://undergraduate.cs.technion.ac.il/wp-content/uploads/2025/11/computer-science-catalog-2025-26-for-website-final.pdf).

### Output Format
The script generates a `technion_courses.json` with the following structure:
* `course_id`: 6-digit unique identifier.
* `pre_requisites`: Full string preserving logic (AND/OR).
* `no_extra_credit_courses`: A list of overlapping courses.
* `recent_semesters`: List of terms the course was offered.