import pandas as pd
import os

# 修正后的代码
print("=== 修正后的代码 ===\n")

# 设置文件路径（根据操作系统自动调整）
if os.name == 'nt':  # Windows系统
    source_file = "D:\\test1.xlsx"
    output_path = "D:\\处理后的数据.xlsx"
else:  # Linux/Mac系统
    source_file = "/workspace/test1.xlsx"
    output_path = "/workspace/处理后的数据.xlsx"

try:
    # 检查文件是否存在
    if not os.path.exists(source_file):
        print(f"错误：文件 {source_file} 不存在")
        exit(1)
    
    print(f"正在读取文件: {source_file}")
    
    # 读取Excel文件
    g = pd.read_excel(source_file,  # Excel文件路径
        sheet_name='Sheet1',  # 获取'Sheet1'工作表的数据
        header=0,  # 取第1行的值作为列名
        index_col=0,  # 把第1列数据设置为索引列
        usecols=['日期','凭证号','科目编号','科目名称'],  # 只取指定列数据
        dtype={'凭证号': str, '科目编号': str},  # 把凭证号、科目编号这2列的数据类型修改为字符
    )
    
    print(f"成功读取数据，共 {len(g)} 行")
    print(f"索引名称: {g.index.name}")
    print(f"列名: {list(g.columns)}")
    
    # 修正：正确的条件判断
    if g.index.name == '日期':  # 修正：使用 g.index.name 而不是 g.index
        print("检测到日期索引，开始格式化...")
        _idx_dt = pd.to_datetime(g.index, errors='coerce')
        g.index = _idx_dt.strftime('%Y/%m/%d')
        print("日期格式化完成")
    else:
        print(f"索引不是日期列（当前索引名: {g.index.name}）")
    
    # 保存处理后的数据
    print(f"正在保存到: {output_path}")
    g.to_excel(output_path, index=True)  # index=True表示保留索引列
    print(f"文件已保存到: {output_path}")
    
    # 显示处理后的数据预览
    print("\n数据预览:")
    print(g.head())
    
except FileNotFoundError:
    print(f"错误：找不到文件 {source_file}")
except KeyError as e:
    print(f"错误：找不到指定的列或工作表: {e}")
    print("请确保Excel文件包含以下列：日期、凭证号、科目编号、科目名称")
except Exception as e:
    print(f"处理过程中发生错误: {e}")

print("\n=== 主要修正内容 ===")
print("1. 修正条件判断：if g.index.name == '日期' （而不是 if g.index == '日期'）")
print("2. 添加了文件存在性检查")
print("3. 添加了异常处理")
print("4. 根据操作系统自动调整文件路径")
print("5. 添加了更详细的输出信息")