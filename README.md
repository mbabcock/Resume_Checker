# Resume_Checker
loads a word doc (docx) resume and analyzes the resume to show your skillset listed

### INTRO & Background
A friend of mine was recently looking for work and we were discussing resumes, specifically his. After our conversation I started to wonder does your resume really convey what you think it does about you.  During an less than interesting meeting that I should have been paying attention to I wrote this simple app to take in a word document (DOCX) resume and perfom basic text analytics on the document to determine if the resume matched what was trying to be conveyed.

### Required Libraries
You will need to install the following libraries in python
* matplotlib
* nltk
* python-docx

### running
C:>python resumecheck.py <path to docx file>
  example: C:>python resumecheck.py c:\temp\resume.docx
  
### future enhancements
   * need to run text through a technical taxonomy and also check for n-grams, such as 'software engineer'

