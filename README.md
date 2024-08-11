<p align="center">
  <img src="https://github.com/ababoude/BillWordFinder/blob/main/images/logo.png" width="300"/>
</p>
<h1 align="center">BWF : Bill Word Finder</h1>
<p align="center">
  <img src="https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Version_:-3.1-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/github/forks/ababoude/BillWordFinder?style=for-the-badge&color=red"/>
  <img src="https://img.shields.io/github/stars/ababoude/BillWordFinder?style=for-the-badge&color=green"/>
  <img src="https://img.shields.io/github/contributors/ababoude/BillWordFinder?style=for-the-badge"/>
</p>

## Description 📜
<img align="right" width="400" src="https://github.com/ababoude/BillWordFinder/blob/main/images/bill-mabel.png">

This script is a brute-force tool designed specifically for fans of Gravity Falls to tackle challenges related to the Bill Cipher ARG (Alternate Reality Game) in 2024. It can be used to verify whether specific words are associated with certain ARG endpoints. The script offers a range of functionalities to assist users.
<br>
<br>
WE. ARE. GOING. TO. KILL. HIM.
<br>
<br>
<br>
<br>

## Features ✨

- 🔍 **Bruteforce Submit Bar**:
  - Sends POST requests with words to https://mystery.thisisnotawebsitedotcom.com/
  - Displays results based on HTTP response codes (404 for not found, 500 for internal server error, etc.).

- 📂 **Bruteforce Mystery URL**:
  - Checks for the existence of files at https://files.thisisnotawebsitedotcom.com/is-it-time-yet for each word.
  - Displays whether the file exists or not (using HEAD requests).

- 💻 **Bruteforce Computer Codes**:
  - Sends POST requests with words to https://codes.thisisnotawebsitedotcom.com/.
  - Displays results based on HTTP response codes (404 for not found, 500 for internal server error, etc.).

- ➕ **Generate Possible Combinations** (by [yBeta](https://github.com/BetaGamerYouTube)):
  - Creates all possible combinations of characters up to a specified length using a defined character set (e.g., letters, numbers, and special characters).
  - Saves these combinations to `input.txt` for further use.
  - Useful for generating potential words to test against ARG endpoints.

## Prerequisites 🛠️

- Python 3.x
- Python libraries:
  - `requests`
  - `requests-toolbelt`
  - `colorama`

You can install these libraries using pip:

```bash
pip install requests requests-toolbelt colorama
```

## Usage 🚀

1. **Clone the repository** or download the script files to your machine.

   ```bash
   git clone https://github.com/ababoude/BillWordFinder.git
   cd BillWordFinder
   ```

2. **Prepare the input file**:
   - Create a text file named `input.txt` in the same directory as the script.
   - Add each word to test on a new line.

3. **Run the script**:
   - Use the following command to execute the script:

     ```bash
     python BillWordFinder.py
     ```

## Example 📊

Here's an example of running the script:
<p align="center">
  <img src="https://github.com/ababoude/BillWordFinder/blob/main/images/term.png" width="700"/>
</p>

## Contributing 🤝

| Contributors  | Additions     |
| ------------- | ------------- |
| [yBeta](https://github.com/BetaGamerYouTube)  | Addition of recursive word generation |

Contributions are welcome! If you have ideas to improve the script or have found bugs, please submit an [issue](https://github.com/ababoude/BillWordFinder/issues) or create a [pull request](https://github.com/ababoude/BillWordFinder/pulls).
