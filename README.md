# Python Script Usage

In the root folder, where the skywalker_cli.py module is included, please include the .json file to be analyzed by the application.
The .json file must follow the convention presented in the challenge, like this:

```json
[
    {
        "timestamp": "2018-12-26 18:11:08.509654",
        "translation_id": "5aa5b2f39f7254a75aa5",
        "source_language": "en",
        "target_language": "fr",
        "client_name": "easyjet",
        "event_name": "translation_delivered",
        "nr_words": 30,
        "duration": 20
    },
    {
        "timestamp": "2018-12-26 18:23:19.903159",
        "translation_id": "5aa5b2f39f7254a75bb33",
        "source_language": "en",
        "target_language": "fr",
        "client_name": "booking",
        "event_name": "translation_delivered",
        "nr_words": 100,
        "duration": 54
	}
]
```
For another example, there is a file "test.json" inside the folder test_Files. Please, do not remove or modify this file in other to not break the unit tests.

In order to run the script on MAC, on the terminal, inside the root directory of the project, please use:
	python3 skywalker_cli.py <input_file.json> <window_size>

In order to run the script on Windows, on the terminal, inside the root directory of the project, please use: 
	python skywalker_cli.py <input_file.json> <window_size>

Python must be installed in the machine that is trying to run the script.

An example call to the program: python skywalker_cli.py test_Files/test.json 10 

The program generates a .json file, called "Results.json" with the answer that was asked for, presented in the root directory.

## The getMinuteAverage function (business.py module)

This function represents the main algorithm, that loops through all the events presented in the json (ordered by date asc).

In order to optimize the loop, the events that would no longer be counted for the minutes ahead to be presented (as their window of time already passed), are removed from the events list for the next iterations.

Also, there is a break in the for loop if the present event is later then the window of time.

#### Extra points

In the Results.json, you can also see, for each window of time, the average of the words translated (average_words_translated) and the average of words translated per second (average_words_per_second).

