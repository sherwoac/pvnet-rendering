import argparse
import os
print(os.environ['PYTHONPATH'])
from blender.render_utils import Renderer, YCBRenderer

parser = argparse.ArgumentParser()
parser.add_argument('--type', action='store', dest='type', type=str)
args = parser.parse_args()


def run_rendering():

    # YCBRenderer.multi_thread_render()
    # renderer = YCBRenderer('037_scissors')
    # object_list = ['ape', 'can', 'cat', 'duck', 'driller', 'eggbox', 'glue', 'holepuncher']
    # object_list = ['ape', 'can', 'duck', 'driller', 'eggbox', 'glue', 'holepuncher']
    object_list = ['driller']
    for object_item in object_list:
        renderer=Renderer(object_item)
        renderer.run()


def run_fuse():
    from fuse.fuse import run
    run()


if __name__ == '__main__':
    globals()['run_' + args.type]()
