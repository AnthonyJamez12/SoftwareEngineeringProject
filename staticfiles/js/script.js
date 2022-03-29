const icon_switch = document.querySelectorAll('.icon_switch');
const line = document.getElementById('line');
const icon_flex = document.getElementById('icon_flex');

icon_flex.addEventListener('click', onclickthree);
function onclickthree() {
  for (const element of icon_switch) {
    element.addEventListener('click', onclick);

    function onclick(e) {
      if (e.target.offsetLeft != 0) {
        console.log(e.target.offsetLeft);
        console.log('osmaa');
        const dist = e.target.offsetLeft - 10;

        const dist2 = dist + 'px';
        line.style.left = dist2;
      }
    }
  }
}

// program for search bar animation
function openSearch() {
  document.getElementById('myOverlay').style.display = 'block';
}

function closeSearch() {
  document.getElementById('myOverlay').style.display = 'none';
}
