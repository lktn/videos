from manim import *

class QuarticFormula(Scene):
    def construct(self):
        a = MathTex("ax^4+bx^3+cx^2+dx+e=0").scale(1.4)
        self.play(Write(a), run_time=2)
        self.wait(2)

        a1 = MathTex("ax^4+bx^3+cx^2+dx+e=0").move_to((3)*UP).scale(1.4)
        self.play(Transform(a, a1))
        self.wait(1)

        vb = MathTex(r"&x=-\frac{b}{4a}\pm\frac{1}{2}\sqrt{\frac{3b^2-8ac}{12a^2}+\frac{1}{3a}\left(\sqrt[3]{\frac{2c^3-9bcd+27b^2e+27ad^2-72ace+\sqrt{\left(2c^3-9bcd+27b^2e+27ad^2-72ace\right)^2-4\left(c^2-3bd+12ae\right)^3}}{2}}+\frac{c^2-3bd+12ae}{\sqrt[3]{\frac{2c^3-9bcd+27b^2e+27ad^2-72ace+\sqrt{\left(2c^3-9bcd+27b^2e+27ad^2-72ace\right)^2-4\left(c^2-3bd+12ae\right)^3}}{2}}}\right)}\pm\frac{1}{2}\sqrt{-4\left(\frac{1}{2}\sqrt{\frac{3b^2-8ac}{12a^2}+\frac{1}{3a}\left(\sqrt[3]{\frac{2c^3-9bcd+27b^2e+27ad^2-72ace+\sqrt{\left(2c^3-9bcd+27b^2e+27ad^2-72ace\right)^2-4\left(c^2-3bd+12ae\right)^3}}{2}}+\frac{c^2-3bd+12ae}{\sqrt[3]{\frac{2c^3-9bcd+27b^2e+27ad^2-72ace+\sqrt{\left(2c^3-9bcd+27b^2e+27ad^2-72ace\right)^2-4\left(c^2-3bd+12ae\right)^3}}{2}}}\right)}\right)^2-\frac{8ac-3b^2}{4a^2}+\frac{\frac{b^3-4abc+8a^2d}{8a^3}}{\frac{1}{2}\sqrt{\frac{3b^2-8ac}{12a^2}+\frac{1}{3a}\left(\sqrt[3]{\frac{2c^3-9bcd+27b^2e+27ad^2-72ace+\sqrt{\left(2c^3-9bcd+27b^2e+27ad^2-72ace\right)^2-4\left(c^2-3bd+12ae\right)^3}}{2}}+\frac{c^2-3bd+12ae}{\sqrt[3]{\frac{2c^3-9bcd+27b^2e+27ad^2-72ace+\sqrt{2c^3-9bcd+27b^2e+27ad^2-72ace^2-4\left(c^2-3bd+12ae\right)^3}}{2}}}\right)}}}").scale(1)
        vb.move_to((61)*RIGHT)
        self.play(Create(vb))
        self.wait(3)

        self.play(vb.animate.shift(LEFT*(122)), run_time=15)
        self.wait(5)