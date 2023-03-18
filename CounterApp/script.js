// const add = document.querySelector(".add");
// const resetCount = document.querySelector(".reset");
// const sub = document.querySelector(".subtract");
const count = document.querySelector(".count");
const buttons = document.querySelector(".buttons");

buttons.addEventListener("click", (e) => {
  if (e.target.classList.contains("add")) {
    count.innerHTML++;
    setColor();
  }
  if (e.target.classList.contains("subtract")) {
    console.log("Subtract");
  }
  if (e.target.classList.contains("reset")) {
    count.innerHTML = 0;
    setColor();
  }
});


// add.addEventListener("click", () = > {
//    count.innerHTML++;
// })
//
// sub.addEventListener("click", () = > {
//    count.innerHTML++;
// })
//
// resetCount.addEventListener("click", () = > {
//    count.innerHTML++;
// });
