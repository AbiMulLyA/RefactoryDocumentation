import click
from datetime import date 

class CLI:
    @click.group()
    def cliGroup():
        """Welcome to MyCliApp"""
        # a = input("whats your name ?")
        # b = input("how old are you ?")

    @cliGroup.command()
    @click.option("--name", default="Budi", help="The person to greet.")
    @click.option("--word", default="", help="Add some words to ur friend.")
    def say(name,word):
        """Simple program to say Hello"""
        print("Hi {}! {}".format(name,word) )
        print(name)
        print(word)


    @cliGroup.command("myage")
    @click.argument("birthyear", type=int)
    def my_age(birthyear):
        """How Old are You?"""
        today = date.today()
        calc = today.year - birthyear
        print("Your are {} years old".format(calc))

    @cliGroup.command("greeting")
    # @click.option("--word", default="", help="Add some words to ur friend.")
    def greeting():
        a = input("whats your name ?")
        b = input("how old are you ?")
        print(a,b)

if __name__ == '__main__':
    CLI.cliGroup()