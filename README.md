# Gravity Falls ARG: Bill Word Finder 🕵️‍♂️🔍

## Description 📜

This script is a brute-force tool designed to help fans of *Gravity Falls* solve challenges related to the Bill Cipher ARG (Alternate Reality Game). In 2024, this script can be used to check if specific words are associated with certain ARG endpoints. The script offers three main functionalities:

1. **Bruteforce Submit Bar**: Sends POST requests to a specific URL for each word in a text file and checks the response.
2. **Bruteforce Mystery URL**: Checks if a file with each word as its name exists at a given URL using HEAD requests.
3. **Bruteforce Computer codes**: Sends POST requests to a specific URL for each word in a text file and checks the response.
4. **Generate Possible Combinations**: Creates and saves all possible combinations of characters up to a specified length to a file.

## Features ✨

- **Bruteforce Submit Bar**:
  - Sends POST requests with words to a specified URL.
  - Displays results based on HTTP response codes (404 for not found, 500 for internal server error, etc.). 🚫🔍

- **Bruteforce Mystery URL**:
  - Checks for the existence of files at a specific URL for each word.
  - Displays whether the file exists or not (using HEAD requests). 📁✅

- **Bruteforce Computer Codes**:
  - Sends POST requests with words to a specified URL.
  - Displays results based on HTTP response codes (404 for not found, 500 for internal server error, etc.). 🚫🔍

- **Generate Possible Combinations**:
  - Creates all possible combinations of characters up to a specified length using a defined character set (e.g., letters, numbers, and special characters).
  - Saves these combinations to `input.txt` for further use.
  - Useful for generating potential words to test against ARG endpoints. 🔠🗂️

## Prerequisites 🛠️

- Python 3.x 🐍
- Python libraries:
  - `requests`
  - `requests-toolbelt`
  - `colorama`

You can install these libraries using pip:

```bash
pip install requests requests-toolbelt colorama
```

## Usage 🚀

1. **Clone the repository** or download the script files to your machine. 🖥️

   ```bash
   git clone https://github.com/ababoude/BillWordFinder.git
   cd BillWordFinder
   ```

2. **Prepare the input file**:
   - Create a text file named `input.txt` in the same directory as the script.
   - Add each word to test on a new line. 📝

3. **Run the script**:
   - Use the following command to execute the script:

     ```bash
     python BillWordFinder.py
     ```

   - You will be prompted to choose one of the available options:
     - **1** for "Bruteforce Submit Bar" 
     - **2** for "Bruteforce Mystery URL"
     - **3** for "Bruteforce Computer codes"
     - **4** for "Generate possible Combinations"

   - Then, the script will ask if you want to display missed results (404 responses or errors). ❓

4. **View the results**:
   - Results will be displayed directly in the terminal with color codes indicating the status of each request. 🌈

## Example 📊

Here's an example of running the script:

```
Gravity Falls ARG : Bill Word Finder
Vers 3.0, by Ababoude (X : @ababoude_)
---------------------------------------------------------------------------
Select an option:
1. Bruteforce Submit Bar
2. Bruteforce Mystery URL
3. Bruteforce Computer [NEW]
4. Generate possible Combinations
Do you want to display missed results? (y/n): y

Checking if computer have codes...

bill [200] - Exists
```

## Contributing 🤝

Contributions are welcome! If you have ideas to improve the script or have found bugs, please submit an [issue](https://github.com/ababoude/BillWordFinder/issues) or create a [pull request](https://github.com/ababoude/BillWordFinder/pulls). 💡
