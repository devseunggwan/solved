function solution(path = '/dev/stdin') {
    let input = require('fs').readFileSync(path).toString().split('\n');
    let len = input[0].length;
    let n = parseInt(input[0]);
    let answer = 0;
    
    while (true){
        n *= 2;
        if (n.toString().length == len) {
            answer += 1;
        } else {
            break;
        }
        
    }
    console.log(answer)
}

solution()