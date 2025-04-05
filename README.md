# Tornado Damage Assessment Model (TDAM)
:construction: In progress - check back soon. :construction:

## Roadmap

**Structure Classifier**: Provide a geospatial dataset (points or polygons) of structures or parcels with a "Structure Category" column, generate a classifier to categorioze the structures into NWS Damage Indicators.
    - Planned: Summer 2025
**Damage Assessment Model**: Given a tornado path polygon with EF ratings, and structures categorized into damage indicators, generate predicted damages at the structure level.
    - Planned: Fall 2025
**Tornado Path Generator**: Generate a tornado path polygon with EF ratings from points (i.e. field surveys).
    - Planned: End of 2025


## Resources
- 2018 American Meteoroligical Society presentation: [An Automated Tornado Damage Assessment Model: Providing Rapid Situational Awareness to the Federal Emergency Management Agency (FEMA)](https://ams.confex.com/ams/98Annual/meetingapp.cgi/Paper/326485)
- 2020 American Meteoroligical Society presentation: [A Tornado Damage Assessment Model and Lessons Learned from the 2019 Lee County, Alabama, EF4 Tornado](https://ams.confex.com/ams/2020Annual/webprogram/Paper365065.html)


## Usage

The Tornado Damage Assessment Model works as follows:

1. Classify Structures
The TDAM damage predictions are highly dependent on the structure classifications. Each structure needs to be mapped to a Damage Indicator. 

2. Predict Damages

