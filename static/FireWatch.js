document.addEventListener("DOMContentLoaded", function () {
  console.log("Document loaded and ready");

  const helperBtn = document.getElementById("helperBtn");
  const helpeeBtn = document.getElementById("helpeeBtn");

  if (helperBtn) {
    console.log("Helper button found");
    helperBtn.addEventListener("click", function () {
      console.log("Helper button clicked");
      window.location.href = "/helper";
    });
  } else {
    console.error("Helper button not found");
  }

  if (helpeeBtn) {
    console.log("Helpee button found");
    helpeeBtn.addEventListener("click", function () {
      console.log("Helpee button clicked");
      window.location.href = "/helpee";
    });
  } else {
    console.error("Helpee button not found");
  }
});
