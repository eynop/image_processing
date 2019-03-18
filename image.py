import argparse

import resize


def do_resize(args, images):
    resize.resize(images, args.width, args.height)
    print('Done')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='commands', dest='command', description='valid commands', help='sub-command help')

    resize_parser = subparsers.add_parser('resize', help='resize help')
    resize_parser.add_argument('-iw', '--width', dest='width', type=float, default=None)
    resize_parser.add_argument('-ih', '--height', dest='height', type=float, default=None)
    resize_parser.set_defaults(func=do_resize)

    args, unknown = parser.parse_known_args()
    args.func(args, unknown)

