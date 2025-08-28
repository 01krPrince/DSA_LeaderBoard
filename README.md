# 📊 DSA Leaderboard Generator

This project generates a **weekly leaderboard image** from a student dataset.  
It takes data from an Excel sheet, processes it, and creates a **styled leaderboard image** with ranks, names, batches, and scores.

---

## 📂 Folder Structure

```

LEADERBOARD/
│
├── assets/
│   ├── background.png        # Background image for leaderboard
│   ├── student\_data.py       # Extracted data (auto-updated from Excel)
│
├── output/                   # Generated leaderboard images
│   └── DSA\_Leaderboard\_YYYY-MM-DD\_CodingAge.png
│
├── DSA LeaderBoard spreadsheet.xlsx   # Raw input data
├── leaderBoard.py            # Main script to generate leaderboard
└── README.md                 # Project documentation

````

---

## 🚀 How It Works

1. **Data Source**  
   - Student data is stored in `DSA LeaderBoard spreadsheet.xlsx`.  
   - The script extracts this data (ignores profile links) and saves it into `assets/student_data.py`.

2. **Leaderboard Generation**  
   - Reads the cleaned data using `pandas`.  
   - Sorts students by `Solved this week`.  
   - Creates a leaderboard image using `Pillow (PIL)`.

3. **Output**  
   - Leaderboard is saved in the `output/` folder.  
   - Filename format:  

     ```
     DSA_Leaderboard_YYYY-MM-DD_CodingAge.png
     ```

---

## 🛠️ Requirements

Install dependencies before running:

```bash
pip install pandas pillow openpyxl
````

* `pandas` → for handling Excel/CSV data
* `pillow` → for image generation
* `openpyxl` → for reading `.xlsx` files

---

## ▶️ Usage

1. Place/update your Excel file:

   ```
   DSA LeaderBoard spreadsheet.xlsx
   ```

2. Run the script:

   ```bash
   python leaderBoard.py
   ```

3. The generated leaderboard image will be saved in:

   ```
   output/DSA_Leaderboard_YYYY-MM-DD_CodingAge.png
   ```

---

## ✨ Features

* Automatically extracts student data from `.xlsx`
* Ignores unnecessary columns (like LeetCode profile links)
* Creates a **gradient-styled leaderboard image**
* Saves outputs into a separate `output/` folder with date-based filenames
* Easy to customize fonts, colors, and layout

---

## 📌 Example Output

Example leaderboard image (with sample data):

```
output/DSA_Leaderboard_2025-08-22_CodingAge.png
```

---

## 🔮 Future Improvements

* Add batch-wise filtering (K1, K2, etc.)
* Generate multiple leaderboards (daily, weekly, monthly)
* Export leaderboard as **PDF** or **HTML page**
* Auto-send leaderboard to Discord/Slack

---

👨‍💻 Maintained by **CodingAge**

```


