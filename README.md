# Movie Recommendation System with Flask

This project implements a movie recommendation system using Flask, a web framework for Python. The recommendation system is built using the TMDB Movie Metadata dataset, which can be found [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Directory Structure

1. **templates:** This directory contains the HTML templates for the web pages.
   - `login.html`: Login page.
   - `signup.html`: Signup page.
   - `success.html`: Page displayed upon successful login or signup.
   - `final.html`: Final recommendation page.

2. `model.py`: This file contains the code for the movie recommendation system. Run this file separately to train the model.

3. `app.py`: The main Flask application file. Run this file to start the web application.

## How to Run

1. Download all the files and place them in a folder.

2. Store the HTML files (`login.html`, `signup.html`, `success.html`, `final.html`) in the `templates` directory.

3. Run `model.py` separately in an IDE or command prompt terminal to train the recommendation model.

4. Run `app.py` to start the Flask web application. The output in the terminal will display the link where the application is hosted.

5. Access the webpage by opening the provided link in any web browser.

## Requirements

Make sure you have the necessary libraries installed. You can install them using:

```bash
pip install flask pandas scikit-learn
```

## Usage

- Visit the provided link in your web browser.
- Use the login or signup pages to access the movie recommendation system.
- Upon successful login or signup, you will be redirected to the recommendation page (`final.html`), where personalized movie suggestions will be displayed.

## Dataset

The movie recommendation system is trained on the TMDB Movie Metadata dataset, available [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). Ensure that you download and use this dataset for training the model.

## Acknowledgments

- This project uses the Flask web framework and the TMDB Movie Metadata dataset.

Feel free to explore, modify, and enhance the project as needed. If you encounter any issues or have suggestions for improvement, please let us know.
