

 # Project Name: Ethnc Products Scraper

### 1. Project Overview 
* **Target Website:** https://pk.ethnc.com/collections/rozana?page=1
* **Data Fields Extracted:** Product Name, Price, Image Link
* **Tools Used:** Python, Requests, BeautifulSoup, Pandas

### 2. Setup Instructions 
1. Clone this repo: `git clone [https://github.com/Ariba567/Ethnc-Products-Scraper]` 
2. Install dependencies: `pip install -r requirements.txt` 
3. Run script: `python scraper.py` 

### 3. Challenges & Solutions 
* **Challenge:** Dealing with dynamic image loading and finding the correct CSS classes for price and titles.
* **Solution:** I inspected the website's source code to identify that Shopify uses the `card-wrapper` class for products and the `money` class for prices. I also implemented `time.sleep(2)` to ensure the server is not overloaded and used "if-else" logic to handle cases where certain data points might be missing, preventing the scraper from crashing.
