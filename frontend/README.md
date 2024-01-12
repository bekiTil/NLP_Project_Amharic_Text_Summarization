# Social Bot

## Table of Contents

- [Social Bot](#social-bot)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://gitlab.com/robots5915129/socialbot.git
   cd socialbot
   ```

2. **Create Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment:**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Activate Virtual Environment:**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Run the Project:**

   ```bash
   python main.py --lang en --account dailyenergies
   ```

3. **Deactivate Virtual Environment:**
   ```bash
   deactivate
   ```

## Project Structure

- `venv/`: Virtual environment directory
- `requirements.txt`: project dependencies
- `main.py`: Entry point
- `config.py`: config parser
- `content_maker.py`: generate content based on input builder's input
- `tests/`: test files
- `utils`: utility functions
