window.onload = () => {
    var canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    const margin = {left: 80, right: 200, bottom: 80, top: 50};
    const width = 1130 - margin.left - margin.right;
    const height = 678 - margin.top - margin.bottom;
    const axisThickness = 2;

    ctx.fillStyle = "black";
    ctx.textAlign = "center";
    ctx.fillRect(margin.left, height + margin.top, width, axisThickness);
    ctx.fillRect(margin.left, margin.top, axisThickness, height);

    for(var i = 0; i < 13; i++) {
        if(i > 0) {
            ctx.fillRect(margin.left + width / 13 * i, height + margin.top, axisThickness + (i % 2 == 0 ? 1 : -1), 10);
            ctx.fillStyle = "#EBEBEB";
            ctx.fillRect(margin.left + width / 13 * i, margin.top, axisThickness + (i % 2 == 0 ? 1 : -1), height);
            ctx.fillStyle = "black";
        }
        if(i % 2 == 0) {
            ctx.font = "bold 10pt sans-serif";
            ctx.fillText(170 + 5 * i, margin.left + width / 13 * i, height + margin.top + 30);
        }
    }

    for(var i = 0; i < 8; i++) {
        if(i > 0) {
            ctx.fillRect(margin.left - 10, height + margin.top - height / 8 * i, 10, axisThickness + (i % 2 == 1 ? 1 : -1));
            ctx.fillStyle = "#EBEBEB";
            ctx.fillRect(margin.left + axisThickness, height + margin.top - height / 8 * i, width, axisThickness + (i % 2 == 1 ? 1 : -1));
            ctx.fillStyle = "black";
        }
        if(i % 2 == 1) {
            ctx.font = "bold 10pt sans-serif";
            ctx.fillText(2500 + 500 * i, margin.left - 40, height + margin.top - height / 8 * i + 6);
        }
    }

    ctx.rotate(- Math.PI / 2);
    ctx.fillText("Body Mass (g)", -height / 2 - margin.top, 10);
    ctx.rotate(Math.PI / 2);
    ctx.fillText("Flipper Length (mm)", margin.left + width / 2, margin.top + height + 60); //TODO

    function printDataPoint(point) {
        switch(point.species) {
            case "Adelie": 
                ctx.fillStyle = "#fda246bb";
                ctx.strokeStyle = "#fda246";
                break;
            case "Chinstrap":
                ctx.fillStyle = "#ac5ad4bb";
                ctx.strokeStyle = "#ac5ad4";
                break;
            case "Gentoo":
                ctx.fillStyle = "#49a1a1bb";
                ctx.strokeStyle = "#49a1a1";
                break;
        }
        if(point.flipper_length_mm !== "NA") {
            var x = (1 - (235 - parseInt(point.flipper_length_mm)) / (235 - 170)) * width + margin.left;
            var y = (6500 - parseInt(point.body_mass_g)) / (6500 - 2500) * height + margin.top;
            var radius = parseFloat(point.bill_length_mm) / 3;
            ctx.beginPath();
            ctx.ellipse(x, y, radius, radius, 0, 0, 2 * Math.PI);
            ctx.fill();
            ctx.stroke();
        }
    }

    Papa.parse('./penglings.csv', {
        delimiter: ",",
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            results.data.forEach(e => printDataPoint(e));
        }
    });

    ctx.fillStyle = "black";
    ctx.fillText("bill_length_mm", margin.left + width + margin.right / 2, margin.top + height / 4);
    ctx.fillText("40", margin.left + width + margin.right / 2, margin.top + height / 4 + 30);
    ctx.fillText("50", margin.left + width + margin.right / 2, margin.top + height / 4 + 70);
    ctx.fillStyle = "#3f3f3f";
    ctx.beginPath();
    ctx.ellipse(margin.left + width + margin.right / 2 - 30, margin.top + height / 4 + 25, 40.0 / 3, 40.0 / 3, 0, 0, 2 * Math.PI);
    ctx.fill();
    ctx.beginPath();
    ctx.ellipse(margin.left + width + margin.right / 2 - 30, margin.top + height / 4 + 65, 50.0 / 3, 50.0 / 3, 0, 0, 2 * Math.PI);
    ctx.fill();
    
    ctx.fillStyle = "black";
    ctx.fillText("species", margin.left + width + margin.right / 2, margin.top + height / 2);
    ctx.textAlign = "left";
    ctx.fillText("Adelie", margin.left + width + margin.right / 2, margin.top + height / 2 + 30);
    ctx.fillText("Chinstrap", margin.left + width + margin.right / 2, margin.top + height / 2 + 70);
    ctx.fillText("Gentoo", margin.left + width + margin.right / 2, margin.top + height / 2 + 110);
    ctx.beginPath();
    ctx.fillStyle = "#fda246";
    ctx.ellipse(margin.left + width + margin.right / 2 - 30, margin.top + height / 2 + 25, 10, 10, 0, 0, 2 * Math.PI);
    ctx.fill();
    ctx.beginPath();
    ctx.fillStyle = "#ac5ad4";
    ctx.ellipse(margin.left + width + margin.right / 2 - 30, margin.top + height / 2 + 65, 10, 10, 0, 0, 2 * Math.PI);
    ctx.fill();
    ctx.beginPath();
    ctx.fillStyle = "#49a1a1";
    ctx.ellipse(margin.left + width + margin.right / 2 - 30, margin.top + height / 2 + 105, 10, 10, 0, 0, 2 * Math.PI);
    ctx.fill();
}