self.port.on("toggleColor", function() {
    if (document.body.style.backgroundColor == 'black' && document.body.style.color == 'white') {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'black';
    } else {
        document.body.style.backgroundColor = 'black';
        document.body.style.color = 'white';
    }
});

