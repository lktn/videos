from manim import *
class Scene(Scene):
    def construct(self):
        a1 = MathTex(r"\int\frac1{x^6+1}dx")
        self.play(Write(a1))

        a2 = MathTex(r"\int\frac1{(x^2+1)(x^4-x^2+1)}dx")
        a3 = MathTex(r"\int\frac{x^2+1-x^2}{(x^2+1)(x^4-x^2+1)}dx")
        a4 = MathTex(r"\int\frac{x^2+1}{(x^2+1)(x^4-x^2+1)}dx-\int\frac{x^2}{x^6+1}dx")
        a5 = MathTex(r"\int\frac1{x^4-x^2+1}dx-\int\frac{x^2}{x^6+1}dx")
        for t in [a2, a3, a4, a5]:
            self.play(Transform(a1, t))
        self.play(a1.animate.move_to([-2.5, 3, 0]))

        a6 = MathTex(r"\int\frac{x^2}{x^6+1}dx")
        self.play(Write(a6))

        a7 = MathTex(r"\int\frac{x^2}{(x^3)^2+1}dx")
        self.play(ReplacementTransform(a6, a7))

        a8 = MathTex(r"u=x^3").move_to([2, 0.5, 0])
        self.play(a7.animate.move_to(2*LEFT), Write(a8))
        
        a9 = MathTex(r"du=3x^2dx").move_to([2, -0.2, 0])
        self.play(Write(a9))

        a10 = MathTex(r"\int\frac{x^2}{u^2+1}\frac{du}{3x^2}").move_to(2*LEFT)
        a11 = MathTex(r"\frac13\int\frac{x^2}{u^2+1}du").move_to(2*LEFT)
        a12 = MathTex(r"\frac13\arctan(u)").move_to(2*LEFT)
        for t in [a10, a11, a12]:
            self.play(Transform(a7, t))

        a13 = MathTex(r"\int\frac{x^2}{x^6+1}dx=\frac13\arctan(x^3)+c_0")
        self.play(ReplacementTransform(a7, a13), FadeOut(VGroup(a8, a9)))

        a14 = MathTex(r"\int\frac1{x^4-x^2+1}dx-\frac13\arctan(x^3)").move_to([-2.5, 3, 0])
        self.play(ReplacementTransform(a1, a14))

        a15 = MathTex(r"\int\frac1{x^4-x^2+1}dx")
        a16 = MathTex(r"\int\frac1{x^4-x^2+1+3x^2-3x^2}dx")
        a17 = MathTex(r"\int\frac1{x^4+2x^2+1-3x^2}dx")
        a18 = MathTex(r"\int\frac1{(x^2+1)^2-(\sqrt3x)^2}dx")
        a19 = MathTex(r"\int\frac1{(x^2+\sqrt3x+1)(x^2-\sqrt3x+1)}dx")
        for t in [a15, a16, a17, a18, a19]:
            self.play(Transform(a13, t))
        self.play(a13.animate.move_to([-2.5, -3, 0]))

        a20 = MathTex(r"\frac1{(x^2+\sqrt3x+1)(x^2-\sqrt3x+1)}=\frac{Ax+B}{x^2+\sqrt3x+1}+\frac{Cx+D}{x^2-\sqrt3x+1}")
        self.play(Write(a20))

        a21 = MathTex(r"\int\frac{Ax+B}{x^2+\sqrt3x+1}dx+\int\frac{Cx+D}{x^2-\sqrt3x+1}dx").move_to([-2.5, -3, 0])
        self.play(ReplacementTransform(a13, a21))

        a22 = MathTex(r"1=(Ax+B)(x^2-\sqrt3x+1)+(Cx+D)(x^2+\sqrt3x+1)")
        a23 = MathTex(
            r"1=&(A+C)x^3+(B+D-A\sqrt3+C\sqrt3)x^2+\\",
            r"&(A+C-B\sqrt3+D\sqrt3)x+(B+D)"
        )
        a24 = MathTex(
            r"A+C=0\quad\quad&B+D=1\\",
            r"B+D-A\sqrt3+C\sqrt3=0\quad\quad&A+C-\sqrt3+D\sqrt3=0"
        )
        a25 = MathTex(
            r"A=-C\quad\quad&B+D=1\\",
            r"A-C=\frac1{\sqrt3}\quad\quad&D=B"
        )
        a26 = MathTex(
            r"A=\frac1{2\sqrt3}\quad\quad&B=\frac12\\",
            r"C=-\frac1{2\sqrt3}\quad\quad&D=\frac12"
        )
        for t in [a22, a23, a24, a25, a26]:
            self.play(Transform(a20, t))

        a27 = MathTex(r"A=\frac1{2\sqrt3}\quad B=\frac12\quad C=-\frac1{2\sqrt3}\quad D=\frac12").move_to(-2*UP)
        self.play(a21.animate.move_to([0, 0, 0]), FadeOut(a20), FadeIn(a27))

        a28 = MathTex(r"\int\frac{\frac1{2\sqrt3}x+\frac12}{x^2+\sqrt3x+1}dx+\int\frac{-\frac1{2\sqrt3}x+\frac12}{x^2-\sqrt3x+1}dx")
        self.play(Transform(a21, a28))

        a29 = MathTex(r"\frac1{2\sqrt3}\int\frac{x+\sqrt3}{x^2+\sqrt3x+1}dx-\frac1{2\sqrt3}\int\frac{x-\sqrt3}{x^2-\sqrt3x+1}dx")
        self.play(Transform(a21, a29), FadeOut(a27))

        a30 = MathTex(r"\frac1{2\sqrt3}\int\frac{x+\frac{\sqrt3}2+\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx-\frac1{2\sqrt3}\int\frac{x-\frac{\sqrt3}2-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx")
        a31 = MathTex(
            r"\frac1{2\sqrt3}\int\frac{x+\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx+\frac1{2\sqrt3}\int\frac{\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx\\",
            r"-\frac1{2\sqrt3}\int\frac{x-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx-\frac1{2\sqrt3}\int\frac{-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx")
        for t in [a30, a31]:
            self.play(Transform(a21, t))

        a32 = MathTex(r"&v=x^2+\sqrt3x+1\quad dv=(2x+\sqrt3)dx\\", r"&w=x^2-\sqrt3x+1\quad dw=(2x-\sqrt3)dx").move_to([-1.5, -3, 0])
        self.play(Write(a32[0]), Write(a32[1]))

        a33 = MathTex(
            r"\frac1{2\sqrt3}\int\frac{x+\frac{\sqrt3}2}v\frac{dv}{2x+\sqrt3}+\frac1{2\sqrt3}\int\frac{\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx\\",
            r"-\frac1{2\sqrt3}\int\frac{x-\frac{\sqrt3}2}w\frac{dw}{2x-\sqrt3}-\frac1{2\sqrt3}\int\frac{-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx")
        a34 = MathTex(
            r"\frac1{4\sqrt3}\int\frac1vdv+\frac1{2\sqrt3}\int\frac{\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx\\",
            r"-\frac1{4\sqrt3}\int\frac1wdw-\frac1{2\sqrt3}\int\frac{-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx")
        a35 = MathTex(
            r"\frac1{4\sqrt3}\log|v|+\frac1{2\sqrt3}\int\frac{\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx\\",
            r"-\frac1{4\sqrt3}\log|w|-\frac1{2\sqrt3}\int\frac{-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx")
        for t in [a33, a34, a35]:
            self.play(Transform(a21, t))

        a36 = MathTex(
            r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac1{2\sqrt3}\int\frac{\frac{\sqrt3}2}{x^2+\sqrt3x+1}dx\\",
            r"-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)-\frac1{2\sqrt3}\int\frac{-\frac{\sqrt3}2}{x^2-\sqrt3x+1}dx")
        self.play(Transform(a21, a36), FadeOut(a32))

        a37 = MathTex(
            r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac14\int\frac1{x^2+\sqrt3x+\frac34+\frac14}dx\\",
            r"-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)+\frac14\int\frac1{x^2-\sqrt3x+\frac34+\frac14}dx")
        a38 = MathTex(
            r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac14\int\frac1{x^2+2\frac{\sqrt3}2x+\left(\frac{\sqrt3}2\right)^2+\frac14}dx\\",
            r"-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)+\frac14\int\frac1{x^2-2\frac{\sqrt3}2x+\left(\frac{\sqrt3}2\right)^2+\frac14}dx")
        a39 = MathTex(
            r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac14\int\frac1{(x+\frac{\sqrt3}2)^2+\frac14}dx\\",
            r"-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)+\frac14\int\frac1{(x+\frac{\sqrt3}2)^2+\frac14}dx")
        for t in [a37, a38, a39]:
            self.play(Transform(a21, t))

        a40 = MathTex(r"s=x+\frac{\sqrt3}2\quad ds=dx").move_to([1.7, -2.3, 0])
        a41 = MathTex(r"t=x-\frac{\sqrt3}2\quad dt=dx").move_to([2.2, -3.3, 0])
        self.play(Write(VGroup(a40, a41)))

        a42 = MathTex(
            r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac14\int\frac1{s^2+\left(\frac12\right)^2}dt\\",
            r"-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)+\frac14\int\frac1{t^2+\left(\frac12\right)^2}dt")
        a43 = MathTex(r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac14(2\arctan(2s))\\-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)+\frac14(2\arctan(2s))")
        for t in [a42, a43]:
            self.play(Transform(a21, t))

        a44 = MathTex(r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)+\frac12\arctan(2x+\sqrt3)\\-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)+\frac12\arctan(2x-\sqrt3)")
        self.play(Transform(a21, a44), FadeOut(VGroup(a40, a41)))

        a45 = MathTex(r"\frac1{4\sqrt3}\log(x^2+\sqrt3x+1)-\frac1{4\sqrt3}\log(x^2-\sqrt3x+1)\\+\frac12\arctan(2x+\sqrt3)+\frac12\arctan(2x-\sqrt3)")
        a46 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\left(\arctan(2x+\sqrt3)+\arctan(2x-\sqrt3)\right)")
        a47 = MathTex(
            r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\",
            r"&+\frac12\left(\arctan\left(\frac{2x+\sqrt3+2x-\sqrt3}{1-(2x+\sqrt3)(2x-\sqrt3)}\right)\right)")
        a48 = MathTex(
            r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\",
            r"&+\frac12\left(\arctan\left(\frac{4x}{1-(4x^2-3)}\right)\right)")
        a49 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\left(\arctan\left(\frac{4x}{4-4x^2}\right)\right)")
        a50 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\left(\arctan\left(\frac{x}{1-x^2}\right)\right)")
        a51 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\left(\arctan\left(\frac{x(1+x^2)}{(1-x^2)(1+x^2)}\right)\right)")
        a52 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\left(\arctan\left(\frac{x+x^3}{1-x^4}\right)\right)")
        a53 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\left(\arctan(x)+\arctan(x^3)\right)")
        a54 = MathTex(r"\int\frac1{x^4-x^2+1}dx=\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\+\frac12\arctan(x)+\frac12\arctan(x^3)+c_1")
        for t in [a45, a46, a47, a48, a49, a50, a51, a52, a53, a54]:
            self.play(Transform(a21, t))

        a55 = MathTex(r"&\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\&+\frac12\arctan(x)+\frac12\arctan(x^3)-\frac13\arctan(x^3)")
        self.play(Transform(a14, a55), FadeOut(a21))
        a56 = MathTex(r"\int\frac1{x^6+1}dx=\frac1{4\sqrt3}\log\left(\frac{x^2+\sqrt3x+1}{x^2-\sqrt3x+1}\right)\\+\frac12\arctan(x)+\frac16\arctan(x^3)+c")
        self.play(Transform(a14, a56))