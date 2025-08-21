def modify_text(text):
    # Example modification: convert to uppercase
    return text.upper()

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        modified_content = modify_text(content)
        
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        
        print(f"File processed successfully. Modified content written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_file = input("Enter the input filename: ").strip()
    
    if not input_file:
        print("No filename provided. Exiting.")
        return
    
    output_file = input("Enter the output filename: ").strip()
    
    if not output_file:
        print("No output filename provided. Exiting.")
        return
    
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
