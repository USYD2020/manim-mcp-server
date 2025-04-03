from manim import *


class SineWaveScene(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
            x_length=8,
            y_length=4
        )

        # 添加坐标轴标签
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # 创建正弦函数
        sine_function = axes.plot(
            lambda x: np.sin(x),
            color=YELLOW
        )

        # 创建动画
        self.play(Create(axes), Create(x_label), Create(y_label), run_time=1)
        self.play(
            Create(sine_function),
            run_time=4  # 4秒绘制正弦波，加上之前的1秒正好是5秒
        )
        self.wait(0.5)  # 结尾暂停0.5秒


if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = SineWaveScene()
        scene.render()
