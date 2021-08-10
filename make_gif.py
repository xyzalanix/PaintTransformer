import glob
from PIL import Image


def main(in_dir, out_path):
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(in_dir))]
    img.save(fp=out_path, format='GIF', append_images=imgs,
             save_all=True, duration=100, loop=0)


if __name__ == '__main__':
    main(in_dir="output/chicago/*.jpg", out_path="output/chicago.gif")
