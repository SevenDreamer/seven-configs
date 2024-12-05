from typer import Typer,get_app_dir
from pathlib import Path
from sconfig.database import create_db_and_tables
from sconfig.model import TrackPath

app = Typer(
    name="seven-config",
    no_args_is_help=True
)

@app.command("add")
def add_config_path(path: str):
    """
    添加当前路径为跟踪配置之一
    """
    # 将当前路径转化为绝对路径
    
    abs_path = Path(path).absolute()
    print(abs_path.name)
    # print("判断是否是目录",abs_path.is_dir())
    # print("判断是否是文件",abs_path.is_file())
    # print("递归")
    # for i in abs_path.glob('**/*'):
        # print(i.name)
    print(abs_path)

@app.command("init")
def init():
    app_dir = Path(get_app_dir(app.info.name))
    app_dir.mkdir(exist_ok=True)
    init_config_db(app_dir)

def init_config_db(app_dir):
    """
    初始化数据库记录文件目录
    
    判断数据库文件是否存在,如果不存在则创建数据库
    """
    create_db_and_tables(app_dir)
    


if __name__ == "__main__":
    app()