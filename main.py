def sort_on(dict):
    return dict["num"]

def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            # print(file_contents) # Enable to show full text with original sentence case
            # print(f"Word count: {len(words)}") # Enable to show word count
            lowered_string = file_contents.lower()
            letters_dictionary = {}
            for char in lowered_string:
                if char.isalpha():
                    if char in letters_dictionary:
                        letters_dictionary[char] += 1
                    else:
                        letters_dictionary[char] = 1

            # Convert dictionary to list of dictionaries
            letter_list = [{"letter": letter, "num": count} for letter, count in letters_dictionary.items()]

            # Sort the list
            letter_list.sort(reverse=True, key=sort_on)
        
            # Print report of text summary including total word count and letters sorted by frequency
            print(f"--- Begin report of books/frankenstein.txt --")
            print(f"{len(words)} words found in the document\n")
            for item in letter_list:
                print(f"The '{item['letter']}' character was found {item['num']} times")
            print(f"--- End report ---")

    except FileNotFoundError:
        print("The file was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()