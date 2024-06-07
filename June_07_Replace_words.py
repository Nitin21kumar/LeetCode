def replaceWords( dictionary, sentence):
    dictionary.sort(key = len)
    words = sentence.split()

    for i in range(len(words)):
        for root in dictionary:
            if words[i].startswith(root):
                words[i] = root
                break
    return " ".join(words)

if __name__ =="__main__":
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    value = replaceWords( dictionary, sentence)
    print(value)
    
    