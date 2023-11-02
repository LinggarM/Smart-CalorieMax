# Smart CalorieMax: Find High-Calorie, Budget-Friendly Meals with Genetic Algorithms
A web app that utilizes **Genetic Algorithms** to generate a list of foods offering maximum calorie content within a specified budget.

## About the Project
Smart CalorieMax is a program/ web app to get **a list of foods with the highest calories** based on **the money you have (your budget)** from a given :
  * list of foods (food options),
  * calories for each food,
  * prices for each food, and
  * how much amount of money you have (budget)**.

Smart CalorieMax will provide a combination of food with the highest total calories from the food options that you give to the program with prices less or equal to your budget.

The output of the program is :
 * a list of foods (best combination with highest calories),
 * total calories, and
 * money required to get the foods.

Smart CalorieMax use **Genetic Algorithm** to determine the list of foods with the highest calories. Here are the Genetic Algorithms parameters used in this project :
* Coding/ representation technique: Binary
* Chromosome length: 10 (Can be customize by user, depend on the number of food options)
* Population size per generation: 10
* Terminal condition/ Number of generation: 50
* Initialization: Random
* Fitness function:
  * Sum(calories), if (sum(prices)) <= budget
  * 0, otherwise
* Parent selection: Roulette wheel
* Crossover/ Recombination
  * Crossover method: Single point cross over
  * Crossover rate: 0.9
* Mutation/ Variation
  * Mutation method: Binary mutation
  * Mutation rate: 0.2
* Survivor selection/ Update generation: Elitism (Best fitness)

## Screenshots
  Dashboard
  :-------------------------:
  ![Screenshots/1.%20Dashboard.png](Screenshots/1.%20Dashboard.png)
  Example Input Values on Forms
  ![Screenshots/2.%20Input%20Form.png](Screenshots/2.%20Input%20Form.png)
  Example Results
  ![Screenshots/3.%20Result.png](Screenshots/3.%20Result.png)

## Live Demo
Web App **Smart CalorieMax**: [http://xxx.xxx](http://xxx.xxx)

## Manual/ Demo Video
Demo Video Web App **Smart CalorieMax**: [Implemetasi Algoritma Genetika.mkv - Google Drive](https://drive.google.com/file/d/1K1WzoqYeEvU1BD8uuMkOEsGb2WLkBY6D/view)

## Technology Used
* HTML
* CSS
* Javascript
* Python
* Numpy
* Flask
* Genetic Algorithms

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
4. There are 5 inputs :

    1. The number of food options (E.g: 10)
    2. All of the food names (E.g: Food1, Food2, Food3, ..)
    3. All of the food calorie values (E.g: 100, 200, 150)
    4. All of the food prices, the currency is arbitrary but must be the same as the budget in input number 5. (E.g: 5000, 8000, 10000)
    5. Budget (Money you have), the currency is arbitrary but must be the same as the food prices in input number 4. (E.g: 10000)

5. Inputs example (The food names is Indonesian, and the currency is Rupiahs) :
    1. First input: 10
    2. Second input: Oatmeal, Roti, Mie Instan, Tuna, Salmon, Lele, Keju, Jamur, Apel, Alpukat
    3. Third input: 97, 265, 200, 132, 208, 122, 403, 22, 52, 160
    4. Fourth input: 7000, 10000, 5000, 20000, 20000, 10000, 5000, 5000, 30000, 7000
    5. Fifth input: 80000

## Contributors
* [Linggar Maretva Cendani](https://github.com/LinggarM) - [linggarmc@gmail.com](mailto:linggarmc@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* [Colorlib](https://colorlib.com/) for HTML templates
