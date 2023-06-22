def solution(id_list, report, k):
    answer = {member: 0 for member in id_list}
    report_req_cnt = {}
    report_res_cnt = {}
    
    report = list(set(report))
    report = [case.strip().split() for case in report]
    
    for case in report:
        if case[0] not in report_req_cnt:
            report_req_cnt[case[0]] = set([case[1]])
        else:
            report_req_cnt[case[0]].add(case[1])
        
        if case[1] not in report_res_cnt:
            report_res_cnt[case[1]] =  1
        else:
            report_res_cnt[case[1]] += 1
        
    for res_member, cnt in report_res_cnt.items():
        if cnt >= k:
            for req_member, res_list in report_req_cnt.items():
                if res_member in res_list:
                    answer[req_member] += 1
    
    return [value for key, value in answer.items()]