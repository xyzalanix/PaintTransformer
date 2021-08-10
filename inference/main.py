from inference import run_inference

if __name__ == '__main__':
    run_inference(input_path='input/chicago.jpg',
                  model_path='model.pth',
                  output_dir='output/',
                  # whether need intermediate results for animation.
                  need_animation=True,
                  # resize original input to this size. None means do not resize.
                  resize_h=None,
                  # resize original input to this size. None means do not resize.
                  resize_w=None,
                  serial=True)          # if need animation, serial must be True.
