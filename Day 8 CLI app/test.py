import click

class cli:
    @click.command()
    @click.option('--name', default="marni", help="masukkan nama")
    @click.argument('name')
    def hello(name):
        print("Hello {}!".format(name))

if __name__ == "__main__":
    cli.hello()