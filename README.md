# torrent9explorer
This python script makes it possible to make researches on the website "torrent9" and then download torrent(s)
Using Python 3 

### Setup

###### Requirements 
```$ pip install cmd2```

### Using
This application use a terminal to work, no ui (python don't support it very well)
```$ python bootstrap.py ```

### Basic commands

###### Help:
```t9explore $> help``` to list all the commands  

###### Searching:
```t9explore $> search "<query>" [-limit [<limit>]]  [-cut [<cut>]]  [-stack [<stack>]]``` to make a search on website 

| Argument | Default | Minimum | Help | Needed |
| ------ | ------ | ------ | ------ | ------ |
| <query> | - | - | String used for query | Yes |
| -limit [<limit>] | 1 | 1 | Define a search "page" limit, the program will stop analysing next page if limit is reached | No |
| -cut [<cut>] | 10 | 1 | Stop printing items after this limit reached | No |
| -stack [<stack>] | 100 | 1 | Kind of useless, but it allow you to define the "max item in a page" when printing items | No |

###### Downloading:
```t9explore $> dl <range or id>``` to download the id who want be downloaded

| Argument | Help | Exemple |
| ------ | ------ | ------ |
| [int]id | Single item, will download thi item with this id | 48, will download item with id 48 |
| [int]start-[int]end | Range, will download every item that god id between start and end | 5-23, will download all items starting with id 5 up to 23 |

### Command usage

###### Searching:
```t9explore $> search "blindspot"```
```t9explore $> search "blindspot" -limit 20 -stack 100```
```t9explore $> search "blindspot" -cut 150 -limit 30```

###### Downloading:
```t9explore $> downloadlist 12``` 
```t9explore $> downloadlist 48-52``` 
```t9explore $> downloadlist 99,100,98,72-75``` 

###### Here is a live demo created by [@thegostisdead](https://github.com/thegostisdead/)
![](https://user-images.githubusercontent.com/25646890/42424341-1390d752-830b-11e8-9f81-e4e129fddbc0.gif)

#### Authors

- **Caceres Enzo** ([@Caceresenzo](https://github.com/Caceresenzo/))
- **Dorian Hardy** ([@thegostisdead](https://github.com/thegostisdead/))