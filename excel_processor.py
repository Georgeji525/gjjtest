import pandas as pd
import os
from pathlib import Path

def process_excel_data(source_file, output_file=None):
    """
    处理Excel文件数据，提取指定列并格式化日期
    
    Args:
        source_file (str): 源Excel文件路径
        output_file (str, optional): 输出文件路径，如果不指定则自动生成
    """
    try:
        # 检查源文件是否存在
        if not os.path.exists(source_file):
            print(f"错误：源文件 {source_file} 不存在")
            return False
        
        print(f"正在读取文件: {source_file}")
        
        # 读取Excel文件
        g = pd.read_excel(
            source_file,  # Excel文件路径
            sheet_name='Sheet1',  # 获取'Sheet1'工作表的数据
            header=0,  # 取第1行的值作为列名
            index_col=0,  # 把第1列数据设置为索引列
            usecols=['日期','凭证号','科目编号','科目名称'],  # 只取指定列数据
            dtype={'凭证号': str, '科目编号': str},  # 把凭证号、科目编号这2列的数据类型修改为字符
        )
        
        print(f"成功读取数据，共 {len(g)} 行")
        print(f"列名: {list(g.columns)}")
        print(f"索引名: {g.index.name}")
        
        # 检查索引是否为日期类型，如果是则格式化
        if g.index.name == '日期':
            print("正在格式化日期索引...")
            _idx_dt = pd.to_datetime(g.index, errors='coerce')
            g.index = _idx_dt.strftime('%Y/%m/%d')
            print("日期格式化完成")
        
        # 设置输出路径
        if output_file is None:
            source_path = Path(source_file)
            output_file = source_path.parent / f"处理后的数据_{source_path.stem}.xlsx"
        
        # 保存处理后的数据
        print(f"正在保存到: {output_file}")
        g.to_excel(output_file, index=True)  # index=True表示保留索引列
        
        print(f"文件已成功保存到: {output_file}")
        print(f"数据预览:")
        print(g.head())
        
        return True
        
    except FileNotFoundError:
        print(f"错误：找不到文件 {source_file}")
        return False
    except pd.errors.EmptyDataError:
        print("错误：Excel文件为空")
        return False
    except KeyError as e:
        print(f"错误：找不到指定的列或工作表: {e}")
        return False
    except Exception as e:
        print(f"处理过程中发生错误: {e}")
        return False

if __name__ == "__main__":
    # 原始代码示例
    source_file = "D:\\test1.xlsx"  # 你可以修改这个路径
    
    # 如果在Linux环境下，使用不同的路径
    if os.name != 'nt':  # 不是Windows系统
        source_file = "/workspace/test1.xlsx"  # Linux路径示例
    
    # 处理数据
    success = process_excel_data(source_file)
    
    if not success:
        print("\n提示：请确保Excel文件存在并包含以下列：")
        print("- 日期")
        print("- 凭证号") 
        print("- 科目编号")
        print("- 科目名称")
        print("工作表名称应为'Sheet1'")