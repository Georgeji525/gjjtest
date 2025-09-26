# 姓名管理系统 - SQL Server版

这是一个连接SQL Server数据库的姓名管理系统，可以格式化姓名并将其存储到数据库中。

## 功能特性

- 用户输入姓名（名字和姓氏）
- 自动格式化姓名（首字母大写）
- 将姓名数据存储到SQL Server数据库
- 查看数据库中所有存储的姓名记录
- 友好的命令行界面

## 安装依赖

```bash
pip install -r requirements.txt
```

## 数据库配置

1. 创建或编辑 `.env` 文件，配置你的SQL Server连接信息：

```env
DB_SERVER=your_server_name
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 17 for SQL Server
```

2. 确保你的系统已安装SQL Server ODBC驱动程序。

## 数据库表结构

程序会自动创建以下表结构：

```sql
CREATE TABLE names (
    id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    full_name NVARCHAR(100) NOT NULL,
    created_date DATETIME DEFAULT GETDATE()
)
```

## 运行程序

```bash
python name_formatter.py
```

## 使用方法

1. 运行程序后，选择操作：
   - 选择 "1" 添加新姓名
   - 选择 "2" 查看所有已存储的姓名
   - 选择 "3" 退出程序

2. 添加姓名时：
   - 输入名字（first name）
   - 输入姓氏（last name）
   - 程序会自动格式化并保存到数据库

## 注意事项

- 确保SQL Server服务正在运行
- 确保数据库用户有创建表和读写数据的权限
- 如果连接失败，请检查 `.env` 文件中的数据库配置信息
- 程序使用加密连接，确保SQL Server支持SSL连接

## 依赖包

- `pyodbc`: SQL Server数据库连接
- `python-dotenv`: 环境变量管理