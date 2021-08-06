# 导入模块
import pathlib
import pyanime4k


# 指定多个视频文件
videos = [
    pathlib.Path('video1.mp4')
]

# 进行计算  视频文件输出至./output
pyanime4k.upscale_videos(
    input_paths=videos,
    output_path=pathlib.Path('./output')
)