document.addEventListener("DOMContentLoaded", () => {
  const weatherInfo = document.getElementById("weather-info");

  function updateWeatherInfo(weatherData) {
    const location = weatherData.name;
    const temperatureCelsius = weatherData.main.temp; // Temperature in Celsius
    const temperatureFahrenheit = Math.round((temperatureCelsius * 9/5) + 32);  

    const weatherHTML = `
      <p class=text-center>${location} - ${temperatureFahrenheit}°F</p>
    `;

    weatherInfo.innerHTML = weatherHTML;
  }

  function fetchWeatherByLocation() {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(async position => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        try {
          const response = await fetch(`/weather?lat=${latitude}&lon=${longitude}`);
          const weatherData = await response.json();

          updateWeatherInfo(weatherData);
        } catch (error) {
          console.error("Error fetching weather data:", error);
        }
      });
    } else {
      console.error("Geolocation is not available in this browser.");
    }
  }

  fetchWeatherByLocation();
});
