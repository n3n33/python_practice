class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit(): # 숫자 인지 판별
                digits.append(log) # 숫자로 변환 가능한 로그 저장
            else:
                letters.append(log) # 숫자로 변환 불가능한 로그 저장

        # 식별자 제외한 문자열 [1:] 을 키로 정렬, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]) )
        return letters + digits
    
        
