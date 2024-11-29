[>>>>>>>>>>>>>>>>>> fa <<<<<<<<<<<<<<<<](./README.md)

<img src='./a.jpg'>

## **Advanced File Management and Log Processing Tool**

This tool is a Python-based, multi-purpose utility designed for managing and processing text files, logs, and compressed archives. It is tailored to handle large datasets, extract sensitive information, and organize data efficiently. The tool provides a command-line interface for users to navigate through its features seamlessly.

---

### **Key Features**

#### **1. Text File Management (.txt)**
- **Smart Search:** Quickly search for specific keywords in text files and save the results in organized reports.
- **Automatic Deletion:** Remove text files based on specific names or contents.
- **Extract Sensitive Data:** Parse text files to extract credentials like `username:password` or `url:username:password` and save them in structured formats.

#### **2. Compressed Archive Management (.zip, .rar)**
- **Targeted Extraction:** Extract specific files or folders from archives using filters (e.g., country name).
- **Format Support:** Handles `.zip` and `.rar` formats.
- **Organized Output:** Automatically stores extracted content in predefined directories for easy access.

#### **3. Folder Management**
- **Folder Deletion:** Remove folders based on specific keywords.
- **Log Counting by Region:** Count and display the number of logs based on region codes (e.g., `US`, `FR`).

#### **4. Database Creation**
- **Log Aggregation:** Extract and consolidate data into databases in formats like `username:password` or `url:username:password`.
- **Remove Duplicates:** Identify and filter out duplicate data, ensuring only unique entries are saved.
- **Save Results:** Save both unique and non-unique data in separate output files.

#### **5. User-Friendly Interface**
- **Simple Menu:** Navigate through the tool using a command-line menu with ASCII art headers for enhanced user experience.
- **Detailed Reports:** Generate reports after each operation, including processing time and output summaries.

---

### **Installation**

#### **Dependencies**
Ensure you have Python installed and install the required libraries using the following command:
```bash
pip install colorama tqdm rarfile
```

---

### **How to Use**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the Tool:**
   ```bash
   python tool.py
   ```

3. **Navigate the Menu:**
   After running the script, you’ll see a menu like this:

   ```
    ____    ______   ___    ___       ____     __    __  ____    __  __  ____    ____       
   /\  _`\ /\__  _\ /\_ \  /\_ \     /\  _`\  /\ \  /\ \/\  _`\ /\ \/\ \/\  _`\ /\  _`\     
   \ \ \L\ \/_/\ \/ \//\ \ \//\ \    \ \ \/\_\\ `\`\\/'/\ \ \L\ \ \ \_\ \ \ \L\_\ \ \L\ \   
    \ \  _ <' \ \ \   \ \ \  \ \ \    \ \ \/_/_`\ `\ /'  \ \ ,__/\ \  _  \ \  _\L\ \ ,  /   
     \ \ \L\ \ \_\ \__ \_\ \_ \_\ \_   \ \ \L\ \ `\ \ \   \ \ \/  \ \ \ \ \ \ \L\ \ \ \\ \  
      \ \____/ /\_____\/\____\/\____\   \ \____/   \ \_\   \ \_\   \ \_\ \_\ \____/\ \_\ \_\
       \/___/  \/_____/\/____/\/____/    \/___/     \/_/    \/_/    \/_/\/_/\/___/  \/_/\/ /

   1. Extract logs from compressed archives (.zip, .rar).
   2. Search for specific queries in text files.
   3. Reduce log size by deleting files or folders.
   4. Count logs by region (folders).
   5. Create a login-password database.
   6. Create a complete database (url:login:password).
   7. Exit.
   ```

4. **Select an Option:**
   Enter the number corresponding to the desired operation and follow the on-screen instructions.

---

### **File Structure**
- **`tool.py`:** The main script containing all functionalities.
- **`result.txt`:** Output file containing processed logs.
- **`unique_entries.txt`:** File storing unique data entries.
- **`Extract/`:** Directory for storing extracted files from archives.

---

### **Use Cases**
- **Log Management:** Process and analyze system logs.
- **Data Extraction:** Extract sensitive information like credentials from text files.
- **File Cleanup:** Remove unnecessary files or folders based on user-defined criteria.
- **Database Creation:** Build structured databases for analytical purposes.

---

### **Contributing**
Feel free to fork this repository and submit pull requests with improvements or additional features. Feedback is always welcome!

**Author:** [Your Name](https://github.com/your-profile)  
**License:** MIT  

Enjoy streamlined file management and log processing! 🚀
