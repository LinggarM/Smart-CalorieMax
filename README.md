# Smart CalorieMax: Find High-Calorie, Budget-Friendly Meals with Genetic Algorithms
A web app that utilizes Genetic Algorithms to generate a list of foods offering maximum calorie content within a specified budget.

## About the Project
Smart CalorieMax is a program/ web app to get **a list of foods with the highest calories** based on the money you have (your budget) from a given :

  * list of foods,
  * calories for each food, and
  * how much amount of money you have (budget)**.

This program determines the list of foods with the highest calories using **Genetic Algorithm**. This program is a web-based platform, created with Flask using Python programming language. The output of the program is a list of foods, total calories, and money needed.

## Screenshots
  Dashboard | Example Input Values on Forms
  :-------------------------:|:-------------------------:
  ![Screenshots/1.%20Dashboard.png](Screenshots/1.%20Dashboard.png)  |  ![Screenshots/2.%20Input%20Form.png](Screenshots/2.%20Input%20Form.png)
  Example Results
  ![Screenshots/3.%20Result.png](Screenshots/3.%20Result.png)

## Live Demo
Web App Menu Makanan Murah Sehat Dan Berkhasiat Dengan Genetic Algorithm: [http://xxx.xxx](http://xxx.xxx)

## Technology Used
* HTML
* CSS
* Python
* Numpy
* Flask

## Manual/ Demo Video
Demo Video Web AppSmart CalorieMax : [Implemetasi Algoritma Genetika.mkv - Google Drive](https://drive.google.com/file/d/1K1WzoqYeEvU1BD8uuMkOEsGb2WLkBY6D/view)

## Installation

1. Clone this repo
   ```sh
   git clone https://github.com/LinggarM/Smart-CalorieMax
   ```
2. Open the repo folder you have cloned in your PC
3. Create a virtual environment
   ```sh
   python -m venv myenv
   ```
4. Activate the virtual environment
   ```sh
   myenv/Scripts/activate or "myenv/Scripts/activate" (Windows)
   myenv/bin/activate (Linux)
   ```
5. Install the requirements/ dependencies
   ```sh
   pip install -r requirements.txt
   ```

## Usage (Tutorials)

1. Open CMD in Repository Folder
2. Run the web app by executing this command :
   ```
   python app.py
   ```
   or :
   ```
   run Flask
   ```
3. Open the given URL
   ```
   http://127.0.0.1:5000/
   ```
5. There are 4 inputs :
    - First input: All the food names (Must be sorted according to first input)
    - Second input: All the food calorie values
    - Third input: All the food prices
    - Fourth input: Budget (Money you have)
    **Inputs example :**
    - First input: Oatmeal, Roti, Mie Instan, Tuna, Salmon, Lele, Keju, Jamur, Apel, Alpukat
    - Second input: 97, 265, 200, 132, 208, 122, 403, 22, 52, 160
    - Third input: 7000, 10000, 5000, 20000, 20000, 10000, 5000, 5000, 30000, 7000
    - Fourth input: 80000

## Contributors
* [Linggar Maretva Cendani](https://github.com/LinggarM) - [linggarmc@gmail.com](mailto:linggarmc@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* [Colorlib](https://colorlib.com/) for HTML templates
