# How this API works

Useful information

**name** = CDR, CMP, CC, CT, LMP, MS, SC, CDF, CDREAGLE,
LMPEAGLE, CDRTRAN, LMPTRAN, CDREVA, LMPEVA, NIXON,
HORNET, R, NOISE

**CDR** = Commander (Neil Armstrong)
**LMP** = Lunar Module Pilot (Buzz Aldrin)
**CMP** = Command Module Pilot (Michael Collins)

# GET SQL REQUESTS

## Request all the information from SQL

**ROUTE**: /sql/all

## Request all the information from ONE speaker

**ROUTE:** /sql/all/name


## Request all the information from MULTIPLE speakers

Delimited to three speakers

**ROUTE:** /sql/all/name1&name2&name3


## Request only comms from ONE speaker

**ROUTE:** /sql/comms/name


## Request only comms from MULTIPLE speakers

**ROUTE:** /sql/comms/name1&name2&name3


# SENTIMENT ANALYSIS

## Perform a sentiment analysis for ONE speaker

**ROUTE:** /sa/name

## Perform a sentiment analysis for MULTIPLE speakers

Delimited to three speakers

**ROUTE:** /sa/name1&name2&name3

# POSTING

**ROUTE:** /insertrow

# DELETING

**ROUTE:** /deleterow
