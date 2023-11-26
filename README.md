# Flask Weather App

The Flask Weather App is a simple web application that utilizes a weather API to provide real-time weather information. This project is built with Flask, a lightweight web framework for Python, and it allows users to retrieve current weather details for a specified location.

## Features

- **Current Weather Data:** Fetch and display real-time weather information.
- **User-Friendly Interface:** A clean and intuitive web interface for an optimal user experience.
- **API Integration:** Utilizes a weather API to retrieve accurate and up-to-date data.

## Getting Started

Follow these steps to set up and run the Flask Weather App:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hima890/flaskWheatherAPP.git
   cd flaskWheatherAPP
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key:**

   Obtain a free API key from a weather data provider and replace the placeholder in the `config.py` file with your key.

4. **Run the Application:**

   ```bash
   python app.py
   ```

   Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the Flask Weather App.

## Configuration

In the `config.py` file, you can customize settings such as the API key, units for temperature (e.g., Celsius or Fahrenheit), and other preferences.

## Technologies Used

- Flask: A micro web framework for Python.
- Weather API: Utilizes a weather data provider's API for current weather information.

## Contributing

Contributions to enhance features, fix bugs, or optimize code are welcome. Please check the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
