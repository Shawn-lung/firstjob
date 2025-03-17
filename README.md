# 轉折點看盤工具 (Turning Point Stock Chart Tool)

轉折點看盤工具 is a Python-based stock analysis application with a graphical interface built using PyQt. Developed as a freelance project (contracted for NT$2,500) and collaboratively implemented by **Hsiang-I, Lung** and **Vincent, Tsai**, this tool is designed to fetch and display real-time stock information along with technical indicators. It showcases skills in Python programming, GUI development, web crawling, and data visualization—capabilities highly relevant for advanced business analytics.

---

## Project Overview

The main objective of this tool is to provide users with an easy-to-use interface to monitor stock information and apply technical analysis. The application allows users to:

- **Configure a list of stock symbols:**  
  Input at least 10 stock codes (up to 100, subject to system performance).

- **Display essential stock data:**  
  - Yesterday’s closing price  
  - Today’s opening price  
  - Limit up (漲停價) and limit down (跌停價) prices  
  - Current stock price, price change, percentage change, and amplitude (振幅)  
  - Data retrieval timestamp

- **Select various time intervals for analysis:**  
  Options include 1 minute, 5 minutes, 15 minutes, 30 minutes, 60 minutes, daily, weekly, and monthly.

- **Choose technical indicators for visualization:**  
  Using **TA-Lib**, the tool supports a variety of financial indicators such as RSI, MACD, Bollinger Bands, Stochastic Oscillator, and a custom “turning point” method (similar to 寶塔線). Users can display at least three (up to five) indicators via line charts.
- **Refresh data on demand:**  
  Refresh buttons located at both the top and bottom of the interface allow users to update the displayed information and charts.

---

## Features

- **Configurable Stock List:**  
  Manage a list of stock codes (minimum 10, up to 100).

- **Comprehensive Stock Data Display:**  
  Automatically fetches and displays key stock metrics such as previous close, today’s open, limit up/down prices, current price, price change, amplitude, and the data timestamp.

- **Flexible Time Intervals:**  
  Supports multiple time intervals from 1-minute to monthly data.

- **Robust Technical Analysis with TA-Lib:**  
  - Incorporates TA-Lib to offer popular indicators like RSI, MACD, Bollinger Bands, Stochastic, and more.  
  - Includes a custom turning point indicator to highlight market inflection points.

- **User-Friendly Interface:**  
  Developed with PyQt, the GUI offers clear presentation and simple interaction:
  - Separate windows for stock and futures analysis.
  - Refresh buttons for on-demand data updates.

---

## Code Structure

The repository is organized as follows:

    firstjob/
    ├── .qt_for_python/                  # Auto-generated PyQt files
    ├── .vscode/                         # VS Code configuration files
    ├── build/                           # Build output (e.g., executable)
    ├── __pycache__/                     # Cached Python bytecode
    ├── CrawlerClass.py                  # Web crawling logic to fetch stock data
    ├── MainUi.py                        # Main user interface layout module
    ├── MainUi_controller.py             # Controller for main UI event handling
    ├── MyWidget.py                      # Custom widget implementations
    ├── futuresWindowUi.py               # Module for futures window functionality
    ├── futuresWindowUi.ui               # Qt Designer file for futures window UI
    ├── futuresWindowUi_controller.py    # Controller for futures window events
    ├── mainUI.ui                        # Qt Designer file for the main UI layout
    ├── start.py                         # Entry point to launch the application
    ├── start.spec                       # PyInstaller spec file for creating an executable
    ├── stockWindowUi.py                 # Module for stock window functionality
    ├── stockWindowUi.ui                 # Qt Designer file for stock window UI
    ├── stockWindowUi_controller.py      # Controller for stock window events
    ├── test.py                          # Test script for development/debugging
    └── favorite.json                    # JSON file for storing user preferences (e.g., favorite stocks)

- **CrawlerClass.py:** Handles web crawling to retrieve real-time stock data.  
- **MainUi.py & MainUi_controller.py:** Define and control the main application interface.  
- **stockWindowUi/** and **futuresWindowUi/**: Manage the UI and logic for displaying stock and futures data, respectively.  
- **start.py:** The main entry point to launch the application.

---

## Installation & Setup

1. **Clone the Repository:**

       git clone https://github.com/Shawn-lung/firstjob.git
       cd firstjob

2. **Set Up a Virtual Environment (Optional but Recommended):**

       python -m venv env
       source env/bin/activate   # On Windows: env\Scripts\activate

3. **Install Dependencies:**

   The application primarily relies on PyQt (PyQt5 or PySide2) and other standard Python libraries. Install dependencies via:

       pip install -r requirements.txt

   Note: If a `requirements.txt` file is not provided, you may need to install PyQt manually:

       pip install PyQt5

4. **Run the Application:**

       python start.py

   Alternatively, run the provided executable (`start.exe`) if available.

---

## Usage Instructions

- **Configuring Stocks:**  
  Update the stock symbol list (or the corresponding configuration file) as needed.

- **Selecting Time Intervals & Indicators:**  
  Use the GUI controls to choose your preferred time interval (e.g., 1m, 5m, 15m, etc.) and select which technical indicators to display.

- **Refreshing Data:**  
  Click the refresh buttons (located at both the top and bottom of the interface) to fetch the latest stock information and update the charts.

---

## Future Improvements

- **Data Caching:**  
  Enhance performance by implementing caching mechanisms for faster data retrieval.
- **Interactive Dashboard:**  
  Consider developing a more dynamic dashboard for real-time monitoring and customization.
- **Error Handling & Logging:**  
  Improve robustness with better error handling and logging features.

---


## Contact

For any questions, feedback, or further information, please contact:

- **Hsiang-I, Lung and Vincent, Tsai**  
- **Email:** lunghsiangi@gmail.com  

