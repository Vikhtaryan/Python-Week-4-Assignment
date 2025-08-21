# Python-Week-4-Assignment
Program that reads a file and writes a modified version to a new file
1. modify_text(text) function
python
def modify_text(text):
    # Example modification: convert to uppercase
    return text.upper()
This function takes a string (text) as input.

It returns a modified version of that string. In this example, it converts all characters to uppercase using the upper() method.

You can customize this function to do other kinds of modifications if you want.

2. process_file(input_filename, output_filename) function
python
def process_file(input_filename, output_filename):
text
try:
    with open(input_filename, 'r', encoding='utf-8') as infile:
        content = infile.read()
text
- Tries to open the file named `input_filename` in read mode.
- Reads the entire content of the file into the variable `content`.
- `encoding='utf-8'` ensures it reads text files with UTF-8 encoding.

text
    modified_content = modify_text(content)
text
- Calls the `modify_text` function to transform the file content.

text
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content)
text
- Opens the file named `output_filename` in write mode (creates or overwrites it).
- Writes the modified content to this new file.

text
    print(f"File processed successfully. Modified content written to '{output_filename}'.")
text
- Prints a success message after writing the output file.

---

#### Exception Handling in `process_file`
text
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
text
- Catches the error if the input file is not found and informs the user.

text
except IOError:
    print(f"Error: The file '{input_filename}' cannot be read.")
text
- Catches other I/O errors related to reading the file.

text
except Exception as e:
    print(f"An unexpected error occurred: {e}")
text
- Catches any other unexpected errors and prints the error message.

---

#### 3. `main()` function
def main():
input_file = input("Enter the input filename: ").strip()

text
- Prompts the user to enter the input filename.
- `.strip()` removes any leading/trailing whitespace.

text
if not input_file:
    print("No filename provided. Exiting.")
    return
text
- If the user enters nothing (empty string), the program notifies and exits early.

text
output_file = input("Enter the output filename: ").strip()
if not output_file:
    print("No output filename provided. Exiting.")
    return
text
- Similarly, asks for the output filename and exits if none is provided.

text
process_file(input_file, output_file)
text
- Calls the `process_file()` function to perform the reading, modification, and writing.

---

#### 4. Program Entry Point
if name == "main":
main()

text
- Ensures that `main()` runs if this script is executed directly.
- This is a common Python idiom for starting a program.

---

### Summary:
- The program is interactive: it asks the user for the input and output filenames.
- It reads the input file safely, handling errors gracefully.
- It modifies the contents with a customizable function (currently uppercase).
- It writes the result to a new file.
- It provides informative messages on both success and failure.

