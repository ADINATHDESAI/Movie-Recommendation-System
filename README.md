# 🎥 Movie Recommendation System

Welcome to the **Movie Recommendation System** project! This project demonstrates a machine learning-based approach to recommend movies based on user preferences. It integrates data science techniques, natural language processing, and a user-friendly Streamlit interface to provide an engaging and intuitive experience.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)

---

## Overview

The Movie Recommendation System is built to help users discover new movies similar to their favorite ones. By leveraging a dataset of movie details and credits, the project processes textual data (overviews, genres, keywords, cast, and crew) to compute cosine similarity scores between movies. The recommendations are presented in a clean and interactive UI built using [Streamlit](https://streamlit.io/).

---

## Features

- **Data Processing:**  
  - Merges movie and credits datasets.
  - Cleans and preprocesses text data.
  - Uses stemming and tokenization for enhanced text matching.

- **Recommendation Engine:**  
  - Computes cosine similarity between movies.
  - Provides top 5 recommendations based on similarity.

- **User Interface:**  
  - Interactive movie selection via a dropdown menu.
  - Displays recommended movies along with their posters.
  - Professional and modern UI built with Streamlit.

- **Model Persistence:**  
  - Saves processed data and similarity matrix using pickle for efficient reloading.

---
> **Note:** Please refer to the `main.ipynb` file for the detailed explanation of the model building.
---
## Project Structure

```plaintext
├── app.py                 # Streamlit UI application
├── movies_dict.pkl        # Pickle file containing processed movie data
├── similarity.pkl         # Pickle file containing the similarity matrix
├── README.md              # This file
└── [Other Notebooks/Files] # Jupyter Notebooks and additional resources for data processing and model building
```
