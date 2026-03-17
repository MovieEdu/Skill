import os
import sys
import shutil

def split_text_file(file_path, chunk_size=3000):
    """
    将文本文件切分为较小的块，默认每块约3000字（约8-12分钟说话内容）。
    保留段落完整性，尽量按换行符切分。
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    # 创建输出目录
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(os.path.dirname(file_path), f"{base_name}_chunks")
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 简单切分逻辑：按行累积，不超过chunk_size
    lines = content.split('\n')
    current_chunk = []
    current_length = 0
    chunk_index = 1

    for line in lines:
        current_chunk.append(line)
        current_length += len(line)
        
        # 当积累到一定长度且遇到空行或段落结束时切分
        if current_length >= chunk_size:
            output_file = os.path.join(output_dir, f"A{chunk_index:02d}.txt")
            with open(output_file, 'w', encoding='utf-8') as out:
                out.write('\n'.join(current_chunk))
            print(f"Created: {output_file}")
            
            # 重置
            current_chunk = []
            current_length = 0
            chunk_index += 1

    # 处理剩余部分
    if current_chunk:
        output_file = os.path.join(output_dir, f"A{chunk_index:02d}.txt")
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write('\n'.join(current_chunk))
        print(f"Created: {output_file}")

    print(f"\n✅ Split complete! Files are in: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_text.py <file_path>")
    else:
        split_text_file(sys.argv[1])