async function getStripePublicKey(){
  try{
    const response = await axios.get('/stripe/config');
    return response.data.public_key;
  }
  catch(error){
    console.error('Error fetching Stripe public key:', error);
  }
}

document.querySelectorAll('.purchase-button').forEach(button => {
  button.addEventListener('click', async event => {
    const stripePublicKey = await getStripePublicKey()
    const stripe = Stripe(stripePublicKey)
    const stripePriceId = event.target.dataset.stripePriceId

    try{
      const response = await axios.post('/stripe/create-checkout-session',{
        price_id: stripePriceId
      });
      const session = response.data;
      const { error } = await stripe.redirectToCheckout(
        {sessionId: session.sessionId}
      );
      if (error){
        console.error('Error creating checkout session:', error);
      }
      } catch(error){
        console.error('Error creating checkout session:', error);
      }
  });
});















// console.log("Sanity check!");

// // Get Stripe publishable key
// fetch("/stripe/config")
// .then((result) => { return result.json(); })
// .then((data) => {
  
//   // Initialize Stripe.js
//   const stripe = Stripe(data.public_key);

//   document.querySelector("#submitBtn").addEventListener("click", () => {
//     // Get Checkout Session ID
//     fetch("/stripe/create-checkout-session")
//     .then((result) => { return result.json(); })
//     .then((data) => {
//       console.log(data);
//       // Redirect to Stripe Checkout
//       return stripe.redirectToCheckout({sessionId: data.sessionId})
//     })
//     .then((res) => {
//       console.log(res);
//     });
//   });
// });