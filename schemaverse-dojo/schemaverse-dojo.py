""" schemaphage-dojo core functionality """
if __package__:
    from .prompt import Prompt
else:
    from prompt import Prompt
import sys

def main():
    """ Main execution thread """

    prompt = Prompt()
    prompt.prompt = 'dojo> '
    prompt.cmdloop('[+] Starting dojo interface...')

if __name__ == '__main__':
    sys.exit(main())