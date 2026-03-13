# This repo's goal is doing some data mining using python

## A few notes on legality and ethics:
* as of right now (2026-03-13) the scraped sites's[ robots.txt](https://students.technion.ac.il/robots.txt) DOES NOT EXIST
* i have not found anything about usage policy of this site.
* im not completly sure this is legal, im not a lawer, but after googling and asking gemeni, gpt and claude to be sure, it seems like this is fine
* with all that being said. my script has a delay between requests of 0.5-1.5 seconds (uniformly distributed) as to not DDOS the site.

Note: if you use this, PLEASE DO NOT REMOVE THE DELAY!!!

## Learning goals:
* get farmilliar with beutifulsoup4 or other scraping frameowrks.
* sharpen scripting skills in general.
* sharpen python skills specifically.

## Learning results:
to be honest... i have prior experience in scraping in general, and this wasnt such a huge learning experience for me..
i didnt really get stuck at any point, and the only things i learned are:
* that uniform distribution is built into the python standart lib (and in cpp's std lib)
* that you can split only by first N occurences of a char.
* honestly the biggest learning result i made was when writing the README.md, i found out about foramatting json lol..


# Usage and Depdencies:
* must have python3.
* must have bs4.

to run the script:
`python3 mine_course_data.py` in the terminal.

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

s.t `<course_id>` is the 6-digit version of the course's id
Note: in the technion each course has two id version, one thats 6-digits and one thats 8-digits.

# design choices:
* the dispatcher design pattern was used when scraping the sections to keep the DRY principle and to keep future maintanance easy if they change/add/augment the sections in the general info card.
* i went with a simple functional type of architechture with no state as opposed to going full OOP with state managemnet because honestly, this data pipeline kind of mini-project really doesnt need that, i considered doing that for the learning experience but adding that would just be noise for no reason.

# Final Notes:
* the technion_courses.json contains the result of running the script with the provided course_ids.json 
* the provided course_ids.json has all courses in List A(all available CS department courses) in the english version of the technion's CS department [curriculum](https://undergraduate.cs.technion.ac.il/wp-content/uploads/2025/11/computer-science-catalog-2025-26-for-website-final.pdf).

### Output Format
The script generates a `technion_courses.json` with the following structure:
* `course_id`: 6-digit unique identifier.
* `pre_requisites`: Full string preserving logic (AND/OR).
* `no_extra_credit_courses`: A list of overlapping courses.
* `recent_semesters`: List of terms the course was offered.

### Possible Future Todo's:
- [ ] scrape courses for other departments.
- [ ] create a CLI search utility for the syllabus text.
- [ ] add support for mapping 8-digit IDs to 6-digit IDs.