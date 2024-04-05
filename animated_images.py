import imageio.v2 as imageio

def creat_gif(image_list, gif_name, duration=0.5):
    frames = [imageio.imread(image_name) for image_name in image_list]
    imageio.mimsave(gif_name, frames, duration=duration)

if __name__ == "__main__":
    image_list = ['image.png', 'image2.png', 'image3.png']
    creat_gif(image_list, 'my_  animation.gif')