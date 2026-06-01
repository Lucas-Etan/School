def calculate_gacha_probability(pull_num: int) -> float:
    """
    计算原神抽卡系统中指定抽数的五星角色获取概率
    """
    # 输入验证
    if not isinstance(pull_num, int) or pull_num <= 0:
        raise ValueError("抽数必须是正整数")

    # 将抽数映射到0-90的保底周期内
    cycle_pull = ((pull_num - 1) % 90) + 1

    # 硬保底：第90抽必定出货
    if cycle_pull == 90:
        return 1.0

    # 软保底机制：从第74抽开始，每抽增加6%（即0.06）
    if cycle_pull >= 74:
        # 预计算所有概率值，使用累加方式确保与测试一致
        probabilities = [0.006] * 73  # 1-73抽
        prob = 0.006
        for i in range(74, 90):
            prob += 0.06
            probabilities.append(prob)
        probabilities.append(1.0)  # 第90抽

        # 返回对应抽数的概率
        return probabilities[cycle_pull - 1]
    else:
        return 0.006