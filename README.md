# text-befuddler
Passes text through random translation and back multiple times to add interesting new meaning

## Prerequisites
You will need [requests](http://docs.python-requests.org/en/master/), which can be installed like this:

	pip install requests

## Usage
To run type

	python main.py

## About
Scrapes from translate.com translations of input text to random languages. Returns new text after translated twice into random languages, and then back to English. Here you can see how it changes every befuddlement.

	never gonna give you up, never gonna let you down, never gonna turn around, and desert you
	And will not turn around disappointing, it's not that I don't go to desert.
	And it was not open, it was not destroyed, that I did not go in the wilderness.
	And it's not open, it's not destroyed, I'm not going to go into the desert
	And in the morning, not to destroy him I desert
	Morning, I do not have to swing to destroy it.
	No need to beat it tomorrow.
	There's no need to beat him tomorrow.
	He did not want to turn on in the morning.
	He do not want to end in the morning.
	At the end of the night.

## Future Developments
 - Sometimes the translator fails to completely translate the whole thing back to English, resulting in a few proper nouns that are actually words from another language. In the future it could check for these glitches and try again until the text is actually English.
 - It often returns the text with HTML entities in it (i.e. "\&#39;" instead of an apostrophe). This could be fixed, but I'd rather not have another dependency.
