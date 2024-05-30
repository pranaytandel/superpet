function  updateQuantity (opertion,productId)
{
   const inputbox = document.getElementById("quantity"+productId);
   inputbox.value=parseInt(inputbox.value)+opertion;
}