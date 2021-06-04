import tweepy
import json
from nltk.corpus import stopwords
import csv
import os
from IPython.display import display
import pandas as pd
sw = set(stopwords.words('english'))
#sw.remove('i')
#sw.remove('myself')
sw.remove('won')
#sw.remove('my')
#sw.remove('me')

auth = tweepy.OAuthHandler("xhZRlQX8w0RTswo40HLsFvgTQ", "zIdnLJ5IRAcbe6Y5qqMR9aogxWlenCr8tcbCrfg14MehsNJHxk")
auth.set_access_token("1304990944316461058-STSZY5wC7gglaqiVX4lytOmx3cpFLJ", "pGQPrSBC7FfnxiC9T42qbONGuSkfcsOlCMipwdMo1thUs")

def get_tweets(accountName):
    #print(accountName + "'s tweets:")
    print()
    wordlist = []
    
    alltweets = []
    new_tweets = api.user_timeline(screen_name = accountName,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = accountName,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

        
    for tweet in alltweets:
        for word in tweet.text.split():
            wordlist.append(word)

    puncList = '''!()-[]{};:'"\, <>./?$%^&*_~'''
    i = 0
    for word in wordlist:
        for character in word:
            if character in puncList:
                word = word.replace(character, "")
                wordlist[i] = word
            else:
                word = word.replace(character, character.lower())
                wordlist[i] = word
        i += 1
    j = 0
    for elem in wordlist:
        if "http" in elem:
            del wordlist[j]
        j += 1



    print()

    numToPrint = input("How many results would you like to print? ")
    
    includeF = 'X'
    while includeF != 'y' and includeF != 'n':
        includeF = input("Include common words? [y/n]: ")

    common_words = ['the','it\'s','and','to','of','a', 'in','is','will','on','for','be','with','our','they','that','have','are','he','she','it','but','not','this','at','from','just','as','then','it\'s','as','was','so','','can','out','really','an','-','new','could','about','world','day','we','no','do','too','your','much','more','see','all','has','by','or','us','when','their','says']
    unique_words = set(wordlist)
    pairs = {}
    for words in unique_words:
        pairs[words] = wordlist.count(words)
    sorted_pairs = sorted(pairs.items(), key = lambda x: x[1], reverse = True)
    k = 0
    if numToPrint == '':
        numToPrint = len(sorted_pairs)
    else:
        numToPrint = int(numToPrint)



    filename = input("Enter the name of the file: ")
    if filename == "":
        filename = "/Users/drew/Documents/Python/twitter/output/DELETEME"
    else:
        filename = "/Users/drew/Documents/Python/twitter/output/" + filename
    open_file = open(filename, 'w')
    writer = csv.writer(open_file)
        
    finalList = []
    
    if includeF == 'y':
        for n in range(0,numToPrint):
            #print(sorted_pairs[n])
            finalList.append(sorted_pairs[n])
            #writer.writerow(sorted_pairs[n])
    elif includeF == 'n':
        m = 0
        p = 0
        while p < numToPrint:
            if sorted_pairs[m][0] not in common_words and sorted_pairs[m][0] not in sw:
                #print(sorted_pairs[m])
                finalList.append(sorted_pairs[m])
                #writer.writerow(sorted_pairs[m])
                p += 1
            m += 1


    for entry in finalList:
        #print(entry)
        writer.writerow(entry)

    print()
    df = pd.DataFrame(finalList, columns=['Word', 'Frequency'])
    display(df)
    print()


    
    """
    for pair in sorted_pairs:
        if sorted_pairs[k][1] > 3:
            print(pair)
        k += 1
    """

    open_file.close()
    if ("DELETEME" in filename):
        os.remove(filename)
        
    
if __name__ == "__main__":
    # Create API object
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Successfully Authenticated")
        print("Initializing API...")
        print("Tweepy version", tweepy.__version__)
    except:
        print("Error during authentication")
    quitF = False
    userID = input("Enter a username: ")
    while quitF == False:
        print()
        get_tweets(userID)
        askAgain = input("Enter a username, or q to quit: ")
        if askAgain == "q":
            quitF = True
        else:
            userID = askAgain
