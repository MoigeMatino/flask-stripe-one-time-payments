console.log("Sanity check!");

// Get Stripe publishable key
fetch("/stripe/config")
.then((result) => { return result.json(); })
.then((data) => {
  
  // Initialize Stripe.js
  const stripe = Stripe(data.public_key);

  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/stripe/create-checkout-session")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});