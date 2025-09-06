def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for word in babbling:
        prev = ""
        i = 0
        valid = True
        while i < len(word):
            matched = False
            for sound in sounds:
                if word.startswith(sound, i) and sound != prev:
                    prev = sound
                    i += len(sound)
                    matched = True
                    break
            if not matched:
                valid = False
                break
        if valid:
            answer += 1
    return answer