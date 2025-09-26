import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

# 加载环境变量
load_dotenv()

class NameDatabase:
    def __init__(self):
        """初始化数据库连接"""
        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_DATABASE')
        self.username = os.getenv('DB_USERNAME')
        self.password = os.getenv('DB_PASSWORD')
        self.driver = os.getenv('DB_DRIVER')
        
        self.connection_string = f"""
        DRIVER={{{self.driver}}};
        SERVER={self.server};
        DATABASE={self.database};
        UID={self.username};
        PWD={self.password};
        Encrypt=yes;
        TrustServerCertificate=yes;
        """
    
    def connect(self):
        """连接到数据库"""
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
            print("成功连接到SQL Server数据库")
            return True
        except Exception as e:
            print(f"数据库连接失败: {e}")
            return False
    
    def create_table(self):
        """创建存储姓名的表"""
        try:
            create_table_sql = """
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='names' AND xtype='U')
            CREATE TABLE names (
                id INT IDENTITY(1,1) PRIMARY KEY,
                first_name NVARCHAR(50) NOT NULL,
                last_name NVARCHAR(50) NOT NULL,
                full_name NVARCHAR(100) NOT NULL,
                created_date DATETIME DEFAULT GETDATE()
            )
            """
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print("数据表创建成功或已存在")
        except Exception as e:
            print(f"创建表失败: {e}")
    
    def insert_name(self, first_name, last_name, full_name):
        """插入姓名数据到数据库"""
        try:
            insert_sql = """
            INSERT INTO names (first_name, last_name, full_name)
            VALUES (?, ?, ?)
            """
            self.cursor.execute(insert_sql, (first_name, last_name, full_name))
            self.conn.commit()
            print(f"姓名 '{full_name}' 已成功保存到数据库")
        except Exception as e:
            print(f"插入数据失败: {e}")
    
    def get_all_names(self):
        """查询所有姓名记录"""
        try:
            select_sql = "SELECT id, first_name, last_name, full_name, created_date FROM names ORDER BY created_date DESC"
            self.cursor.execute(select_sql)
            rows = self.cursor.fetchall()
            
            if rows:
                print("\n=== 数据库中的所有姓名记录 ===")
                for row in rows:
                    print(f"ID: {row[0]}, 名: {row[1]}, 姓: {row[2]}, 全名: {row[3]}, 创建时间: {row[4]}")
            else:
                print("数据库中暂无记录")
        except Exception as e:
            print(f"查询数据失败: {e}")
    
    def close(self):
        """关闭数据库连接"""
        if hasattr(self, 'conn'):
            self.conn.close()
            print("数据库连接已关闭")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def main():
    """主函数"""
    # 初始化数据库
    db = NameDatabase()
    
    if not db.connect():
        print("无法连接到数据库，程序退出")
        return
    
    # 创建表
    db.create_table()
    
    try:
        while True:
            print("\n=== 姓名管理系统 ===")
            print("1. 添加新姓名")
            print("2. 查看所有姓名")
            print("3. 退出")
            
            choice = input("请选择操作 (1-3): ").strip()
            
            if choice == '1':
                # 输入姓名
                first_name = input("请输入名字: ").strip()
                last_name = input("请输入姓氏: ").strip()
                
                if first_name and last_name:
                    # 格式化姓名
                    formatted_name = get_formatted_name(first_name, last_name)
                    print(f"格式化后的姓名: {formatted_name}")
                    
                    # 保存到数据库
                    db.insert_name(first_name, last_name, formatted_name)
                else:
                    print("名字和姓氏不能为空！")
            
            elif choice == '2':
                # 查看所有记录
                db.get_all_names()
            
            elif choice == '3':
                print("谢谢使用！")
                break
            
            else:
                print("无效选择，请重新输入")
    
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    
    finally:
        # 关闭数据库连接
        db.close()

if __name__ == "__main__":
    main()