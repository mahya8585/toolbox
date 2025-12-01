# SVGファイルをpngファイルに変換するシステム
# inkscapeのダウンロードが必要です
from cairosvg import svg2png
from pathlib import Path


def convert_svg_to_png(input_path, output_path):
    """
    SVGファイルをPNGファイルに変換する関数

    :param input_path: 入力SVGファイルのパス
    :param output_path: 出力PNGファイルのパス
    """
    try:
        svg2png(url=input_path, write_to=output_path, output_width=512, output_height=512)
        print(f"    ->done")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


def file_convert(directory: Path, output_directory: Path) -> None:
    """
    ディレクトリ内のアイテムをチェックし、ディレクトリなら中のファイル名を、
    ファイルならそのファイル名を取得する関数

    :param directory: ディレクトリのパス
    """
    try:

        for item in directory.iterdir():
            if item.is_dir():
                print(f"{item.name} はディレクトリです。中のファイル:")
                # アウトプットフォルダの作成
                dir_name = item.name
                output_directory.joinpath(dir_name).mkdir(parents=True, exist_ok=True)

                for file in item.iterdir():
                    print(f"  - {file.name}")

                    # SVGをPNGに変換
                    output_file_name = file.name.replace(".svg", ".png")
                    convert_svg_to_png(str(directory.joinpath(dir_name, file.name)), str(output_directory.joinpath(dir_name).joinpath(output_file_name)))
            else:
                print(item.name)

                # SVGをPNGに変換
                output_file_name = item.name.replace(".svg", ".png")
                convert_svg_to_png(str(directory.joinpath(item.name)), str(output_directory.joinpath(output_file_name)))

    except Exception as e:
        print(f"エラーが発生しました: {e}")


# 実行

# ディレクトリパスの設定
input_svg_dir = Path("svg")
output_png_dir = Path("png")

file_convert(input_svg_dir, output_png_dir)

# convert_svg_to_png(str(input_svg), str(output_png))