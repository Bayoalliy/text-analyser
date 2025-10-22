# 🧩 String Analyzer Service (Stage 1 Task)

Welcome to **Stage 1** of the String Analyzer Project! :dart:  
This RESTful API service analyzes strings, computes their properties, and stores them in **MongoDB** for retrieval and filtering.

---

## 🎯 Overview

The **String Analyzer Service** performs detailed analysis on any given string.  
For each analyzed string, it computes and stores the following:

- **length** → Number of characters  
- **is_palindrome** → Whether the string reads the same forwards and backwards (case-insensitive)  
- **unique_characters** → Count of distinct characters  
- **word_count** → Number of whitespace-separated words  
- **sha256_hash** → SHA-256 hash (unique identifier)  
- **character_frequency_map** → Dictionary mapping each character to its count  

---

## 🚀 API Endpoints

### 1️⃣ Create / Analyze String
**POST** `/strings`

#### Request Body
```json
{
  "value": "string to analyze"
}
