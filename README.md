escapetools
===========
This repository aims to contain a suite of tools to aid you in liberating your data from Google and other web app vendors. As a start, we are working on actually grabbing the data, but at a later point we might re-implement alternatives to the hosted solutions.

Currently there is a PoC of a GMail harvester that is capable of grabbing emails and outputting their contents to the terminal. At a later point we will look at implementing scrapers for other hosted apps.

Roadmap
-------
For the GMail case, the plan is to get the scraper to a state where it is able to dump the email data (with attachments) into a standardized format. Then, we should clean-room implement the GMail interface (or maybe implement [a better one](http://www.vanschneider.com/work/mail/)), perhaps as a skin for RoundCube or other webmail middleware -- needs investigation).
