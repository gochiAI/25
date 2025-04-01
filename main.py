import os
import requests

# 保存先のベースディレクトリ
base_dir = os.getcwd()

# ダウンロードする画像のリスト
images_to_download = [
    "core_sys/images/main/first/icon.jpg",
    "core_sys/images/main/common/door.png",
    "core_sys/images/main/title/title.jpg",
    "core_sys/images/main/op/text.png",
    "core_sys/images/main/op/head.png",
    "core_sys/images/main/op/scene01.jpg",
    "core_sys/images/main/op/scene02.jpg",
    "core_sys/images/main/op/scene03.jpg",
    "core_sys/images/main/op/scene04.jpg",
    "core_sys/images/main/clear/kv1.jpg",
    "core_sys/images/main/clear/kv2.jpg",
    "core_sys/images/main/clear/congratu.jpg",
    "core_sys/images/main/clear/wall1_thumb.jpg",
    "core_sys/images/main/clear/wall1.jpg",
    "core_sys/images/main/clear/wall2_thumb.jpg",
    "core_sys/images/main/clear/wall2.jpg",
    "core_sys/images/main/clear/logo.svg"
]

# キャラクターごとの画像をダウンロード
characters = ["aoyama", "rize", "megu", "chiya", "chino", "syaro", "cocoa", "maya", "fuyu", "elu", "natsume"]
for chara in characters:
    images_to_download.append(f"core_sys/images/main/photo/thumb/{chara}.jpg")
    images_to_download.append(f"core_sys/images/main/photo/{chara}.jpg")

# ダウンロード関数
def download_image(image_path):
    url = f"https://gochiusa.com/af/{image_path}"
    filepath = os.path.join(base_dir, image_path)
    dirname = os.path.dirname(filepath)

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # HTTPエラーをチェック

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded: {url} -> {filepath}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# 画像をダウンロード
for image_path in images_to_download:
    download_image(image_path)

print("Download complete.")
