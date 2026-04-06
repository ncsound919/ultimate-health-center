// NAVIGATION
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
}

// QUICK BMI CALCULATOR (PURE JS)
function calcQuickBMI() {
  const h = document.getElementById('bmiH').value;
  const w = document.getElementById('bmiW').value;
  const resDiv = document.getElementById('bmiResult');

  if (h > 0 && w > 0) {
    const bmi = (w / ((h / 100) ** 2)).toFixed(1);
    let category = '';
    let color = '';

    if (bmi < 18.5) { category = 'Underweight'; color = '#3498db'; }
    else if (bmi < 25) { category = 'Normal'; color = '#2ecc71'; }
    else if (bmi < 30) { category = 'Overweight'; color = '#e67e22'; }
    else { category = 'Obese'; color = '#e74c3c'; }

    resDiv.innerHTML = `Your BMI is <strong>${bmi}</strong> (${category})`;
    resDiv.style.background = color;
    resDiv.classList.remove('hidden');
  } else {
    alert('Please enter valid height and weight');
  }
}

// TIPS TICKER
const tips = [
  "Stay hydrated: Drink at least 8 glasses of water a day.",
  "Move your body: Even a 10-minute walk can boost your mood.",
  "Eat the rainbow: Incorporate different colored fruits and vegetables into your meals.",
  "Prioritize sleep: Aim for 7-9 hours of quality rest each night.",
  "Practice mindfulness: Take 5 minutes to breathe deeply and focus on the present.",
  "Don't skip breakfast: Fuel your body and brain for the day ahead.",
  "Check your posture: Sit up straight and stretch regularly.",
  "Be kind to yourself: Celebrate small victories on your health journey."
];

const tickerTrack = document.getElementById('tipsTicker');
if (tickerTrack) {
  tickerTrack.innerHTML = tips.map(tip => `<span class="ticker-item">${tip} &nbsp;&nbsp;&bull;&nbsp;&nbsp; </span>`).join('');
}

// LOCALSTORAGE HELPER
const storage = {
  save: (key, data) => localStorage.setItem(key, JSON.stringify(data)),
  get: (key) => JSON.parse(localStorage.getItem(key)) || null
};

// EXPOSE FOR GLOBAL ACCESS
window.calcQuickBMI = calcQuickBMI;
