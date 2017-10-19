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

	We are all born ignorant, but one must work hard to remain stupid.
	We are all pleased, but we have to struggle together to destroy.
	We are all happy, but we are all ashes.

## Future Developments
 - Sometimes the translator fails to completely translate the whole thing back to English, resulting in a few proper nouns that are actually words from another language. In the future it could check for these glitches and try again until the text is actually English.
 - It often returns the text with HTML entities in it (i.e. "\&#39;" instead of an apostrophe). This could be fixed, but I'd rather not have another dependency.
