function solution(path = '/dev/stdin') {
    let input = require('fs').readFileSync(path).toString().split('\n');
    let s = input[0];

    if (s.endsWith('driip')) {
        console.log('cute');
    } else {
        console.log('not cute');
    }
}

solution()