# Password Decrypter

In this assignment, we want to create a simple Password decrypter.

## Story

Have you ever had your password stolen by a chance? Do you use some simple password, such as "password", name of you/your loved one
or just some common word? You should probably change that. Using common words as your password is prone to be guessed, either by a person, or by a computer algorithm, as many
brute force algorithms use the most commonly used phrases/words. Today, we will play the side of an attacker.

You've read in the news, that some undergraduate student started his own viral app for chatting with friends, similar to Discord.
As you went scrolling through the website's code, you found out that it's not well written, and you figured out, that passwords of the
accounts are stored as a simple json text file. After a further investigation, you figured out the stored passwords are actually [MD5 hashes](https://en.wikipedia.org/wiki/MD5).
When you see this, you just scream out to yourself "[Not like this!](https://www.youtube.com/watch?v=8ZtInClXe1Q)".

While reading through the text file, one exact entry peaks your interest.

```json
{
  "username": "quickscoper360",
  "password": "5f4dcc3b5aa765d61d8327deb882cf99"
}
```

This hash seems familiar to you. After putting the keyword `password` into [MD5 Hash generator](https://www.md5hashgenerator.com/), you find out that it generates an MD5 hash `5f4dcc3b5aa765d61d8327deb882cf99`.
You try the `password` password for that user on the website, and bada bing, bada boom, **you're in**!

With a mischievous grin, you decide to find out, which passwords you can crack out of these entries.

## Tasks

The way our password decrypter will work is we will implement it in a way of [dictionary attack](https://en.wikipedia.org/wiki/Dictionary_attack).

###1. Implement a decrypter for one exact hash

You've rushed as soon as you saw the vulnerability on the website. You've launched the IDE and decided to implement a function in Python, which will
take a path to your file of all the saved commonly used words, and an MD5 hash (stored as a string) and find out, if the password
is present in the list of words. If it is present it will return the password, otherwise it returns `None`.

**TO DO**

Implement a function `find_password_from_file()`, which takes two arguments and returns the password found in a file.

As a file, you can use [following txt file of all words in english language](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt), 
or you can create your own text file with words you might want to use.

###2. Decrypt entire "database"

As you've written that function, you realise that's it taking longer than you wanted (it's brute force algorithm after all).
You are frustrated, that whenever you want to check multiple entries, you have to check through all the words all over again.
But then, something clicks in your head, and you decide to do it smartly and create an object, which will firstly load all
the words, create hashes for them and then go through the "database" (based on the calculations you've done already).

**TO DO**

Implement class `Decrypter`, which will have the following:
1. Constructor (a.k.a. `__init__`) - for this, you will just create attributes of your class as you see fit
2. `load_words()` - this is a method used to load the words and hashes for exact each and every word (so that you don't have to 
   recreate the hash every single time)
3. `decrypt_hash()` - this method will look at hash and check, if there is already an entry made in the Decrypter itself. 
   If it finds a password, which creates the exact same hash, then it returns it, otherwise it will return `None`.
4. `decrypt_db()` - this method will load "database" (JSON text file) and check for every entry (pair of username and password),
   if there is a password loaded in the class. If there is such a password, it will create a new entry in the final result, otherwise it will leave it blank.
   It will return list of all found combinations of username and password (format of the result is up to you, but it should return individual entries with a username and password, if there is any found).
   
   For example, the result for the entry mentioned above could be following:
   ```python3
   [ {"username": "quickscoper360", "password": "password"} ]
   ```
   But even returning it as a tuples could be a valid solution:
   ```python3
   [ ("quickscoper360", "password") ]
   ```

###3. Create a terminal client

Now that you've finished the Decrypter, everything is working nice and well. However, there is still one small
thing bugging you. The fact, that everytime you want to load a different json file, or different set of words, you have to
adjust the code and re-run it. You would want it to be an interactive application, in which you can choose what happens.

**TO DO**

Implement a terminal client, which will use your Decrypter class you've created in a previous task.
It should have a following functionality:
- display help (by typing `help` or `h`)
- input new set of words (for example by typing `new-words words.txt`)
- add words on top of your already loaded ones (for example by typing `add-words words.txt`)
- decrypt one single hash and display password (for example by using `decrypt-hash 5f4dcc3b5aa765d61d8327deb882cf99`)
- quit the application (by typing `q` or `quit`)

## Footnote
In case of any questions about the task, you can contact me on either by my email address <jan.popelas@kiwi.com>, or on Kiwi Slack.

Made by Ján Popeláš, April 2021