# bulk-word-definer




bulk-word-definer is an application for defining multiple words at once! You only need to provide the application a list of words. Consequently, the application will define each word and provide the results in a text file.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need the following in order to run the application as intended on your machine:

```
An internet connection
Python 3 or above
Pip package installer for python
```

### Installing and Running the application


**Step1 - Application setup**
First clone this repository or download it manually to a working directory on your computer.
Thereafter, open terminal/cmd inside the 'bulk-word-definer' directory on your computer.
Now Run the following command in your terminal/cmd:

```
pip install -r requirements.txt
```


**Step2 - Create your own word list** 
Open 'wordsfortesting.txt' file in the 'bulk-word-definer' directory. This is a sample word list with basic english words that you can provide this application with. Each word is in a separate line and the word list is saved as a '.txt' file.  In order to create your own word list, copy all of the words you want to define using this application in a '.txt' file and separate each word by a line. Lastly, save the file in the 'bulk-word-definer' directory (the file should now have ".txt" as its format). 




**Step3 - Running the application**
Open cmd/terminal in the 'bulk-word-definer' directory. Thereafter, run the command below in the cmd/terminal.

```
py bulk-word-definer.py
```

The application is now running in your cmd/terminal.
Now the application should display a welcome message and prompt you to provide a unique name for the session. I suggest naming the session based on the name of the word list file you would like to use. To name the session I type 'wordsfortesting' without the quotation marks since I will be using 'wordsfortesting.txt' word list (you can name the session anything you want). Press enter to submit the name.  
Now the application prompts you to choose one of the two options:
1.one sentence definition ==> this means for each word only one sentence of definition will be provided
2.definitions with example sentences ==> this means the application will provide definitions as well as example sentences for each word.

To choose option 1 press enter in the terminal/cmd. 
To choose option 2 type the exclamation mark sign (!) in the terminal/cmd and press enter.

After you choose one of the two options, the application prompts you to type the full name of the word list file. Now type the full name of the word list file (including .txt extension) in the terminal/cmd and press enter. For example in my scenario since I want to define each word in the 'wordsfortesting.txt' file I type in the cmd/terminal 'wordsfortesting.txt' without the quotaion marks and press enter. 

Now the application will define the words in the list one by one. The application will show the progress by stating how many words it has defined. After the application finds the definition of all of the words, it will provide them in a '.txt' file in the  'bulk-word-definer' directory. The name of the file will be stated when the application finishes its tasks.
Open the newly created text file with the mentioned name to see all the words with their definitions!

The image below shows the bulk-word-definer application.
![bulk-word-definer App](https://i.imgur.com/Q640cwm.png)


## Contributing

Feel free to fork and expand this project! Send a pull request if you would like to add your code to the project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Farzam-MDN/JustShareKeys/releases). 

## Authors

* **Farzam Madani** - *Creation of the core application* - [Farzam-MDN](https://github.com/Farzam-MDN)

See also the list of [contributors](https://github.com/Farzam-MDN/JustShareKeys/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Farzam-MDN/JustShareKeys/blob/master/LICENSE) file for details

## Acknowledgments

* Big thanks to anyone whose library was used in this project!
