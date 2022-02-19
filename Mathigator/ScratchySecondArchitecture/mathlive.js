document.getElementById('formula').addEventListener('input',(ev) => {
    // `ev.target` is an instance of `MathfieldElement`
    console.log(ev.target.value);
});
