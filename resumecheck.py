import sys
import docx
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
import matplotlib.pyplot as plt


def loadResume(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    
    resume_text = ""
    for ch in fullText:
        resume_text += ch
    
    resume_text_lower = resume_text.lower()
    
    return resume_text_lower

def filteredWordList(resume_text):
    stop_words = set(stopwords.words('english')) 
    
    ##print(resume_text)
    print("\n\n\n=======\n")
    
    word_tokens = word_tokenize(resume_text) 
    word_tokens = [word.lower() for word in word_tokens if word.isalpha()]
    filtered_wordlist = [w for w in word_tokens if not w in stop_words] 
    filtered_wordlist = [] 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_wordlist.append(w) 
    
    ##print(filtered_wordlist)
    return filtered_wordlist
    
def whatIam(filtered_list):
    fdist1 = FreqDist(filtered_list)
    print("\n\nI AM A....\n\n")
    filtered_word_freq = dict((word, freq) for word, freq in fdist1.items() if not word.isdigit())
    print(filtered_word_freq)
    
    fdist1.plot(30, cumulative=False)
    plt.show()
    
def main():
    print("Welcome to the Resume Checker - This checks your resume to verify you are sending the right message")
    filename = sys.argv[1]
    resume_text = loadResume(filename)
    filtered_list = filteredWordList(resume_text)
    whatIam(filtered_list)

if __name__ == '__main__':
    main()