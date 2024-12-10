
#### **Comics List Cleaner** 
Clean and Expand Comic Issue Lists

#### **Description:**
This Python script processes a list of comic issues, cleans the data, and generates two output files:
1. A cleaned list of unique comic issues, expanded for issue ranges (e.g., `#1–#5` becomes individual lines for each issue).
2. A list of unique comic series extracted from the issue titles.

It handles special cases like:
- Removing unnecessary text inside parentheses while preserving valid years (e.g., `(2018)`).
- Including issue numbers with suffixes (e.g., `25.BEY`).

#### **Features:**
- Cleans and normalizes issue titles.
- Handles ranges of issues and generates individual entries.
- Preserves issue suffixes like `.BEY`.
- Removes duplicate entries, keeping only the first occurrence.
- Extracts and lists unique comic series.

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/thertemis/Comics-list-cleaner.git
   cd Comics-list-cleaner
   ```

2. Ensure you have Python 3.6 or higher installed.

3. Install required dependencies (if any). No external libraries are required for this script.

---

### **Usage**

1. Create an input file (`input.txt`) containing your raw list of comic issues.

   Example content for `input.txt`:
   ```text
   Doctor Strange (volume 2018) #9 – #12
   Avengers (2021 series) #5.BEY
   Fantastic Four (of the Future) #10
   Doctor Strange (volume 2018) #9 – #12
   ```

2. Run the script:
   ```bash
   python cleancomicslist.py
   ```

3. Check the output files:
   - `output_issues.txt`: Contains the cleaned and expanded list of issues.
   - `output_series.txt`: Contains the unique list of comic series.

---

### **Example Output**

#### Input (`input.txt`):
```text
Doctor Strange (volume 2018) #9 – #12
Avengers (2021 series) #5.BEY
Fantastic Four (of the Future) #10
Doctor Strange (volume 2018) #9 – #12
```

#### Output 1 (`output_issues.txt`):
```text
Doctor Strange (2018) #9
Doctor Strange (2018) #10
Doctor Strange (2018) #11
Doctor Strange (2018) #12
Avengers (2021) #5.BEY
Fantastic Four #10
```

#### Output 2 (`output_series.txt`):
```text
Avengers (2021)
Doctor Strange (2018)
Fantastic Four
```

---

### **Parameters**

- `input_file`: Path to the input file containing the raw list of issues.
- `output_issues_file`: Path to the output file for cleaned and expanded issues.
- `output_series_file`: Path to the output file for unique series.

---

### **Contribution**

Feel free to submit issues or pull requests to enhance the functionality or fix bugs.
