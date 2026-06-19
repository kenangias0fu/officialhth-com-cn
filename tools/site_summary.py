def main():
    # 站点摘要数据
    site_data = {
        "title": "华体会体育",
        "url": "https://officialhth.com.cn",
        "keywords": ["华体会", "体育赛事", "在线娱乐"],
        "tags": ["体育", "娱乐", "品牌"],
        "description": "华体会体育是一家专注于体育赛事与在线娱乐的综合平台，提供丰富多样的体育资讯及互动服务。"
    }

    # 生成摘要字符串
    summary_lines = [
        "===== 站点摘要 =====",
        f"标题: {site_data['title']}",
        f"URL: {site_data['url']}",
        f"关键词: {', '.join(site_data['keywords'])}",
        f"标签: {', '.join(site_data['tags'])}",
        f"说明: {site_data['description']}",
        "===================="
    ]

    # 输出摘要
    for line in summary_lines:
        print(line)

    # 附加统计信息
    print(f"\n关键词数量: {len(site_data['keywords'])}")
    print(f"标签数量: {len(site_data['tags'])}")
    print(f"描述长度: {len(site_data['description'])} 字符")

    # 额外格式化输出（用于展示）
    print("\n--- 结构化摘要 ---")
    print(f"| {'项目':<10} | {'内容':<50} |")
    print(f"|{'-'*12}|{'-'*52}|")
    print(f"| {'标题':<10} | {site_data['title']:<50} |")
    print(f"| {'URL':<10} | {site_data['url']:<50} |")
    print(f"| {'关键词':<10} | {', '.join(site_data['keywords']):<50} |")
    print(f"| {'标签':<10} | {', '.join(site_data['tags']):<50} |")
    print(f"| {'说明':<10} | {site_data['description']:<50} |")

    # 可选地生成摘要文件
    output_file = "site_summary_output.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for line in summary_lines:
                f.write(line + "\n")
            f.write(f"\n关键词数量: {len(site_data['keywords'])}\n")
            f.write(f"标签数量: {len(site_data['tags'])}\n")
            f.write(f"描述长度: {len(site_data['description'])} 字符\n")
        print(f"\n摘要已保存至: {output_file}")
    except IOError as e:
        print(f"\n写入文件失败: {e}")

    # 返回站点字典以备后续使用
    return site_data

if __name__ == "__main__":
    site_dict = main()
    # 无额外操作，仅确保运行安全