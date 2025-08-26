function bubbleSort(a, n, k) {
    for (let last = n; last >= 2; last--) {
        for (let i = 0; i < last; i++) {
            if (a[i] > a[i + 1]) {
                temp = a[i + 1]
                a[i + 1] = a[i]
                a[i] = temp

                k -= 1
                if (k === 0) {
                    console.log(a[i], a[i + 1])
                    return
                }
            }
        }
    }

    console.log(-1)
}

function solution(path = '/dev/stdin') {
    let input = require('fs').readFileSync(path).toString().split('\n');
    let first = input[0].split(" ")
    let n = parseInt(first[0])
    let k = parseInt(first[1])
    let a = input[1].trim().split(" ").map(v => Number(v))

    bubbleSort(a, n, k)
}

solution()