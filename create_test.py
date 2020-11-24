import os


def create_yolo_testing_data(img_folder):
    with open('test.txt', 'w') as f:
        for i in range(1, 13069):
            img_name = f'{str(i)}.png'
            line = f'data/test_obj/{img_name}\n'
            f.write(line)


if __name__ == "__main__":
    img_folder = "test"
    create_yolo_testing_data(img_folder)
