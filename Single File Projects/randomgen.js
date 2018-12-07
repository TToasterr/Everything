var thing = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',' ',' '];
var final = [];

function main(lookin, size, alertWhen) {
    var charamount = size - (size * 2);
    var lookingfor = lookin;
    console.log(`Looking for '${lookingfor}'`);
    console.log(`Iteration size: ${size}`);
    console.log();
    console.log();

    function generate() {
        final = [];
        // for (var i = 0; i <= (lookingfor.length) * 100; i++) {
        for (var i = 0; i < size; i++) {
            var index = Math.floor(Math.random() * thing.length);
            final.push(thing[index]);
            charamount++;
        }
    }
    var xd = 0;
    console.time(`Last ${alertWhen} iterations took`);

    while (!final.includes(lookingfor)) {
        generate();
        var contains = "";
        var done = 0;
        final = final.join('');
        if (xd % alertWhen == 0) {
            if (final.includes(lookingfor.substring(0,lookingfor.length-6))) {
                contains = lookingfor.substring(0,lookingfor.length-6);
            }
            if (final.includes(lookingfor.substring(0,lookingfor.length-5))) {
                contains = lookingfor.substring(0,lookingfor.length-5);
            }
            if (final.includes(lookingfor.substring(0,lookingfor.length-4))) {
                contains = lookingfor.substring(0,lookingfor.length-4);
            }
            if (final.includes(lookingfor.substring(0,lookingfor.length-3))) {
                contains = lookingfor.substring(0,lookingfor.length-3);
            }
            if (final.includes(lookingfor.substring(0,lookingfor.length-2))) {
                contains = lookingfor.substring(0,lookingfor.length-2);
            }
            if (final.includes(lookingfor.substring(0,lookingfor.length-1))) {
                contains = lookingfor.substring(0,lookingfor.length-1);
            }

            console.log(`Iteration #${xd}`);
            console.timeEnd(`Last ${alertWhen} iterations took`);
            console.time(`Last ${alertWhen} iterations took`);
            console.log(`Total characters generated: ${charamount}`);
            console.log(`Found '${contains}' in this iteration.`);
            console.log('');
        }
        xd++;
    }
    console.log(final);
}

// The first input is the string to search for.
// The longer the string, the longer the wait.

// The second input is the iteration size.
// This is the amount of characters it
// generates per iteration. Bigger means longer.

// The last input is when to alert you. If set
// to 1000, it will alert you every 1000 iterations.
// If 0, wont alert you. If 1, will alert you for
// every iteration.
main(' toaster ', 10000000, 1)
