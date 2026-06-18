from manim import *
config.pixel_height = 1920*2
config.pixel_width = 1080*2

class EulerSinProduct(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2*PI, 2*PI, 1],
            y_range=[-3, 3, 1],
            x_length=4*PI,
            y_length=2*PI
        )

        axes.x_axis.add_labels({
            -2*PI: MathTex("-2\\pi"),
            -PI: MathTex("-\\pi"),
            PI: MathTex("\\pi"),
            2*PI: MathTex("2\\pi"),
        })
        for i, mob in enumerate(axes.x_axis.labels):
            mob.scale(1.2)
            if i in [1, 2]:
                mob.shift(0.1*DOWN)

        graph = axes.plot(
            lambda x: np.sin(x), 
            x_range=[-2*PI, 2*PI, 0.1],
            color=RED
        )
        
        self.play(Create(axes))
        self.wait(0.5)
        self.play(Create(graph))
        self.wait(0.5)
        self.play(VGroup(axes, graph).animate.shift(3*UP))
        self.wait(0.5)
        

        a1 = MathTex(r"\sin(x)=Ax(x^2-\pi^2)(x^2-4\pi^2)(x^2-9\pi^2)\cdots")
        a2 = MathTex(r"{\sin(x)\over x}=", r"A", r"(x^2-\pi^2)(x^2-4\pi^2)(x^2-9\pi^2)\cdots")
        a3 = MathTex(r"\lim_{x\to0}{\sin(x)\over x}")
        a4 = MathTex("1")
        a5 = MathTex("1", r"=\lim_{x\to0}A(x^2-\pi^2)(x^2-4\pi^2)(x^2-9\pi^2)\cdots")
        a6 = MathTex("1=", r"A(-\pi^2)(-4\pi^2)(-9\pi^2)\cdots")
        a7 = MathTex(r"A=\frac1{(-\pi^2)(-4\pi^2)(-9\pi^2)\cdots}")
        a8 = MathTex(
            r"{\sin(x)\over x}=", 
            r"{(x^2-\pi^2)", r"(x^2-4\pi^2)", r"(x^2-9\pi^2)\cdots", 
            r"\over", r"(-\pi^2)", r"(-4\pi^2)", r"(-9\pi^2)", r"\cdots}"
        )
        a9 = MathTex(
            r"{\sin(x)\over x}=", 
            r"{x^2-\pi^2", r"\over", r"-\pi^2", r"}\cdot{", r"x^2-4\pi^2", r"\over", 
            r"-4\pi^2", r"}\cdot{", r"x^2-9\pi^2", r"\over", r"-9\pi^2", r"}\cdots"
        )
        a10 = MathTex(r"{\sin(x)\over x}=", r"\prod_{n=1}^\infty\left({x^2-n^2\pi^2\over-n^2\pi^2}\right)")
        a11 = MathTex(r"{\sin(x)\over x}=\prod_{n=1}^\infty\left(1-{x^2\over n^2\pi^2}\right)")
        a12 = MathTex(r"\sin(x)=x\prod_{n=1}^\infty\left(1-{x^2\over n^2\pi^2}\right)")
        VGroup(a1, a2, a8, a9, a10, a11, a12).shift(2*DOWN).scale(1.2)
        VGroup(a3, a4, a5, a6, a7).next_to(a2, 2*DOWN).scale(1.2)

        self.play(Write(a1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a1, a2))
        self.wait(0.5)
        self.play(Write(a3))
        self.wait(0.5)
        self.play(ReplacementTransform(a3, a4))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a4, a5[0]))
        self.wait(0.5)
        self.play(Write(a5[1]))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a5, a6))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a6, a7))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(VGroup(a2[0], a2[2]), a8[:4]),
            ReplacementTransform(a2[1], a8[4:])
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(a8[0], a9[0]),
            TransformMatchingShapes(a8[1], a9[1]),
            TransformMatchingShapes(a8[2], a9[5]),
            TransformMatchingShapes(a8[3], a9[9]),
            TransformMatchingShapes(a8[5], a9[3]),
            TransformMatchingShapes(a8[6], a9[7]),
            TransformMatchingShapes(a8[7], a9[-2]),
            TransformMatchingShapes(a8[8], a9[-1]),
            ReplacementTransform(a8[4], VGroup(a9[2], a9[4], a9[6], a9[8], a9[10]))
        )
        self.wait(0.5)
        self.play(FadeOut(a7))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(a9[0], a10[0]),
            ReplacementTransform(a9[1:], a10[1])
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(a10, a11))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a11, a12))
        self.wait(0.5)
        self.play(Circumscribe(a12))