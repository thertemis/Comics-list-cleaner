import re

# Read input from a text file
def read_input_file(file_path):
    """Reads the content of the file and returns the lines."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

# Normalize and clean parentheses
def normalize_parentheses(line):
    """
    Keeps only years inside parentheses.
    Transforms "(volume 2018)" into "(2018)".
    Removes other text within parentheses.
    """
    return re.sub(r"\((?!\d{4})[^\)]*\)", "", line)

# Generate individual lines for issue ranges
def expand_issue_ranges(line):
    """
    Processes lines containing issue ranges (e.g., #9–#20) 
    and generates a separate line for each issue number.
    """
    expanded_lines = []
    # Search for issue ranges (#9–#20)
    match = re.search(r"#(\d+)\s*–\s*#(\d+)", line)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        # Remove the range and create individual lines
        base_line = re.sub(r"#\d+\s*–\s*#\d+", "", line).strip()
        for i in range(start, end + 1):
            expanded_lines.append(f"{base_line} #{i}")
    else:
        expanded_lines.append(line.strip())
    return expanded_lines

# Filter and clean issue titles
def process_lines(lines):
    """
    Filters and cleans lines containing '#'.
    Keeps only years in parentheses.
    Handles issue ranges (#X–#Y) to generate individual lines.
    Includes issue numbers with suffixes like '.BEY'.
    """
    processed_titles = []
    for line in lines:
        # Normalize parentheses to keep only years
        line = normalize_parentheses(line)

        # Expand issue ranges and process the expanded lines
        expanded_lines = expand_issue_ranges(line)

        for expanded_line in expanded_lines:
            if "#" in expanded_line:  # Check if the line contains '#'
                # Keep only the title up to the first word after '#'
                match = re.match(r"(.*? #\d+(\.\w+)?\b)", expanded_line)
                if match:
                    processed_titles.append(match.group(1).strip())
    return processed_titles

# Remove duplicate lines, keeping the first occurrence
def remove_duplicates(titles):
    """
    Removes duplicate lines, keeping only the first occurrence.
    """
    seen = set()
    unique_titles = []
    for title in titles:
        if title not in seen:
            seen.add(title)
            unique_titles.append(title)
    return unique_titles

# Extract unique series names
def extract_series(processed_titles):
    """
    Extracts unique series names from processed titles.
    """
    series_set = set()
    for title in processed_titles:
        # Extract everything before the last `#`
        match = re.match(r"(.*) #\d+(\.\w+)?\b", title)
        if match:
            series_set.add(match.group(1).strip())
    return sorted(series_set)

# Write content to an output file
def write_output_file(output_path, content):
    """Writes titles or series to an output file."""
    with open(output_path, "w", encoding="utf-8") as file:
        for line in content:
            file.write(line + "\n")

# Main process
def main(input_file, output_issues_file, output_series_file):
    """
    Reads an input file, processes the lines to clean titles,
    removes duplicates, and generates a list of issues and unique series.
    """
    lines = read_input_file(input_file)
    processed_titles = process_lines(lines)

    # Remove duplicates, keeping the highest line
    unique_titles = remove_duplicates(processed_titles)

    # Extract unique series
    series_list = extract_series(unique_titles)

    # Write the unique issues to the output issues file
    write_output_file(output_issues_file, unique_titles)

    # Write the unique series to the output series file
    write_output_file(output_series_file, series_list)

    print(f"Files generated: {output_issues_file}, {output_series_file}")

# Execution
if __name__ == "__main__":
    # Input and output files
    input_file = "input.txt"  # Replace with the path to your input file
    output_issues_file = "output_issues.txt"  # File for unique cleaned issues
    output_series_file = "output_series.txt"  # File for unique series

    main(input_file, output_issues_file, output_series_file)
