escapetools
===========
This repository aims to contain a suite of tools to aid you in liberating your data from Google and other web app vendors. As a start, we are working on actually grabbing the data, but at a later point we might re-implement alternatives to the hosted solutions.

Currently there is a PoC of a GMail harvester that is capable of grabbing emails and outputting their contents to the terminal. At a later point we will look at implementing scrapers for other hosted apps.

Roadmap
-------
For the GMail case, the plan is to get the scraper to a state where it is able to dump the email data (with attachments) into a standardized format. Then, we should clean-room implement the GMail interface (or maybe implement [a better one](http://www.vanschneider.com/work/mail/)), perhaps as a skin for RoundCube or other webmail middleware -- needs investigation).

After finishing the GMail work, we should go on with the other targets on the list below.

Targets
-------
* GMail
* Google Calendar
* Google Drive
* Facebook

Related projects
----------------
* [GMVault](https://github.com/gaubert/gmvault) has a much more mature GMail ripper than we do.
* [GMailUI](https://github.com/joscha/gmailui) is a UI toolkit for making GMail-like interfaces.
* [CSS3.Gmail.Buttons](https://github.com/AdamWhitcroft/CSS3.Gmail.Buttons) implement GMail-like buttons in pure CSS3.
* [FullCalendar](http://arshaw.com/fullcalendar/) implements a good alternative to GCal
* [Mailpile](https://github.com/pagekite/Mailpile) has a rather nice mail backend with searches and stuff.

Other links
-----------
* Google's [Data Liberation Front](http://www.dataliberation.org/). Concerns getting raw data from Google's services. 
