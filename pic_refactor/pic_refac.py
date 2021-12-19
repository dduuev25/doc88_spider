import os
import cv2

def file_count(dir):
    count = 0
    for dirpath,dirnames,filenames in os.walk(dir):
        for file in filenames:
            count+=1
    return count


class PicRefactor:
    def __init__(self):
        pass

    @staticmethod
    def pic_cut_batch(src_dir, target_dir, y0, y1, x0, x1):
        try:
            for img in os.listdir(src_dir):
                img_path = os.path.join(src_dir, img)
                _img = cv2.imread(img_path)
                cropped = _img[y0:y1, x0:x1]
                cv2.imwrite(os.path.join(target_dir, img), cropped)
                print(str(img) + " done!")
            print("All done!")
        except Exception as ee:
            print(ee)

    @staticmethod
    def pic_batch_proc(src_dir,target_dir, y0, y1, x0, x1):
        for i in range(file_count(src_dir)):
            img_path = os.path.join(src_dir, str(i+1)+".png")
            print(img_path)
            _img = cv2.imread(img_path)
            cropped = _img[y0:y1, x0:x1]
            cv2.imwrite(os.path.join(target_dir, str(i+1)+".png"), cropped)
            print(str(i+1)+".png " + " done!")
        print("All done!")




    @staticmethod
    def pic_cut_single(src_file,target_dir,new_fname,y0,y1,x0,x1):
        try:
            _img = cv2.imread(src_file)
            cropped = _img[y0:y1, x0:x1]
            cv2.imwrite(os.path.join(target_dir, new_fname), cropped)
            print("done!")
        except Exception as ee:
            print(ee)

if __name__ == "__main__":
    src_dir = 'D:\\screenshots\\fluent_python_f'
    target_dir = 'D:\\screenshots\\fluentp'
    y0, y1, x0, x1 = 490, 3306, 0, 2160
    PicRefactor.pic_batch_proc(src_dir, target_dir, y0, y1, x0, x1)
    # PicRefactor.pic_cut_batch(src_dir, target_dir, y0, y1, x0, x1)
    # print(file_count(src_dir))
    # # PicRefactor.pic_batch_print(src_dir)

