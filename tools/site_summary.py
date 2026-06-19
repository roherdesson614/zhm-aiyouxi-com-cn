import json
import os
from textwrap import dedent

# 站点资料配置
SITE_DATA = {
    "name": "爱游戏",
    "url": "https://zhm-aiyouxi.com.cn",
    "keywords": ["爱游戏", "游戏资讯", "游戏评测"],
    "tags": ["游戏", "资讯", "评测"],
    "description": "提供最新游戏资讯、深度评测与玩家社区互动。",
    "category": "游戏门户",
    "language": "zh-CN",
    "created": "2023-05-10",
    "status": "active"
}

# 附加关键词列表
ADDITIONAL_KEYWORDS = [
    "游戏攻略", "单机游戏", "网络游戏", "手机游戏",
    "电竞赛事", "游戏推荐", "新游上线", "游戏活动"
]


def format_summary(data: dict, extra_keywords: list) -> str:
    """格式化结构化摘要"""
    lines = []
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"站点URL：{data['url']}")
    lines.append(f"核心关键词：{'、'.join(data['keywords'])}")
    lines.append(f"补充关键词：{'、'.join(extra_keywords[:4])}")
    lines.append(f"标签：{' '.join('#' + tag for tag in data['tags'])}")
    lines.append(f"简短说明：{data['description']}")
    lines.append(f"分类：{data['category']}")
    lines.append(f"语言：{data['language']}")
    lines.append(f"创建时间：{data['created']}")
    lines.append(f"站点状态：{data['status']}")
    return "\n".join(lines)


def structured_block(data: dict, extra_keywords: list) -> dict:
    """生成结构化的块数据"""
    return {
        "header": {
            "type": "site_summary",
            "version": "1.0"
        },
        "site": {
            "name": data["name"],
            "url": data["url"],
            "keywords": data["keywords"] + extra_keywords[:2],
            "tags": data["tags"],
            "description": data["description"],
            "category": data["category"],
            "language": data["language"],
            "created": data["created"],
            "status": data["status"]
        },
        "metadata": {
            "generator": "site_summary.py",
            "format": "json"
        }
    }


def save_summary_to_file(content: str, filename: str = "site_summary.txt") -> bool:
    """将摘要内容保存到文本文件"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"写入文件时出错：{e}")
        return False


def save_structured_json(data: dict, filename: str = "site_summary.json") -> bool:
    """将结构化数据保存为JSON文件"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"写入JSON文件时出错：{e}")
        return False


def print_separator(char: str = "=", length: int = 48):
    """打印分隔线"""
    print(char * length)


def main():
    """主函数：生成并输出站点摘要"""
    # 生成文本摘要
    summary_text = format_summary(SITE_DATA, ADDITIONAL_KEYWORDS)
    # 生成结构化块
    block = structured_block(SITE_DATA, ADDITIONAL_KEYWORDS)

    print_separator("=")
    print("站点摘要（文本格式）：")
    print_separator("-")
    print(summary_text)

    print()
    print_separator("=")
    print("站点摘要（结构化JSON）：")
    print_separator("-")
    print(json.dumps(block, ensure_ascii=False, indent=2))

    # 可选：保存到文件
    text_saved = save_summary_to_file(summary_text)
    json_saved = save_structured_json(block)

    if text_saved and json_saved:
        print()
        print("摘要已保存到文件：site_summary.txt 和 site_summary.json")


if __name__ == "__main__":
    main()