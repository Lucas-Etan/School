import pytest
from business_logic import calculate_gacha_probability


class TestGachaProbability:
    def test_base_probability(self):
        """测试基础概率：1-73抽应为0.6%"""
        for pull in range(1, 74):
            prob = calculate_gacha_probability(pull)
            assert prob == 0.006, f"第{pull}抽概率错误"

    def test_soft_pity_start(self):
        """测试软保底开始：第74抽概率应为6.6%"""
        prob = calculate_gacha_probability(74)
        assert prob == 0.066, "第74抽概率错误"

    def test_soft_pity_increase(self):
        """测试软保底递增：第74-89抽每抽递增6%"""
        expected_prob = 0.066
        for pull in range(74, 90):
            prob = calculate_gacha_probability(pull)
            assert prob == expected_prob, f"第{pull}抽概率错误"
            expected_prob += 0.06

    def test_hard_pity_guarantee(self):
        """测试硬保底：第90抽必定获取（概率100%）"""
        prob = calculate_gacha_probability(90)
        assert prob == 1.0, "第90抽概率错误"

    def test_invalid_pull_number(self):
        """测试无效的抽数：0或负数应抛出异常"""
        with pytest.raises(ValueError):
            calculate_gacha_probability(0)

        with pytest.raises(ValueError):
            calculate_gacha_probability(-1)

    def test_pull_over_90(self):
        """测试超过90抽：超过90抽应重置为新一轮保底"""
        prob = calculate_gacha_probability(91)
        assert prob == 0.006, "第91抽（新一轮第1抽）概率错误"