document.addEventListener("DOMContentLoaded", () => {
  const weatherInfo = document.getElementById("weather-info");
  const logWeather = document.getElementById("log-weather");
  const logLocation = document.getElementById("log-location");

  function updateWeatherInfo(weatherData) {
    const location = weatherData.name;
    const temperatureCelsius = weatherData.main.temp;
    const temperatureFahrenheit = Math.round((temperatureCelsius * 9/5) + 32);  

    const weatherHTML = `
      <p class=text-center>${location} - ${temperatureFahrenheit}°F</p>
    `;
    const logWeatherHTML = `
      ${temperatureFahrenheit}
    `

    weatherInfo.innerHTML = weatherHTML;
    logWeather.value = logWeatherHTML;
    logLocation.value = location;
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


// Setting default value to today's date 

document.addEventListener("DOMContentLoaded", () => {
  const currentDate = new Date().toISOString().split('T')[0];
  
  document.getElementById("date-input").value = currentDate;
});

document.addEventListener('DOMContentLoaded', function () {
  var logSectionLink = document.querySelector('.logSectionLink');

  logSectionLink.addEventListener('click', function (e) {
      e.preventDefault(); 
      var targetId = logSectionLink.getAttribute('href').substring(1);

      var targetSection = document.getElementById(targetId);

      if (targetSection) {
          var sectionTop = targetSection.getBoundingClientRect().top + window.scrollY;

          window.scrollTo({
              top: sectionTop,
              behavior: 'smooth' 
          });
      }
  });
});

