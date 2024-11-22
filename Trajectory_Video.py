from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
import os
from moviepy.editor import ImageSequenceClip, concatenate_videoclips, VideoFileClip
import multiprocessing as mp

# 變數定義
grid_size = 200
cell_size = 7
line_width = 1
path_width = 3  # 調整為 3
image_size = grid_size * cell_size + (grid_size + 1) * line_width

def coordinate_to_pixel(co: tuple[int, int], cell_size: int, line_width: int):
    return (
        co[0] * (cell_size + line_width) + (cell_size - 1) // 2 + line_width,
        co[1] * (cell_size + line_width) + (cell_size - 1) // 2 + line_width
    )

def generate_frame_image(args):
    frame_index, path, day, temp_folder = args
    
    image = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(image)
    
    # 繪製網格
    for i in range(grid_size + 1):
        x = i * (cell_size + line_width)
        draw.line((x, 0, x, image_size), fill="black", width=line_width)
        y = i * (cell_size + line_width)
        draw.line((0, y, image_size, y), fill="black", width=line_width)

    # 繪製路徑
    color = (255, 0, 0)  # 紅色
    draw.line(path, fill=color, width=path_width)

    # 繪製日期文字
    font_size = 24  # 調整後的字型大小
    font = ImageFont.truetype("arial.ttf", font_size)
    text = f"Day {day}"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = 10
    text_y = 10
    draw.rectangle([text_x - 5, text_y - 5, text_x + text_width + 5, text_y + text_height + 5], fill="white")
    draw.text((text_x, text_y), text, font=font, fill="black")

    frame_path = os.path.join(temp_folder, f"frame_{frame_index}.png")
    image.save(frame_path)
    return frame_path

def create_daily_videos(csv_path: str, output_folder: str, uids: list[int], day_interval: tuple[int, int]):
    temp_folder = os.path.join(output_folder, 'temp')
    os.makedirs(temp_folder, exist_ok=True)
    
    for uid in uids:
        uid_folder = os.path.join(output_folder, f'trajectory/uid{uid}')
        os.makedirs(uid_folder, exist_ok=True)
        os.makedirs(os.path.join(uid_folder, 'pic'), exist_ok=True)
        
        trajectory_df = pd.read_csv(csv_path)
        trajectory_df = trajectory_df[trajectory_df['uid'] == uid]
        trajectory_df = trajectory_df[(trajectory_df['d'] >= day_interval[0]) & (trajectory_df['d'] <= day_interval[1])]
        
        grouped = trajectory_df.groupby('d')
        days = sorted(grouped.groups.keys())
        
        for day in days:
            group = grouped.get_group(day)
            frames = [None] * 48
            path = []
            last_t = -1
            last_pixel = coordinate_to_pixel((group.iloc[0]['x'], group.iloc[0]['y']), cell_size, line_width)
            
            for _, row in group.iterrows():
                t = row['t']
                co = (row['x'], row['y'])
                pixel = coordinate_to_pixel(co, cell_size, line_width)
                
                frame_index = t % 48
                
                if t != last_t:
                    path.append(last_pixel)
                    for idx in range(last_t + 1, t):
                        if 0 <= idx < 48:
                            frames[idx] = (idx, path.copy(), day, temp_folder)
                    last_pixel = pixel
                    path = path[:-1] + [last_pixel]
                
                path.append(pixel)
                frames[frame_index] = (frame_index, path.copy(), day, temp_folder)
                last_t = t
            
            for idx in range(last_t + 1, 48):
                frames[idx] = (idx, path.copy(), day, temp_folder)
            
            with mp.Pool(mp.cpu_count()) as pool:
                image_files = pool.map(generate_frame_image, frames)
            
            # 檢查每個生成的文件是否存在
            for frame_file in image_files:
                if not os.path.exists(frame_file):
                    print(f"File not found: {frame_file}")
            
            # 創建每日影片
            video_file_temp = os.path.join(temp_folder, f'day_{day}.mp4')
            clip = ImageSequenceClip(image_files, fps=16)
            clip.write_videofile(video_file_temp, codec='libx264', preset='ultrafast', threads=mp.cpu_count())
            
            # 儲存每日最後一幀圖片
            last_frame_path = os.path.join(uid_folder, 'pic', f'day{day}.png')
            last_frame_image = Image.open(image_files[-1])
            last_frame_image.save(last_frame_path)
        
        # 確保按正確的順序連接影片
        final_clips = [VideoFileClip(os.path.join(temp_folder, f'day_{day}.mp4')) for day in days]
        final_clip = concatenate_videoclips(final_clips, method='compose')
        final_video_file = os.path.join(uid_folder, 'video.mp4')
        final_clip.write_videofile(final_video_file, codec='libx264', preset='ultrafast', threads=mp.cpu_count())
        
        # 刪除每日影片和臨時圖片
        for day in days:
            os.remove(os.path.join(temp_folder, f'day_{day}.mp4'))
        for frame_file in os.listdir(temp_folder):
            os.remove(os.path.join(temp_folder, frame_file))
    
    # 刪除臨時資料夾
    os.rmdir(temp_folder)

if __name__ == "__main__":
    csv_path = "data/Challenge Data/CityD Challenge Data.csv"
    output_folder = "result"
    uids = [0, 2, 5, 6]  # uid 列表
    day_interval = (0, 2)
    create_daily_videos(csv_path, output_folder, uids, day_interval)
