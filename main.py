
import random


sylabbles = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','y','z','ch','sh','th','str','dr','kr',
             'pr','a','e','i','o','u','ee','oa','ui','ai','oi','zorp','zip','yip','yap','chew']

moo = 'moo'


def generate_name(parts, moo):
    name = ''
    isMoo = 0
    numSyls = random.randint(2,4)
    #print(numSyls)


    for i in range(numSyls):
        if isMoo == 0:
            #print(isMoo)
            addMoo = random.randint(0,1)
            if addMoo %2 == 0:
                name += moo
                isMoo = 1
        name += parts[random.randint(0,len(parts))]

    return name


def main():
    print("Generating Cow name")
    print(generate_name(sylabbles, moo))


if __name__ == "__main__":
    main()