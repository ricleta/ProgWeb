// Wait for the DOM to be fully loaded before running scripts
document.addEventListener('DOMContentLoaded', function() {

  // --- Clock Hands Logic ---
  const hourHand = document.querySelector('.hour-hand');
  const minuteHand = document.querySelector('.minute-hand');
  const secondHand = document.querySelector('.second-hand');

  function updateClock() {
    const now = new Date();
    const seconds = now.getSeconds();
    const minutes = now.getMinutes();
    const hours = now.getHours();

    const secondsDegrees = (seconds / 60) * 360;
    const minutesDegrees = (minutes / 60) * 360 + (seconds / 60) * 6;
    const hoursDegrees = (hours / 12) * 360 + (minutes / 60) * 30;

    secondHand.style.transform = `translateX(-50%) rotate(${secondsDegrees}deg)`;
    minuteHand.style.transform = `translateX(-50%) rotate(${minutesDegrees}deg)`;
    hourHand.style.transform = `translateX(-50%) rotate(${hoursDegrees}deg)`;
  }

  setInterval(updateClock, 1000);
  updateClock();

  // --- Drag and Drop Logic ---
  const clock = document.querySelector('.analog-clock');
  
  let isDragging = false;
  let velocityX = 0;
  let velocityY = 0;
  let lastX, lastY;
  let animationFrameId;

  // When the mouse button is pressed down on the clock
  clock.addEventListener('mousedown', (e) => {
    // Stop any existing physics animation
    if (animationFrameId) {
      cancelAnimationFrame(animationFrameId);
    }

    isDragging = true;
    // Store the initial mouse position to calculate velocity
    lastX = e.clientX;
    lastY = e.clientY;
    clock.style.cursor = 'grabbing'; // Change cursor to indicate dragging
  });

  // When the mouse moves anywhere on the page
  document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    e.preventDefault();

    // Calculate velocity based on mouse movement
    velocityX = e.clientX - lastX;
    velocityY = e.clientY - lastY;

    // Update last mouse position
    lastX = e.clientX;
    lastY = e.clientY;

    // Update clock position directly
    clock.style.left = `${clock.offsetLeft + velocityX}px`;
    clock.style.top = `${clock.offsetTop + velocityY}px`;
  });

  // When the mouse button is released anywhere on the page
  document.addEventListener('mouseup', () => {
    if (!isDragging) return;
    isDragging = false;
    clock.style.cursor = 'grab'; // Change cursor back
    
    // Start the physics animation loop
    startPhysicsLoop();
  });

  function startPhysicsLoop() {
    animationFrameId = requestAnimationFrame(physicsLoop);
  }

  function physicsLoop() {
    // Apply gravity by constantly increasing the downward velocity
    velocityY += 0.5; // This is our gravity constant

    // Apply friction to slow down the clock
    velocityX *= 0.95;
    velocityY *= 0.95;

    // Calculate the new position
    let newX = clock.offsetLeft + velocityX;
    let newY = clock.offsetTop + velocityY;

    // Bounce off the walls
    if (newX < 0 || newX + clock.offsetWidth > window.innerWidth) {
      velocityX *= -0.8; // Reverse velocity and lose some energy
      newX = Math.max(0, Math.min(newX, window.innerWidth - clock.offsetWidth));
    }
    if (newY < 0 || newY + clock.offsetHeight > window.innerHeight) {
      velocityY *= -0.8; // Reverse velocity and lose some energy
      newY = Math.max(0, Math.min(newY, window.innerHeight - clock.offsetHeight));
    }

    clock.style.left = `${newX}px`;
    clock.style.top = `${newY}px`;

    // Stop the animation if the clock is barely moving
    if (Math.abs(velocityX) > 0.1 || Math.abs(velocityY) > 0.1) {
      animationFrameId = requestAnimationFrame(physicsLoop);
    }
  }
});
