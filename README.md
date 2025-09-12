
# 🎿 Ski Search Engine

Welcome to the Ski Search Engine repository! This project provides a lightweight search engine tailored to skiing-related content, combining web crawling, indexing, and a simple user interface.

---

## 📌 Overview

The Ski Search Engine is designed to:
- Crawl skiing-related websites
- Index the content for fast retrieval
- Provide a user-friendly interface to search and explore skiing information

---

## 🧰 Technologies Used

| Tool | Purpose |
|------|--------|
| **Apache Nutch** | Web crawling and content fetching |
| **Apache Solr** | Indexing and search functionality |
| **Python** | Backend integration with Solr |
| **HTML, CSS, JavaScript** | Frontend user interface |
| **WSL (Windows Subsystem for Linux)** | Linux-based development environment on Windows |

---

## ⚙️ Setup Instructions (WSL-Based)

This project was developed using **Windows Subsystem for Linux (WSL)** to run Apache Nutch and Apache Solr in a Linux-like environment on Windows.

### 🐧 Prerequisites
- Windows 10/11 with WSL enabled  
- A Linux distribution installed via WSL (e.g., Ubuntu)  
- Java (OpenJDK 8 or 11) installed in WSL  
- Python installed in WSL  
- Apache Nutch and Apache Solr installed inside WSL

### 🔧 Setup Steps

1. **Install Apache Nutch and Solr in WSL**
   - Follow official install guides for each tool inside your WSL terminal
   - Ensure Solr is running on a port accessible from your browser (e.g., `localhost:8983`)

2. **Run the Nutch Crawler**
   - Configure seed URLs and crawl depth
   - Execute crawl commands from WSL

3. **Index with Solr**
   - Use Nutch’s indexing scripts to push data to Solr
   - Confirm indexed content via Solr’s admin UI

4. **Python Backend**
   - Run Python scripts from WSL to query Solr
   - Use Flask or another lightweight framework if needed

5. **Frontend Access**
   - Open the HTML interface in your browser (served via Python or directly as static files)
   - Enter a search query and view results

---

## 📂 Project Structure
ski-search-engine/ ├── crawler/             # Apache Nutch configs and scripts ├── indexer/             # Solr schema and indexing logic ├── backend/             # Python scripts for Solr integration ├── frontend/            # HTML, CSS, JS files for UI ├── README.md            # Project documentation






