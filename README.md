# 🛒 Amazon Product Scraper with Browser-Based CSV Viewer

A multi-page Amazon product scraper built with **Selenium & BeautifulSoup** that extracts product titles, prices, and images across multiple search result pages. Results are displayed in a clean **browser-based CSV viewer** with real-time search and keyword highlighting.

---

## ✨ Features

### 🤖 Scraper (Python)
- Scrapes **multiple pages** of Amazon search results automatically
- Extracts **Product Title**, **Price**, and **Image URL** per listing
- **Smart data consistency check** — uses `min_length` to prevent index mismatch errors
- **Data cleaning** — removes quotes and commas from titles and prices for clean CSV output
- Saves each page as a **separate CSV file** (`laptops_1.csv`, `laptops_2.csv`, ...)
- Tested on **Amazon.nl, Amazon.co.uk, and Amazon.com**

### 🌐 CSV Viewer (Browser UI)
- Upload the scraped CSV directly in the browser
- Displays data in a formatted **HTML table**
- **Real-time search** — filters rows instantly as you type
- **Keyword highlighting** — matched text is visually highlighted
- Zero dependencies — pure HTML, CSS, Vanilla JavaScript

---

## 🔁 How It Works

```
Set search URL in amazon.py
        ↓
Selenium opens Amazon search page
        ↓
BeautifulSoup parses titles, prices & images
        ↓
min_length check → prevents data mismatch
        ↓
Data cleaned (quotes & commas removed)
        ↓
laptops_1.csv, laptops_2.csv ... saved
        ↓
Open index.html in browser
        ↓
Upload CSV → Browse & search products 🎉
```

---

## 🛠️ Tech Stack

| Category       | Technology                              |
|----------------|-----------------------------------------|
| Scraping       | Python, Selenium, BeautifulSoup4        |
| Data Export    | Python CSV module                       |
| Multi-page     | Loop with page range + pagination logic |
| UI             | HTML5, CSS3, Vanilla JavaScript         |
| Browser Parser | FileReader API, DOM Manipulation        |

---

## 📁 Project Structure

```
Web_Scraper_Amazon/
│
├── amazon.py     # Scraper — multi-page Amazon product scraper
├── index.html    # CSV Viewer UI — upload, display, search
├── script.js     # FileReader, table rendering & search/highlight logic
└── style.css     # Styling for the viewer interface
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Google Chrome + ChromeDriver (matching your Chrome version)

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Hirad1380/Web_Scraper_Amazon.git
cd Web_Scraper_Amazon

# 2. Install dependencies
pip install selenium beautifulsoup4
```

### Run the Scraper
```python
# In amazon.py, change the URL to any Amazon search:
url = "https://www.amazon.nl/s?k=laptops&..."

# Change number of pages to scrape:
for page in range(1, 3):  # scrapes 2 pages
```

```bash
python amazon.py
```

Files `laptops_1.csv`, `laptops_2.csv` will be created in the project folder.

### View the Results
1. Open `index.html` in your browser
2. Click **Choose a file** and upload any generated CSV
3. Browse and search the scraped products

---

## 📊 CSV Output Format

| ID | TITLE | PRICE | IMAGE |
|----|-------|-------|-------|
| 1  | Lenovo IdeaPad 3 15... | 49900 | https://... |
| 2  | HP 15s-fq5055nd... | 59900 | https://... |
| ...| ...   | ...   | ...   |

---

## 🌍 Supported Amazon Regions

| Region | URL format |
|--------|-----------|
| 🇳🇱 Amazon.nl | `https://www.amazon.nl/s?k=...` |
| 🇬🇧 Amazon.co.uk | `https://www.amazon.co.uk/s?k=...` |
| 🇺🇸 Amazon.com | `https://www.amazon.com/s?k=...` |

---

## ⚠️ Notes

> - Amazon actively detects bots — if scraping fails, try adding a delay with `time.sleep()`
> - Amazon may update their CSS class names, which could require updating the selectors in `amazon.py`
> - Use responsibly and in accordance with Amazon's Terms of Service

---

## 👨‍💻 Author

**Hirad Bayat**  
M.Sc. Applied Computer Science — University of Duisburg-Essen  
📧 Bayathirad7@gmail.com  
🔗 LinkedIn: [Hirad Bayat](https://www.linkedin.com/in/hirad-bayat)  
🐙 GitHub: [Hirad1380](https://github.com/Hirad1380)
