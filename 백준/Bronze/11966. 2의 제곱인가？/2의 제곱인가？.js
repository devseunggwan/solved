function read(path = '/dev/stdin') {
    let input = require('fs').readFileSync(path).toString().split('\n');

    return input;
}

function solution() {
    let input = read();
    let n = parseInt(input[0]);

    while (n != 1) {
        if (n % 2 === 1) {
            return 0
        }
        n = n / 2
    }

    return 1
}

console.log(solution());