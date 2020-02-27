def dropAt(twoot):
    counter=0
    for character in twoot:
        if character=='@':
            twoot=twoot[:counter]+twoot[counter+1:]
        counter+=1
    return twoot
