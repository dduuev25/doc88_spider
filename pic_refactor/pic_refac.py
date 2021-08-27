import os
import cv2

class PicRefactor:
    def __init__(self):
        pass

    @staticmethod
    def pic_cut_batch(self,src_dir,target_dir,y0,y1,x0,x1):
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
    def pic_cut_single(self,src_file,target_dir,new_fname,y0,y1,x0,x1):
        try:
            _img = cv2.imread(src_file)
            cropped = _img[y0:y1, x0:x1]
            cv2.imwrite(os.path.join(target_dir, new_fname), cropped)
            print("done!")
        except Exception as ee:
            print(ee)