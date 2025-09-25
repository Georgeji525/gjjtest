import pandas as pd
from datetime import datetime, timedelta
import numpy as np

def create_sample_excel():
    """创建示例Excel文件用于测试"""
    
    # 创建示例数据
    dates = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
    
    data = {
        '日期': dates,
        '凭证号': [f'PZ{str(i).zfill(4)}' for i in range(1, len(dates) + 1)],
        '科目编号': [f'{1001 + i}' for i in range(len(dates))],
        '科目名称': ['库存现金', '银行存款', '应收账款', '存货', '固定资产', 
                   '应付账款', '短期借款', '实收资本', '利润分配', '主营业务收入']
    }
    
    # 创建DataFrame
    df = pd.DataFrame(data)
    
    # 保存为Excel文件
    output_file = '/workspace/test1.xlsx'
    df.to_excel(output_file, sheet_name='Sheet1', index=False)
    
    print(f"示例Excel文件已创建: {output_file}")
    print("文件内容:")
    print(df)
    
    return output_file

if __name__ == "__main__":
    create_sample_excel()