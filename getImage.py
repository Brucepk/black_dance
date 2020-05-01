# coding:utf-8
import os


def getImage(videoPath, imagePath):
    img_count = 1
    crop_time = 0.0
    video_duration = input('请输出你的视频时长，单位-秒:')
    while crop_time <= int(video_duration):
        os.system('ffmpeg -i %s -f image2 -ss %s -vframes 1 %s.png' %
                  (videoPath, str(crop_time), imagePath + str(img_count)))
        img_count += 1
        print(
            'Geting Image ' +
            str(img_count) +
            '.png' +
            ' from time ' +
            str(crop_time))
        crop_time += 0.1
    print('图片收集结束！！！')


if __name__ == '__main__':
    videoPath = r'/Users/brucepk/Movies/短视频素材/黑人抬棺素材/t.mov'
    imagePath = r'/Users/brucepk/Movies/短视频素材/黑人抬棺素材/image/'
    getImage(videoPath, imagePath)
