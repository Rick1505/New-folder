// Set the date and time for the countdown
const countdownDate = new Date('April 1, 2024 00:00:00').getTime();

// Update the countdown every second
const countdown = setInterval(function() {
  // Get the current date and time
  const now = new Date().getTime();

  // Calculate the time remaining
  const distance = countdownDate - now;

  // Calculate days, hours, minutes, and seconds
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the countdown
  document.getElementById('timer').innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

  // If the countdown is over, display a message
  if (distance < 0) {
    clearInterval(countdown);
    document.getElementById('timer').innerHTML = 'Countdown is over!';
  }
}, 1000); // Update every second

const countdown2 = setInterval(function() {
    // Get the current date and time
    const now = new Date().getTime();
  
    // Calculate the time remaining
    const distance = countdownDate - now;
  
    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
    // Display the countdown
    document.getElementById('timer2').innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  
    // If the countdown is over, display a message
    if (distance < 0) {
      clearInterval(countdown);
      document.getElementById('timer2').innerHTML = 'Countdown is over!';
    }
  }, 1000); // Update every second