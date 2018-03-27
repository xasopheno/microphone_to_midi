import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Audio.Components.Generator import Generator
from Audio.Components.args.record_options import record_options

if __name__ == '__main__':
    args = record_options()
    print('args: ', args)

    generator = Generator(args=args)
    generator.generate()
