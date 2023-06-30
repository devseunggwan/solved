function solution(participant, completion) {
    var answer = '';
    
    participant.sort();
    completion.sort();
    
    for(let i in participant){
        if(participant[i] != completion[i]) return participant[i]
    }
}