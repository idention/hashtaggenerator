def generate_hashtag(s):
    if(len(s) < 140 and len(s) > 0):
        tags = s.split()
        tag = "#"
        for word in tags:
            tag += word.capitalize()
        return tag
    else:
        return False
