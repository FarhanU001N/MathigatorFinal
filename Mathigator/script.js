import Mathfield from //unpkg.com/mathlive/dist/mathlive.min.js;
const mf = document.querySelector('#formula');
const latexField = document.querySelector('#latex');
latexField.addEventListener('input', () => 
  mf.setValue(latexField.value)
);
function updateLatex() {
  document.querySelector('#latex').value = mf.value;
}
mf.addEventListener('input', updateLatex);
updateLatex();
document.getElementById('formula').addEventListener('input',(ev) => {
    // `ev.target` is an instance of `MathfieldElement`
    console.log(ev.target.value);
});
import Math;
e=Math.floor(Math.random() * 10);