var toggle = document.getElementById("enable-dark-mode");
var darkTheme = document.getElementById("dark-mode-theme");

// the default theme is light
var savedTheme = localStorage.getItem("dark-mode-storage") || "light";
setTheme(savedTheme);

document.getElementById('enable-dark-mode').onclick = function() {
   alert("button was clicked");
}
toggle.addEventListener("click", () => {
  alert("button was clicked");
  if (toggle.className === "fa fa-moon-o") {
    setTheme("dark");
  } else if (toggle.className === "fa fa-sun") {
    setTheme("light");
  }
});

function setTheme(mode) {
  localStorage.setItem("dark-mode-storage", mode);

  if (mode === "dark") {
    darkTheme.disabled = false;
    toggle.className = "fa fa-sun";
    toggle.title = "Enable Light Mode";
  } else if (mode === "light") {
    darkTheme.disabled = true;
    toggle.className = "fa fa-moon";
    toggle.title = "Enable Dark Mode";
  }
}