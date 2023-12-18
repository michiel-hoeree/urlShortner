import random


def magic_eight_ball(question):
    antwoord = ["It is certain", "It is decidedly so", "Without a doubt", "Better not tell you now", "Cannot predict now", "Maybe rephrase the question", "Don’t count on it", "My reply is no", "Outlook not so good"]
    return random.choice(antwoord)


def remember(function):
    previosQuestions = set()
    def wrapper(question):
        if question in previosQuestions:
            return "you allready asked that"
        else:
            previosQuestions.add(question)
            return function(question)
    return wrapper


def main():
    rude8ball = remember(magic_eight_ball)
    print(rude8ball("hello"))
    print(rude8ball("hello"))


if __name__ == "__main__":
    main()