


video_file="\\\\192.168.1.223\\tmp\\金密钥\\课程视频\\环球系列\\新加坡\\2018新加坡系列讲座 带领实修菩提心.mp4"


from videocr import save_subtitles_to_file

if __name__ == '__main__':
    save_subtitles_to_file(video_path=video_file, file_path='test01.srt', lang='ch', time_start='02:00', time_end='04:00', conf_threshold=75, sim_threshold=80, use_fullframe=False, det_model_dir=None, rec_model_dir=None, use_gpu=False, brightness_threshold=None, similar_image_threshold=100, similar_pixel_threshold=25, frames_to_skip=1, crop_x=20, crop_y=600, crop_width=1240, crop_height=100)
    
     